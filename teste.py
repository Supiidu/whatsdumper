from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Configuration for chrome options
chrome_options = Options()
chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Path to chrome executable

# Use webdriver-manager to automatically manage ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
input("Scan the QR code and press Enter")

# List of numbers to send the message (in international format)
numbers = []

# Loop to allow multiple number entries
while True:
    user_input = input("Enter a phone number e.g., +5512345678900 (or 'exit' to finish): ")

    # Check if the user typed 'exit' to break the loop
    if user_input.lower() == 'exit':
        break
    
    # Add the entered number to the list
    numbers.append(user_input.strip())

# Message to be sent
message = input("Enter the message: ")

for number in numbers:
    # Access the link to open the conversation on WhatsApp Web
    url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
    driver.get(url)
    sleep(10)  # Wait for the page to load

    # Click the send button
    send_button = driver.find_element('xpath', '//span[@data-icon="send"]')
    send_button.click()
    sleep(2)  # Wait for the message to be sent

# Close the browser at the end
driver.quit()

print("Finished")
