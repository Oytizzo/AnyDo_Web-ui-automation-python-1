from selenium.webdriver.common.by import By


class MainPageLocator:
    LOGIN_WITH_FACEBOOK = (By.CLASS_NAME, 'AppLoginButton--facebook')
    LOGIN_WITH_GOOGLE = (By.CLASS_NAME, 'AppLoginButton--google')
    LOGIN_WITH_EMAIL = (By.CLASS_NAME, 'AppLoginButton--email')


class LoginPageLocator:
    EMAIL = (By.XPATH, '/html/body/div/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/input')
    EMAIL_ARROW = (By.XPATH, '/html/body/div/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form/div/button')
    PASSWORD = (By.XPATH, '/html/body/div/div[1]/section/div/div[3]/div/div/div/div[2]/div/div[2]/form[2]/div/input')
