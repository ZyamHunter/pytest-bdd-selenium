from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

feature_file_path = os.path.abspath('Features/search.feature')

@scenario(feature_file_path, 'Pesquisar informação na página home')
def test_publish():
    pass


@given('Que esteja na página home')
def step_impl(browser):
    browser.get('https://www.google.com/')

    wait = WebDriverWait(browser, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    img_google = wait.until(EC.visibility_of_element_located(
        (By.XPATH, '//img[@alt="Google"]')))


@when('Confirmar a informação no campo de pesquisa')
def step_impl(browser):
    wait = WebDriverWait(browser, 10)
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    search_box.send_keys('Selenium')
    search_box.send_keys(Keys.RETURN)


@then('As informações relacionadas serão exibidas')
def step_impl(browser):
    wait = WebDriverWait(browser, 10)
    first_link = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
    first_link.click()
    wait.until(EC.title_contains('Selenium'))
