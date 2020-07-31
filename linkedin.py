import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

try:
    driver = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver.exe")

    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

    driver.find_element_by_id("username").send_keys(#usrname)
    driver.find_element_by_id ("password").send_keys(#password)
    driver.find_element_by_tag_name("button").click()

    driver.get("https://www.linkedin.com/in/maghil/edit/certification/new/")

    #wait until element is found
    driver.implicitly_wait(200)

    #certification name
    driver.find_element_by_id("certification-name").send_keys("Coursera")

    #certification issuer
    el=driver.find_element_by_xpath("//div[@class='pe-artdeco-typeahead search-basic-typeahead search-vertical-typeahead relative pe-artdeco-typeahead__stack-index--3 ember-view']//input")
    el.click()
    el.send_keys("test1")
    el.send_keys(Keys.ENTER)

    #certification will not expire checkbox
    driver.find_element_by_xpath("//div[@class='mb3']//label").click()

    #certification start date
    driver.find_element_by_xpath("//select[@id='certification-start-month']/option[text()='December']").click()
    driver.find_element_by_xpath("//select[@id='certification-start-year']/option[text()='2020']").click()

    #certification license number
    driver.find_element_by_id("certification-license-number").send_keys("test2")

    #certification url
    driver.find_element_by_id("certification-url").send_keys("test3")

    #certification save
    driver.find_element_by_class_name("pe-form-footer__action--submit artdeco-button form-submit-action t-14 t-white t-normal").click()

    time.sleep(5)

except Exception as e:
    print(e)

finally:
    print("closing browser")
    driver.close()
