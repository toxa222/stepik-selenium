import os
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "sel_file.txt"
file_path = os.path.join(current_dir, file_name)
try:
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.implicitly_wait(5)
    # print(browser.window_handles)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
    btn = browser.find_element_by_id('book')
    btn.click()

    # alr = browser.switch_to.alert
    # alr.accept()
    #
    time.sleep(2)
    inpx = browser.find_element_by_css_selector('#input_value')
    x = calc(int(inpx.text))
    ans = browser.find_element_by_css_selector('#answer')
    ans.send_keys(str(x))
    btn2 = browser.find_element_by_css_selector('[type=submit]')
    btn2.click()
    #
    res = browser.switch_to.alert
    otvet = res.text.split()[-1]
    pyperclip.copy(otvet)

    # time.sleep(2)
    # browser.execute_script("prompt('Hello world!');")
    # time.sleep(2)
    # alert = browser.switch_to.alert
    # time.sleep(2)
    # alert.send_keys("my answer!")
    #
    # time.sleep(2)
    # alert.accept()


    # lst = browser.find_element_by_css_selector('#dropdown')
    # sl = Select(lst)
    # sl.select_by_visible_text()

    # robot = browser.find_element_by_css_selector('#robotsRule')
    # print(robot.get_attribute('checked'))
    #
    # robot.click()
    # print(robot.get_attribute('checked'))
    #
    # robotcheck = browser.find_element_by_css_selector('#robotCheckbox')
    # print('req', robotcheck.get_attribute('required'))
    # print('checked',robotcheck.get_attribute('checked'))
    #
    #
    # print(robotcheck.get_attribute('id'))
    # robotcheck.click()
    # print('checked',robotcheck.get_attribute('checked'))


    # x1 = browser.find_element_by_css_selector('#input_value')
    # res = calc(x1.text)
    # print(res)
    #
    # sel = Select(browser.find_element_by_css_selector('#dropdown'))
    # sel.select_by_visible_text(str(res))

    # answ = browser.find_element_by_css_selector('#answer')
    # answ.send_keys(res)

    # rdb1 = browser.find_element_by_css_selector('#robotsRule')
    # rdb1.click()
    # chkd1 = browser.find_element_by_css_selector('#robotCheckbox')
    # chkd1.click()


    # elements = browser.find_elements_by_css_selector('input[required]')
    # for elem in elements:
    #     elem.send_keys('My answer')
    # inp1 = browser.find_element_by_css_selector('[name=firstname]')
    # inp1.send_keys('Name')
    # inp2 = browser.find_element_by_css_selector('[name=lastname]')
    # inp2.send_keys('LastName')
    # inp3 = browser.find_element_by_css_selector('[name=email]')
    # inp3.send_keys('Email')
    #
    # inpf = browser.find_element_by_css_selector('#file')
    # inpf.send_keys(file_path)
    # btn = browser.find_element_by_tag_name('button')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    # btn.click()
    # res = browser.find_element_by_tag_name('h1')
    # assert 'Congratulations! You have successfully registered!' == res.text
finally:
    time.sleep(5)
    browser.quit()
