from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('el usuario navega a la página de SwagLabs')
def step_impl(context):
    context.browser.get("https://www.saucedemo.com/v1/index.html")

@given('el usuario ingresa el nombre de usuario "standard_user" y la contraseña "secret_sauce"')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    context.browser.find_element(By.ID, "password").send_keys("secret_sauce")
    context.browser.find_element(By.ID, "login-button").click()

@then('el ícono del carrito debe ser visible')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
    assert cart_icon.is_displayed()

@when('el usuario agrega "Sauce Labs Backpack" al carrito')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

@then('el contador del carrito debe mostrar "1"')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1"

@when('el usuario elimina "Sauce Labs Backpack" del carrito')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))).click()

@then('el carrito debe estar vacío')
def step_impl(context):
    # badge desaparece cuando no hay elementos
    assert len(context.browser.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
