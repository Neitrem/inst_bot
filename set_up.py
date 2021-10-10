from seleniumwire import webdriver


def set_up(new_person, url):



    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument(f'--proxy-server={new_person["proxy"]}')

    chrome_options.add_argument(f'user-agent={new_person["ua"]}')

    chrome_options.add_argument('window-size=1200x600')

    new_driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=r"Path to the chromedriver.exe")

    new_driver.get(url)

    return new_driver
