from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

browser = webdriver.Chrome(options=chrome_options)

print("title: ", browser.title)

timeout = 10

try:
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "TasksToolBar__title")))

    greetings = browser.find_element(By.CLASS_NAME, "TasksToolBar__title")
    greetings_text = greetings.get_attribute("innerHTML")
    print("=" * 50)
    print("logged in and got greetings")
    print(greetings_text)
    print("=" * 50)

    create_task = browser.find_element(By.CLASS_NAME, "AppHeaderNewTaskButton__button")
    create_task.click()

    print("clicked")

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "BackdropModal__modal")))

    print('visible now')


except Exception as e:
    print(e)
