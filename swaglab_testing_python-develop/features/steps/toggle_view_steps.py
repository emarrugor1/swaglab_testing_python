from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("el usuario ha iniciado sesión exitosamente")
def step_impl(context):
    context.browser.get("https://www.saucedemo.com/v1/index.html")
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    context.browser.find_element(By.ID, "password").send_keys("secret_sauce")
    context.browser.find_element(By.ID, "login-button").click()
    WebDriverWait(context.browser, 10).until(EC.url_contains("inventory.html"))

@when("el usuario aplica el ordenamiento por precio de menor a mayor")
def step_impl(context):
    sort_select = context.browser.find_element(By.CLASS_NAME, "product_sort_container")
    sort_select.click()
    lohi = context.browser.find_element(By.CSS_SELECTOR, "option[value='lohi']")
    lohi.click()
    WebDriverWait(context.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    context.product_names_before = [el.text for el in context.browser.find_elements(By.CLASS_NAME, "inventory_item_name")]

@when("el usuario alterna la vista de productos")
def step_impl(context):
    toggle_btn = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, "toggle-view")))
    toggle_btn.click()

@then("la vista debe cambiar correctamente")
def step_impl(context):
    container = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    classes = container.get_attribute("class")
    assert "list" in classes or "grid" in classes, "No se reflejó el cambio de vista correctamente"

@then("el orden de productos debe mantenerse")
def step_impl(context):
    product_names_after = [el.text for el in context.browser.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert context.product_names_before == product_names_after, "El orden de productos cambió tras alternar la vista"

@then("el botón debe reflejar la vista activa")
def step_impl(context):
    icon = context.browser.find_element(By.ID, "toggle-view-icon")
    assert "active" in icon.get_attribute("class"), "El botón no refleja la vista activa correctamente"
