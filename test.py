from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime
import re

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("https://app.cloudqa.io/home/AutomationPracticeForm")

# Testing for Date of Birth field.
# Date of Birth field has the id of dob.
dob = browser.find_element(By.ID, "dob")

date_format = '%Y-%m-%d'

try:
   dateObject = datetime.datetime.strptime(dob, date_format)
   print(dateObject)

except ValueError:
   print("Incorrect data format, should be YYYY-MM-DD")

email = browser.find_element(By.ID, "email")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

if(re.fullmatch(regex, email)):
    print("${email} is a valid Email")

else:
    print("${email} is a invalid Email")

mobile = browser.find_element(By.ID, "mobile")

# with 91 or 0
pattern = re.compile("(0|91)?[6-9][0-9]{9}")

# normal Number with 10 digits
pattern = re.compile(r'^\d{10}$')

if pattern.match(mobile):
    print(f"{mobile} is a valid mobile number")
else:
    print(f"{mobile} is an invalid mobile number")
	
browser.quit()