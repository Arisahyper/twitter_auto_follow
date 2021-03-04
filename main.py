import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys

url = "https://twitter.com/home"


def connect(url, driver):
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)


def login(id, pas, driver):
    id_box = driver.find_element_by_name("session[username_or_email]")
    pass_box = driver.find_element_by_name("session[password]")
    id_box.send_keys(id)
    pass_box.send_keys(pas)
    id_box.submit()

    time.sleep(2)


def search(word, driver):
    search_box = driver.find_element_by_xpath(
        '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')

    search_box.send_keys(word)
    search_box.send_keys(keys.ENTER)

    time.sleep(2)


def target(driver):
    target_button = driver.find_element_by_xpath(
        '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a')
    target_button.click()

    time.sleep(2)


def follow(driver):
    for i in range(1, 11):
        driver.find_elements_by_xpath(
            f"/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[ {i} ]/div/div/div/div[2]/div[1]/div[2]/div")[0].click()
        time.sleep(1)


def main():
    id = input("user-id >> ")
    pas = getpass.getpass("pass >> ")
    word = input("word >> ")
    print("Please wait...")

    driver = webdriver.Chrome()

    connect(url, driver)
    login(id, pas, driver)
    search(word, driver)
    target(driver)
    follow(driver)

    driver.quit()


if __name__ == "__main__":
    main()
