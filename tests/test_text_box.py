from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_text_box_displays_submitted_name_and_email(browser):
    name = "Andrey Tester"
    email = "andrey@example.com"
    browser.get("https://demoqa.com/text-box")
    wait = WebDriverWait(browser, 10)

    name_field = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
    name_field.send_keys(name)
    browser.find_element(By.ID, "userEmail").send_keys(email)

    submit = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit)
    submit.click()

    result_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#output #name")))
    assert result_name.text == f"Name:{name}"
    assert browser.find_element(By.CSS_SELECTOR, "#output #email").text == f"Email:{email}"
