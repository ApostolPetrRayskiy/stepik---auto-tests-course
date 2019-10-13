from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_xpath('/html/body/div/form/div/div/div/h2/img[@valuex]')
x2 = x_element.get_attribute('valuex')
y = calc(x2)
option1 = browser.find_element_by_xpath('//input[@id="answer"]')
option1.send_keys(y)
option2 = browser.find_element_by_css_selector('[type="checkbox"]')
option2.click()
option3 = browser.find_element_by_css_selector('[value="robots"]')
option3.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()
time.sleep(10)
browser.quit()
