from time import sleep
from typing import final

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from PIL import Image
import pytesseract


browser = webdriver.Chrome()
browser.get('https://www.typingtest.com/')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'__psm 7'
browser.find_element(By.CSS_SELECTOR, '#testStartForm > button').click()

sleep(3)
canv = browser.find_element(By.CSS_SELECTOR, '#test-container > canvas')

actions = ActionChains(browser)
def puter(lines):
    for letter in lines:
        if letter == " ":
            actions.send_keys(Keys.SPACE).perform()
        else:
            actions.send_keys(letter).perform()

    actions.send_keys(Keys.SPACE).perform()

while True:
    sleep(1)
    try:
        canv.screenshot('test.png')
    except StaleElementReferenceException :
        print("done")
        sleep(100)


    image = Image.open('test.png')
    width, height = image.size
    crop_box = (0,40, width, height // 4)
    cropped_image = image.crop(crop_box)

    text = pytesseract.image_to_string(cropped_image)
    lines = text.splitlines()
    puter(lines)
