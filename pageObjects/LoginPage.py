
class LoginPage:
    textbox_userid_id = "userName"
    textbox_password_id = "password"
    button_login_id = "login"
    button_newUser_id = "newUser"
    label_failedLoginMsg_id = "name"

    def __init__(self,driver):
        self.driver = driver

    def enter_user_id(self,login):
        self.driver.find_element_by_id(self.textbox_userid_id).send_keys(login)

    def enter_password(self,pwd):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def click_new_user(self):
        self.driver.find_element_by_id(self.button_newUser_id).click()