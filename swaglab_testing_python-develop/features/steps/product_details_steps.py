from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('el usuario hace clic en el producto "{producto}"')
def step_impl(context, producto):
    wait = WebDriverWait(context.driver, 10)
    links = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
    for link in links:
        if link.text == producto:
            link.click()
            return
    assert False, f"No se encontró el producto: {producto}"

@then('debería ver el nombre "{nombre}", precio "{precio}" y descripción "{descripcion}"')
def step_impl(context, nombre, precio, descripcion):
    wait = WebDriverWait(context.driver, 10)

    name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_name")))
    assert nombre in name.text, f"Nombre incorrecto: se esperaba '{nombre}', se obtuvo '{name.text}'"

    price = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_price")))
    assert precio in price.text, f"Precio incorrecto: se esperaba '{precio}', se obtuvo '{price.text}'"

    desc = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_details_desc")))
    assert descripcion in desc.text, f"Descripción incorrecta: se esperaba '{descripcion}', se obtuvo '{desc.text}'"

    img = context.driver.find_element(By.CLASS_NAME, "inventory_details_img")
    assert img.is_displayed(), "La imagen del producto no está visible"

    # Regresar a inventario
    wait.until(EC.element_to_be_clickable((By.ID, "back-to-products"))).click()
