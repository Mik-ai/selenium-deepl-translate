from config import driver
from selenium.webdriver.common.by import By
import time

element_translate_from = driver.find_element(
    By.XPATH,
    """
//*[@aria-placeholder='Введите текст для перевода.
Перетащите файл PDF, Word (.docx) или PowerPoint (.pptx) в это поле, чтобы перевести его с помощью нашего переводчика документов.
Чтобы перевести речь, нажмите на микрофон.']
                              """,
)

def translate_text(text:str):
    element_translate_from.click()
    time.sleep(0.1)
    element_translate_from.send_keys(text)
    time.sleep(0.4)
    text = driver.find_element(By.XPATH,"//d-textarea[@name='target']").text
    driver.find_element(By.XPATH,"//button[@aria-label='Удалить исходный текст']").click()
    return text
