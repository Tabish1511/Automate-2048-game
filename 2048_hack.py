from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://play2048.co/')

elem = browser.find_element(By.XPATH, "//div[@class='score-container']")

'''print(elem.text)
print(type(elem.text))'''


htmlElem = browser.find_element(By.TAG_NAME, "html")

while elem.text != '2048' or elem.text < '2048':
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    elem = browser.find_element(By.XPATH, "//div[@class='score-container']")


print('Congrats! Your score is ' + elem.text)


browser.quit()


# Program ends here
