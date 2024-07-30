# glpi_api/api.py

import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class GLPIAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.login()

    def login(self):
        login_url = f"{self.base_url}/front/login.php"
        
        # Configurar Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Ejecutar en modo headless
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        
        # Navegar a la página de login
        driver.get(login_url)
        
        # Encontrar y llenar los campos de login utilizando los XPaths proporcionados
        user_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/form/div/div/div[2]/input")
        password_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/form/div/div/div[3]/input")
        login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/form/div/div/div[6]/button")
        
        user_input.send_keys(self.username)
        password_input.send_keys(self.password)
        
        # Desplazarse al botón de inicio de sesión y hacer clic
        actions = ActionChains(driver)
        actions.move_to_element(login_button).perform()
        driver.execute_script("arguments[0].scrollIntoView();", login_button)
        login_button.click()
        
        # Obtener cookies y CSRF token
        cookies = driver.get_cookies()
        csrf_token = driver.find_element(By.NAME, '_glpi_csrf_token').get_attribute('value')
        
        driver.quit()
        
        # Configurar sesión de requests con cookies y CSRF token
        for cookie in cookies:
            self.session.cookies.set(cookie['name'], cookie['value'])
        self.session.headers.update({'X-CSRF-Token': csrf_token})

    def create_ticket(self, title, content, urgency=3, requester_id=None, assigned_id=None):
        create_ticket_url = f"{self.base_url}/front/ticket.form.php"
        response = self.session.get(create_ticket_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer el token del formulario
        form_token = soup.find('input', {'name': '_glpi_csrf_token'})['value']
        
        payload = {
            '_glpi_csrf_token': form_token,
            'name': title,
            'content': content,
            'urgency': urgency,
            'add': 'Agregar'
        }

        if requester_id:
            payload['_users_id_requester'] = requester_id
        if assigned_id:
            payload['_users_id_assign'] = assigned_id
        
        response = self.session.post(create_ticket_url, data=payload, allow_redirects=False)
        
        if response.status_code == 302:
            redirect_url = response.headers['Location']
            response = self.session.get(f"{self.base_url}{redirect_url}")

        response_text = response.text
        
        if response.status_code == 200:
            ticket_id = self.extract_ticket_id_from_message(response_text)
            if ticket_id:
                return {"message": "Ticket created successfully", "ticket_id": ticket_id}
            else:
                return {"message": "Ticket created successfully, but could not extract ticket ID"}
        else:
            return {"message": "Failed to create ticket", "details": response_text}

    def extract_ticket_id_from_message(self, response_text):
        # Buscar el ID del ticket en el mensaje de éxito
        soup = BeautifulSoup(response_text, 'html.parser')
        toast_container = soup.find('div', {'id': 'messages_after_redirect'})
        if toast_container:
            toast_body = toast_container.find('div', {'class': 'toast-body'})
            if toast_body:
                ticket_link = toast_body.find('a', href=True)
                if ticket_link:
                    ticket_id_match = re.search(r'id=(\d+)', ticket_link['href'])
                    if ticket_id_match:
                        return ticket_id_match.group(1)
        return None

    def close(self):
        self.session.close()
