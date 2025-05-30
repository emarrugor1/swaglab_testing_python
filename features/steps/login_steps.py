from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import os
import tempfile

def take_screenshot(context, step_name):
    temp_dir = tempfile.gettempdir()
    screenshot_name = f"{step_name}.png"
    screenshot_path = os.path.join(temp_dir, screenshot_name)
    context.driver.save_screenshot(screenshot_path)
    with open(screenshot_path, "rb") as image_file:
        allure.attach(image_file.read(), name=step_name, attachment_type=allure.attachment_type.PNG)

@given('que estoy en la página de inicio de sesión de Swaglab')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/v1/')
    context.driver.maximize_window()
    take_screenshot(context, "pantalla_login")

@when('ingreso el usuario "{username}" y la contraseña "{password}"')
def step_impl(context, username, password):
    with allure.step('Ingresar usuario y contraseña'):
        context.driver.find_element(By.ID, 'user-name').send_keys(username)
        context.driver.find_element(By.ID, 'password').send_keys(password)
        take_screenshot(context, "usuario_y_contraseña_ingresados")

@when('hago clic en el botón de login')
def step_impl(context):
    with allure.step('Clic en el botón de login'):
        context.driver.find_element(By.ID, 'login-button').click()
        take_screenshot(context, "después_de_login")

@then('debo ver la página principal de productos')
def step_impl(context):
    with allure.step('Verificar página de productos'):
        take_screenshot(context, "pagina_principal_productos")
        assert 'inventory' in context.driver.current_url
    context.driver.quit()

