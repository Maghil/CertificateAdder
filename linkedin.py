import time
import yaml
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

with open(r'linkedIn.yml') as file:
    user = yaml.full_load(file)

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    #login page
    driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

    driver.find_element_by_id("username").send_keys(user["email"])
    driver.find_element_by_id ("password").send_keys(user["pwd"])
    driver.find_element_by_tag_name("button").click()

    #API to add new certificate
    driver.get("https://www.linkedin.com/profile/add?startTask=CERTIFICATION_NAME&name=test1&organizationName=Coursera&issueYear=2018&issueMonth=2&expirationYear=2020&expirationMonth=5&certUrl=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Flearn%2Fcertifications%2Fd365-functional-consultant-sales&certId=1234")

    time.sleep(5)
    #certification will not expire checkbox
    driver.find_element_by_xpath("//div[@class='mb3']//label").click()

    time.sleep(5)

    #certification save button
    driver.find_element_by_class_name("pe-form-footer__action--submit artdeco-button form-submit-action t-14 t-white t-normal").click()

    

except Exception as e:
    print(e)

finally:
    print("closing browser")
    driver.close()
