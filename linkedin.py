import time
import helper as h
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



def executor():
    try:
        u=h.userData()
        user=u['linkedIn']
        c= h.certificate()
        certificate =c["cert1"]

        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        #login page
        driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

        driver.find_element_by_id("username").send_keys(user["user"])
        driver.find_element_by_id ("password").send_keys(user["pwd"])
        driver.find_element_by_tag_name("button").click()

        #API to add new certificate
        driver.get("https://www.linkedin.com/profile/add?startTask=CERTIFICATION_NAME&name="+certificate["name"]+"&organizationName="+certificate["org"]+"&issueYear="+str(certificate["issueYear"])+"&issueMonth="+str(certificate["issueMonth"])+"&expirationYear="+str(certificate["expireYear"])+"&expirationMonth="+str(certificate["expireMonth"])+"&certUrl="+certificate["lUrl"]+"&certId="+str(certificate["lNumber"]))

        time.sleep(5)
        #certification will not expire checkbox
        driver.find_element_by_xpath("//div[@class='mb3']//label").click()

        time.sleep(5)

        #certification save button
        driver.find_element_by_class_name("pe-form-footer__action--submit artdeco-button form-submit-action t-14 t-white t-normal").click()
        return(1)

    except TimeoutError:
        print(e)
        print("closing browser")  
        driver.close()
        return(0)
              
if __name__ == "__main__":
    executor()
