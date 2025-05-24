'''
BumBot 1.0
Authors: David Santos, Matthew Evangelista
'''

import undetected_chromedriver as uc
import json
import time
from selenium.webdriver.common.by import By
from openai import OpenAI
import sys
import io

# Used to read emojis
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Replace INSERT key with your own OpenAI API Key.
client = OpenAI(api_key="INSERT")

# Load Login Cookies
with open('samplesite_cookies.json', 'r') as f:
    cookies = json.load(f)
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
# Load the base website and insert the login cookies 
driver.get("https://samplesite.com")
for cookie in cookies:
    cookie.pop('sameSite', None)
    driver.add_cookie(cookie)

# Open actual WebApp
driver.get("https://samplesite.com/app")
time.sleep(3)
elements = driver.find_elements(By.CLASS_NAME, "contact")
contacts_data = []

for person in elements:
    lines = person.text.split('\n')
    contacts_data.append(lines)

# Index for chats where the last message is from the match
filtered_data = []

for i in contacts_data:
    if i.count("Unread Message") > 0 :
        filtered_data.append(1)
    else: 
        filtered_data.append(0)

chat = driver.find_elements(By.CLASS_NAME, "contact")
chatCounter = 0
for i in chat:
    if filtered_data[chatCounter] == 1:
        i.click()
    
    time.sleep(1)
    chatCounter += 1

with open("input.txt", "r", encoding="utf-8") as file:
    system_text = file.read()

chatCounter = 0
output = []

for i in contacts_data:
        if filtered_data[chatCounter] == 1:
            prevMsg = str(i[2])
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # or another model like gpt-4, gpt-3.5-turbo
                messages=[
                    {"role": "system", "content": "You are going to realistically simulate a conversation in a dating app. You type in lower caps." + system_text},
                    {"role": "user", "content": "Previous Message: " + prevMsg}
                ]
            )
            
            output.append((str(i[0]) + ": " + (response.choices[0].message.content) + "\n"))
        
        chatCounter += 1

with open("output.txt", "w", encoding='utf-8') as f:
    for i in output:
        f.write(i)
    
driver.quit()
