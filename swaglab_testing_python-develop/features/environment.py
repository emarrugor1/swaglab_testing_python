import allure
import os

def after_scenario(context, scenario):
    if scenario.status == "failed" and hasattr(context, "driver"):
        screenshot_name = f"screenshot_{scenario.name.replace(' ', '_')}.png"
        screenshot_path = os.path.join(os.getcwd(), screenshot_name)
        context.driver.save_screenshot(screenshot_path)
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
