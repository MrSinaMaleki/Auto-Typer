from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


# chrome_options = Options()
# chrome_options.add_argument("--headless")

browser = webdriver.Chrome()
browser.get('https://monkeytype.com/')
browser.find_element(By.CSS_SELECTOR, '#cookiesModal > div.modal > div.main > div.buttons > button.active.acceptAll').click()


actions = ActionChains(browser)
def puter():


    try:
        # active_words = 0 if not(browser.find_elements(By.CSS_SELECTOR, '#words > div.word.typed')) else len(browser.find_elements(By.CSS_SELECTOR, '#words > div.word.typed'))
        # print(active_words)
        #
        # word_elements = browser.find_elements(By.CSS_SELECTOR, '#words > div.word ')[active_words:]
        # words = []
        # for word_element in word_elements:
        #     letter_elements = word_element.find_elements(By.TAG_NAME, 'letter')
        #     word = "".join(letter.get_attribute("innerHTML") for letter in letter_elements)
        #     words.append(word)
        # words += " "
        #
        #
        # key_sequence = " ".join(words)
        # # print(key_sequence)
        # actions.send_keys(key_sequence).perform()

        key_sequence = browser.execute_script("""
                    // Count already typed words
                    const typedCount = document.querySelectorAll('#words > div.word.typed').length;
                    // Get remaining word elements
                    const wordElements = Array.from(document.querySelectorAll('#words > div.word')).slice(typedCount);
                    // Build the key sequence by joining innerHTML of <letter> tags from each word
                    const words = wordElements.map(word => {
                        return Array.from(word.getElementsByTagName('letter'))
                                    .map(letter => letter.innerHTML)
                                    .join('');
                    });
                    return words.join(' ');
                """)

        actions.send_keys(key_sequence).perform()
        print(key_sequence)
        if len(key_sequence) < 1:
            raise StaleElementReferenceException()
        # +800 WPM (HAHAHA)

    except StaleElementReferenceException:
        sleep(1)
        wpm = browser.find_element(By.CSS_SELECTOR, '#result > div.wrapper > div:nth-child(1) > div.group.wpm > div.bottom')
        print("WPM:",wpm.get_attribute("innerHTML"))
        sleep(100)

    # while True:
    #     try:
    #         one_word_element = browser.find_elements(By.CSS_SELECTOR, '#words > div.word.active')
    #
    #         final_word = ""
    #         for letter_element in one_word_element:
    #             letters = letter_element.find_elements(By.TAG_NAME, 'letter')
    #             for letter in letters:
    #                 final_word += letter.get_attribute("innerHTML")
    #
    #         # print(final_word)
    #
    #         # for char in final_word:
    #         #     if char == " ":
    #         #         actions.send_keys(Keys.SPACE).perform()
    #         #     else:
    #         #         actions.send_keys(char).perform()
    #         actions.send_keys(final_word).perform()
    #         actions.send_keys(Keys.SPACE).perform()
    #
    #         if len(final_word) < 1:
    #             raise StaleElementReferenceException
    #
    #     except StaleElementReferenceException:
    #         sleep(1)
    #         wpm = browser.find_element(By.CSS_SELECTOR, '#result > div.wrapper > div:nth-child(1) > div.group.wpm > div.bottom')
    #         print("WPM:",wpm.get_attribute("innerHTML"))
    #         sleep(100)


while True:
    puter()


