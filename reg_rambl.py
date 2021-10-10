import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from db_manager import set_person, create_table
from generate_person import create_person
from set_up import set_up


def r_sleep_(type):
    if(type == 'fast'):
        time.sleep(random.randint(50, 100)/100)
    elif(type == 'medium'):
        time.sleep(random.randint(5, 10))
    elif(type == 'big'):
        time.sleep(random.randint(25, 35))


def email_reg(current_person, current_driver):
    r_sleep_('fast')
    # login
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'login'))).send_keys(current_person['login'])
    r_sleep_('fast')
    # Password
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'newPassword'))).send_keys(current_person['password'])
    r_sleep_('fast')
    # Confirm password
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'confirmPassword'))).send_keys(current_person['password'])
    r_sleep_('fast')
    # Hint question
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'question'))).click()
    r_sleep_('fast')
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'rui-RelativeOverlay-content'))).click()
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'answer'))).send_keys(current_person['last_name'])

    # enter captcha
    r_sleep_('big')

    # Confirm
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'rui-Button-button'))).click()

    r_sleep_('medium')

    # firstname
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'firstname'))).send_keys(current_person['first_name'])
    r_sleep_('fast')
    # lastname
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'lastname'))).send_keys(current_person['last_name'])
    r_sleep_('fast')
    # Select gender(only female is possible))
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'gender'))).click()
    r_sleep_('fast')
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'rui-RelativeOverlay-content'))).click()
    r_sleep_('fast')
    # select day
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'birthday'))).click()
    r_sleep_('fast')
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'rui-RelativeOverlay-content'))).click()
    r_sleep_('fast')
    # select month
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div/div[1]/div/article/form/section[4]/div/div/div/div[2]'))).click()
    r_sleep_('fast')
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'rui-RelativeOverlay-content'))).click()
    r_sleep_('fast')
    # select year
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div/div[1]/div/article/form/section[4]/div/div/div/div[3]'))).click()
    r_sleep_('fast')
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'rui-RelativeOverlay-content'))).click()
    r_sleep_('fast')
    # Select city
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.ID, 'geoid'))).send_keys('Budapest')
    # confirm
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'rui-Button-type-primary'))).click()

    r_sleep_('big')

    # Activate IMAP protocol
    current_driver.get('https://mail.rambler.ru/settings/mailapps')
    r_sleep_('fast')
    # select yes button
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="MailApps-toggle-3E"]/div/button[1]'))).click()

    # Enter captcha
    r_sleep_('big')

    # submit
    WebDriverWait(current_driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@class="MailAppsChange-submitWrapper-JZ"]/button'))).click()


    return current_person


if __name__ == "__main__":
    create_table()

    person = create_person('rambler.ru', 'some proxy')

    url = 'https://id.rambler.ru/login-20/mail-registration'

    driver = set_up(person, url)

    person_info = email_reg(person, driver)

    set_person(person_info)

    time.sleep(10)
