from v40_settings import SettingBrowserClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Data.data import user_setting_dict
import time
import random
import pickle
import os


class StartLoginQuit(SettingBrowserClass):

    def __init__(self, count):
        super().__init__(count)
        self.username = user_setting_dict[f'profile{self.count}']['login']
        self.password = user_setting_dict[f'profile{self.count}']['password']
        self.browser = self.setting_browser_bot()

    def login(self):  # Авторизация
        try:
            browser = self.browser
            browser.get('https://www.reddit.com/login/')
            time.sleep(user_setting_dict[f'profile{self.count}']['randomtime_start'])

            username_input = browser.find_element(By.NAME, 'username')
            username_input.clear()
            username_input.send_keys(self.username)

            time.sleep(random.randrange(2, 10))

            password_input = browser.find_element(By.NAME, 'password')
            password_input.clear()
            password_input.send_keys(self.password)

            time.sleep(random.randrange(1, 5))

            password_input.send_keys(Keys.ENTER)
            time.sleep(random.randrange(3, 7))
            time.sleep(10)

            # Создание файла куки
            with open(f"/home/ivan/PycharmProjects/Reddit_Up_Vote_v1/Cookie/{self.username}_cookies", "wb") as f:
                pickle.dump(browser.get_cookies(), f)

            print(f'Account{self.count}: [+] Вошел успешно (Залогинился)')

        except Exception as e:
            print(f'Account{self.count}: [-] Не получилось залогиниться')
            print(f'Account{self.count}: {e}')
            self.close_browser()

    def close_browser(self):
        try:
            with open(f"//home/ivan/PycharmProjects/Reddit_Up_Vote_v1/Cookie/{self.username}_cookies", "ab") as f:
                pickle.dump(self.browser.get_cookies(), f)
            self.browser.close()
            self.browser.quit()
            print(f'Account{self.count}: [+] Браузер закрыт успешно! Увидимся) ')
        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось закрыть браузер')
            print(f'Account{self.count}: {e}')

    def start_browser(self):
        file_cookie = os.path.isfile(f'/home/ivan/PycharmProjects/Reddit_Up_Vote_v1/Cookie/{self.username}_cookies')
        browser = self.browser

        if file_cookie:
            try:
                browser.get('https://www.reddit.com/login/')
                # Проверяем, есть ли куки и загружаем их.
                with open(f"/home/ivan/PycharmProjects/Reddit_Up_Vote_v1/Cookie/{self.username}_cookies", "rb") as f:
                    cookies = pickle.load(f)
                    for cookie in cookies:
                        browser.add_cookie(cookie)
                browser.refresh()
                time.sleep(user_setting_dict[f'profile{self.count}']['randomtime_start'])
                print(f'Account{self.count}: [+] Печеньки найдены и загружены')
            except Exception as e:
                print(f'Account{self.count}: [-] Не удалось загрузить печеньки')
                print(f'Account{self.count}: {e}')
                self.close_browser()

        if not file_cookie:
            self.login()

0
