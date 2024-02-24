import time

import pytest
from selene import browser, be, have



@pytest.fixture()

def setup():

    yield
    browser.quit()

def test_open_page():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_non_result():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qdfbnmd,/sg;lkodfy!@#PO(*^TGVMOI&^%RFBLP(^RF').press_enter()
    time.sleep(5)
    browser.element('[class="card-section"]').should(have.text('qdfbnmd,/sg;lkodfy!@#PO(*^TGVMOI&^%RFBLP(^RF'))


#5. Добавьте еще один тест на поиск, который проверит, что поиск не выдает результатов по вашему запросу:

#- вводим строку, по которой не ожидаем результатов (придумайте случайный набор символов)

#- проверяем, что поиск не выдает результатов, и пишет об этом сообщение