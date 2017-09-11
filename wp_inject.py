from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from random import randint

town1 = "White Plains"
town2 = "Portchester"
zip1 = "10605"
phone = "(555) 555-5555"
name = "Dr. John Smith"
occupation = "Dentist"

chrome_path = "xxx"
url = "xxx"

get_number = [1, 2, 3]
delay = 5

page_names = []
title_data = []
desc_data = []

driver = webdriver.Chrome(chrome_path)
driver.get(url + '/wp-login.php')

username = "xxx"
password = "xxx"
pages_path = "edit.php?post_type=page"

user_login = driver.find_element_by_id("user_login")
user_pass = driver.find_element_by_id("user_pass")

user_login.send_keys(username)
user_pass.send_keys(password)

driver.find_element_by_id("wp-submit").click()

driver.find_element_by_xpath('//a[@href="'+ pages_path +'"]').click()

get_page_names = driver.find_elements_by_class_name("post_title")
for i in get_page_names:
    page_names.append(i.get_attribute('innerHTML'))

get_magic_numbers = driver.find_elements_by_class_name("aioseop_edit_link")
for i in get_magic_numbers:
    grabbed = i.get_attribute('id')
    if "title" in grabbed:
        title_data.append(grabbed)
    if "desc" in grabbed:
        desc_data.append(grabbed)

titles = dict(zip(page_names, title_data))
for a, b in titles.items():
    title_generator = randint(0, len(get_number) - 1)
    magic_number =  (re.findall('\d+', b))[0]
    driver.find_element_by_id(b).send_keys('\n')
    top_title = driver.find_element_by_id("aioseop_new_title_" + magic_number)
    if a == "Home":
        c = occupation
    elif a == "Contact":
        c = "Contact " + occupation  
    else:
        c = a
    if title_generator == 1:
        title_inject = c + " in " + town1 + " | " + town1 + " " + c + " | " + c + " in " + town2
    elif title_generator == 2:
        title_inject = town2 + " " + c + " | " + c + " in " + town1 + " | " + c + " " + zip1
    else:
        title_inject = c + " in " + town2 + " | " + town2 + " " + c + " | " + c + " " + town1
    top_title.clear()
    top_title.send_keys(title_inject)
    driver.find_element_by_id("aioseop_title_save_" + magic_number).click()

descs = dict(zip(page_names, desc_data))
for a, b in descs.items():
    title_generator = randint(0, len(get_number) - 1)
    magic_number =  (re.findall('\d+', b))[0]
    driver.find_element_by_id(b).send_keys('\n')
    desc_title = driver.find_element_by_id("aioseop_new_description_" + magic_number)
    if a == "Home":
        c = "a " + occupation.lower()
    elif a == "Contact":
        c = "a " + occupation.lower() 
    else:
        c = a.lower()
    if title_generator == 1:
        desc_inject = "If you need  " + c +  " in " + town2 + ', then call ' + name + ' today at ' + phone + "."
    elif title_generator == 2:
        desc_inject = "For " + c + " in " + town1 + ",call " + phone + " today for an appointment with " + name + "."
    else:
        desc_inject = "Call " + name + " today at " + phone + " if you need " + c + " in " + town2 + "."
    desc_title.clear()
    desc_title.send_keys(desc_inject)
    driver.find_element_by_id("aioseop_description_save_" + magic_number).click()


