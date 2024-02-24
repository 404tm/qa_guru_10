from selene.support.shared import browser
from demoqa_tests.data.users import User


class SimpleUserRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#firstName')
        self.email = browser.element('[id="userEmail"]')
        self.currentAddress = browser.element('#currentAddress')
        self.submit_button = browser.element('[id="submit"]')
        #self.gender = browser.all('[class="custom-control custom-radio custom-control-inline"]')

    class locators:
        full_name = '#userName'
        email = '#mail'

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_adress(self, value):
        self.currentAddress.type(value)

    def submit(self):
        self.submit_button.click()

    def should_have_submited(self, full_name, email):
        pass

    def register(self, user: User):
        self.fill_email(user.email)
        self.fill_full_name(user.full_name)
        self.fill_adress(user.currentAddress)
        self.submit()
        return self
