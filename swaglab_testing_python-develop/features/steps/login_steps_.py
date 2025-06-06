from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@given("el usuario navega a la página de SwagLabs")
def step_navegar_a_login(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://www.saucedemo.com/v1/index.html")

@when('el usuario ingresa el nombre de usuario "standard_user" y la contraseña "secret_sauce"')
def step_ingresar_credenciales(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()

@then("debería ser redirigido al inventario")
def step_verificar_inventario(context):
    WebDriverWait(context.driver, 5).until(EC.url_contains("v1/inventory.html"))
    assert "v1/inventory.html" in context.driver.current_url
    context.driver.quit()
