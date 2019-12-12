# 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_path = "C:\\Users\\Aniket Pant\\OneDrive\\AniketCloud\\iNow_WebScraper_Project\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_path, options = chrome_options)
driver.get("https://sis-jeffersonco.chalkableinformationnow.com/InformationNow/Login.aspx")

# iNOW credentials
username = ""
password = ""
username_field = driver.find_element_by_xpath("""//*[@id="txtUsername"]""") # retrieve fields for inputs
password_field = driver.find_element_by_xpath("""//*[@id="txtPassword"]""")
username_field.send_keys(username) # send "keys" to respective fields
password_field.send_keys(password)
driver.find_element_by_xpath("""//*[@id="btnLogin"]""").click() # login to site

# Time to get grades
# First, navigate to the grades page
driver.find_element_by_xpath("""//*[@id="ctl00_navMenun6"]/td/table/tbody/tr/td/a""").click() # go to grades
all_classes = driver.find_elements_by_class_name("""gridRow""") # get grade for first class
for school_class in all_classes:
    print(school_class.text)
    print("__________________")