from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

feature_file_path = os.path.abspath('Features/home.feature')

@scenario(feature_file_path, 'Verificar página home')
def test_publish():
    pass


@given('Que o navegador esteja aberto')
def step_impl(browser):
    # if browser is None or not isinstance(browser, webdriver.Chrome):
    #     raise Exception("O navegador não está aberto corretamente.")
    print("Navegador aberto")


@when('Acessar a página home da plataforma')
def step_impl(browser):
    browser.get('https://www.google.com/')


@then('Todos os recursos da página serão carregados')
def step_impl(browser):
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, 'q')))
    browser.find_element(By.NAME, 'q')
