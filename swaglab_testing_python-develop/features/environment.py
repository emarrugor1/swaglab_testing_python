import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def after_scenario(context, scenario):
    if scenario.status == "failed" and hasattr(context, "driver"):
        screenshot_name = f"screenshot_{scenario.name.replace(' ', '_')}.png"
        screenshot_path = os.path.join(os.getcwd(), screenshot_name)
        context.driver.save_screenshot(screenshot_path)
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def after_all(context):
    input("\n✅ Pruebas finalizadas. Presiona ENTER para cerrar el navegador...\n")
    context.browser.quit()