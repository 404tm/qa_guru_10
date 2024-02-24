from selene import browser, be, have

browser.config.windows_width = 1920
browser.config.windows_height = 1080

def test_automation_practice_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Yaroslav')
    browser.element('[id="lastName"]').type('Martynov')
    browser.element('[id="userEmail"]').type('404tm2@mail.ru')
    browser.all('[class="custom-control custom-radio custom-control-inline"]').element_by(have.exact_text("Female")).click()
    browser.element('[id="userNumber"]').should(be.blank).type('9058687171')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__year-select"]').element('[value="1993"]').click()
    browser.element('[class="react-datepicker__month-select"]').element('[value="6"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--004 react-datepicker__day--weekend"]').click()
    browser.all('[class="custom-control custom-checkbox custom-control-inline"]').element_by(have.exact_text("Sports")).click()
    browser.element('[id="currentAddress"]').type("Нижний Новгород. Советский район. ул. Белинского")
    #browser.element('[class="btn.btn-primary"]').click()