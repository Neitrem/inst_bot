import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from db_manager import get_person, change_value
from mail import get_code
from set_up import set_up
import string
import random


def r_sleep_(type):
    if(type == 'fast'):
        time.sleep(random.randint(50, 100)/100)
    elif(type == 'medium'):
        time.sleep(random.randint(5, 10))
    elif(type == 'big'):
        time.sleep(random.randint(30, 40))


def inst_acc_reg(current_person):
    if(current_person['is_inst_created'] != '1'):



        r_sleep_('fast')
        # insert email
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.NAME, 'emailOrPhone'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.NAME, 'emailOrPhone'))).send_keys(current_person['email'])
        r_sleep_('fast')
        # insert fullname
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.NAME, 'fullName'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.NAME, 'fullName'))).send_keys(current_person['first_name'] + ' ' + current_person['last_name'])
        r_sleep_('fast')
        # insert username
        while True:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.NAME, 'username'))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.NAME, 'username'))).send_keys(current_person['login_inst'].lower())

            r_sleep_('fast')

            try:
                driver.find_element_by_class_name('coreSpriteInputError')
            except Exception:
                break
            else:
                current_person['login_inst'] = current_person['first_name'] + '_' + \
                                               current_person['last_name'] + \
                                               ''.join(random.choice(string.hexdigits) for i in range(5))

                change_value('login_inst', current_person['login_inst'], current_person['id'])

                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.NAME, 'username'))).clear()
        r_sleep_('fast')
        # insert password
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.NAME, 'password'))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.NAME, 'password'))).send_keys(current_person['password'])
        r_sleep_('fast')
        # submit

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

        r_sleep_('medium')
        # birthday verification
        # month
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
            "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
            f"//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[3]"))).click()

        # day
        r_sleep_('fast')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
            "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
            f"//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[2]"))).click()

        # year
        r_sleep_('fast')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
            "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
            f"//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

        # submit
        r_sleep_('fast')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
            "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()

        r_sleep_('medium')

        inst_code, response = get_code(current_person['email'], current_person['password'])

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.NAME, 'email_confirmation_code'))).send_keys(inst_code)

        r_sleep_('fast')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
            "//*[@id='react-root']/section/main/div/div/div[1]/div[2]/form/div/div[2]"))).click()


if __name__ == "__main__":

    # test values
    person = get_person(3)

    url = 'https://www.instagram.com/accounts/emailsignup/'

    driver = set_up(person, url)

    inst_acc_reg(person)

    time.sleep(100000)
