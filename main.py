# Importing os for loading environment variables and getting full path of the driver
# Environment variables are those variables which are set during running the program to give details
# of the system
import os
# Dot env is a module which loads data written in .env file to the environment
import dotenv
# Importing the Chrome object which helps in automating with firefox
from selenium.webdriver import Chrome
# Importing datetime which helps us adding, subtracting and getting with date and times
from datetime import datetime
# Importing EC which helps us to check if a element is visible in the page
from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait helps us to wait until a certain element is present
from selenium.webdriver.support.ui import WebDriverWait
# The By object helps us to get elements By id, classname etc
from selenium.webdriver.common.by import By
# The sleep function waits for some second for next code to run
from time import sleep
# The keys helps to send different keys to the page
from selenium.webdriver.common.keys import Keys

# This loads all the data in .env file to environment variables
dotenv.load_dotenv()

# Setting variable for path of driver and url
PATH = os.path.join(os.getcwd(), 'Chromedriver')
URL = 'https://www.messenger.com'

# Getting email and password from .env
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Getting the user to whom we will send message
user = input("Enter the user id : ")

# Getting the message to send
message = input("Enter the message to send : ")

# Getting the time to send message and converting to time object
time = input('Enter the time (Y-m-d H:m:S): ')
time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

# Calculating the time left by subtracting the given time by the current
time_left = time - datetime.now()
time_left = time_left.total_seconds()

if time_left < 0:
    print("Invalid Time !!")
    exit()

print(f'\nWaiting for {time_left} seconds !\n')

# Waiting until the given time
sleep(time_left)

# Creating a chrome object with the driver path to automate with it
browser = Chrome(executable_path=PATH)

# Opening the messenger url
browser.get(URL)

sleep(5)
# Waiting until the element with id email appears and after it appears setting it to the variable
email_field = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'email'))
)

# Entering the email to the email field
email_field.send_keys(EMAIL)

# Waiting until the element with id pass appears and after it appears setting it to the variable
pass_field = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'pass'))
)

# Entering the password in password field
pass_field.send_keys(PASSWORD)

# Waiting until the login button appears
login_button = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'loginbutton'))
)

# Clicking in login button to login
login_button.click()

# Getting the link for user to message
message_link = URL + f"/t/{user}"

# Going to the user message page
browser.get(message_link)

sleep(5)
# Getting the input field to message
inputField = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role=textbox]'))
)

# Sending the message in message field
for msg in message:
    inputField.send_keys(msg)

# Sending enter to input field to send message
inputField.send_keys(Keys.ENTER)

print("Message sent sucessfully !")

# Closing the browser
#browser.close()