try:
    from selenium import webdriver
    from tkinter import messagebox
    import time
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from bs4 import BeautifulSoup
    print("Loading...")
except Exception as e:
    print("Error : {} ".format(e))

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

"The Channel url you wanted send pm"
browser.get("")

timeout = 45

try:
    WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, 'app-mount')))
    print("Login page is ready!")

    "your discord username"
    username = ''
    UsernameElement = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input')
    UsernameElement.send_keys(username)

    "your discord password"
    password = ''
    PasswordElement = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input')
    PasswordElement.send_keys(password)

    LoginButton = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')

    time.sleep(1.5)
    LoginButton.click()

    WebDriverWait(browser, timeout).until(EC.presence_of_element_located((By.ID, 'app-mount')))
    print("Logged in")

    time.sleep(1.5)

    SearchForUsers = browser.find_elements(By.CLASS_NAME, "member-2gU6Ar")
    key = 0

    for item in SearchForUsers:
        try:
            Users = browser.find_elements(By.CLASS_NAME, "member-2gU6Ar")[key]
            print("Right clicking to user")
            userField = Users.find_element(By.TAG_NAME, 'div')
            userField.click()

            time.sleep(1.5)

            spamMessage = "Hi, I am a bot. I am here to help you. If you need any help, please contact me. Thank you. "

            "Sending a message"
            textArea = browser.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div/div[5]/div/input').send_keys(spamMessage + Keys.ENTER)

            time.sleep(3)
            browser.back()

        except NoSuchElementException:
            print("Message couldn't send")

        key = key + 1

    print("Done!")

except TimeoutException:
    print("Timeout error!")

time.sleep(5)
browser.quit()