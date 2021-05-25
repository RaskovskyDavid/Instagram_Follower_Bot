from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from secret import user, password

chrome_driver_path = "C:\workspacePython\chromedriver.exe"

SIMILAR_ACCOUNT = "larutadelagarnacha"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        time.sleep(2)
        user_login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_login.send_keys(user)
        pass_login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_login.send_keys(password)
        pass_login.send_keys(Keys.ENTER)
        time.sleep(2)

        try:
            pop = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
            pop.click()
        except NoSuchElementException:
            print("Pop up ¿Guardar tu información de inicio de sesión? no salio")
        try:
            pop = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            pop.click()
        except NoSuchElementException:
            print("Pop up Activar notificaciones no salio")

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        amount_followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
        quantity = str(amount_followers.text)
        converted_quantity = ""
        for char in quantity:
            if char.isnumeric():
                converted_quantity += char
        total_follower = int(converted_quantity) // 50
        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(total_follower):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector(' div > div.Pkbci > button')
        print(len(all_buttons))
        for button in all_buttons:
            if button.text == 'Seguir':
                button.click()
                time.sleep(1)

