from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def get_product_names(context):
    elements = context.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    return [el.text for el in elements]

def get_product_prices(context):
    elements = context.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    return [float(el.text.replace("$", "")) for el in elements]

@then("los productos deben estar ordenados alfabéticamente de la A a la Z")
def step_orden_az(context):
    time.sleep(1)
    names = get_product_names(context)
    assert names == sorted(names), "❌ El orden A-Z no es correcto"

@then("los productos deben estar ordenados alfabéticamente de la Z a la A")
def step_orden_za(context):
    Select(context.driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("za")
    time.sleep(1)
    names = get_product_names(context)
    assert names == sorted(names, reverse=True), "❌ El orden Z-A no es correcto"

@then("los productos deben estar ordenados por precio de menor a mayor")
def step_orden_precio_menor_mayor(context):
    Select(context.driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")
    time.sleep(1)
    prices = get_product_prices(context)
    assert prices == sorted(prices), "❌ El orden por precio menor a mayor no es correcto"

@then("los productos deben estar ordenados por precio de mayor a menor")
def step_orden_precio_mayor_menor(context):
    Select(context.driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("hilo")
    time.sleep(1)
    prices = get_product_prices(context)
    assert prices == sorted(prices, reverse=True), "❌ El orden por precio mayor a menor no es correcto"
    context.driver.quit()
