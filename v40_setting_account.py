from v40_start import StartLoginQuit
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pickle
import random


class SettingAccount(StartLoginQuit):

    def __init__(self, count):
        super().__init__(count)
        self.actions = ActionChains(self.browser)

        # Элементы Реддит
        # Старт меню с выбором сабов
        self.btn_back_start_menu = '_1tj26oBtwO7xtDQfIgqLJ3'  # class
        self.btn_skip_start_menu = '_22ChQI9alXTuxk7yqwRt8l'  # class
        self.btn_continue_start_menu = 'dK60vCQAai2JPR7mVZ4ir'  # class
        self.btn_randomize = '_2Q_2oitWh5modqGvZBePJC _2iuoyPiKHN3kfOoeIQalDT _2tU8R9NTqhvBrhoNAXWWcP HNozj_dKjQZ59ZsfEegz8 _1tPpYVD73ugqp4k-VMFRki'  # class

        # Элементы стартовой страницы
        self.elements_reddit_for_random = {
            'back_to_top': '//*[@id="AppRouter-main-content"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/button',
            'search_reddit': '/html/body/div[1]/div/div[2]/div[1]/header/div/div[1]/div[3]/div/form/input',
            'btn_home': '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button',
            'btn_feed': '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/a',
        }
        # Элементы страницы настроек аккаунта
        self.btn_setting_sex = '//*[@id="AppRouter-main-content"]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/button'  # class
        self.elements_sex_for_random = {
            'btn_man': '/html/body/div[5]/div/button[2]',  # class
            'btn_women': '/html/body/div[5]/div/button[1]',  # class
            'btn_non_binary': '/html/body/div[5]/div/button[3]'  # class
        }
        self.profile_in_setting = '//*[@id="AppRouter-main-content"]/div/div[1]/div/a[2]'  # class
        self.feed_setting = '//*[@id="AppRouter-main-content"]/div/div[1]/div/a[4]'  # class
        self.btn_confirm_NSFW = '#SHORTCUT_FOCUSABLE_DIV > div:nth-child(7) > div > div > div > div > div > button.Ch-0dFLxLOtcc6xCyQvsk._2iuoyPiKHN3kfOoeIQalDT._10BQ7pjWbeYP63SAPNS8Ts.HNozj_dKjQZ59ZsfEegz8'
        self.btn_safe_search = '#AppRouter-main-content > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div > div > div:nth-child(1) > div._21H_PIzpqfpibB_EcUDwpj > div._1nT46ChOZ3tgGqgs2CyMeJ > div'

        # НЕ стабильные элементы
        self.switch_nsfw = '#AppRouter-main-content > div > div._1OrNGmpfcSuSebbZM5vYq4 > div._3FVpvZ7OLbS_68QzaxplxT > div:nth-child(9) > div._1oREjd5ToMFah-VfX5Zt1z'  # class
        self.switch_adult_cont = '#AppRouter-main-content > div > div._1OrNGmpfcSuSebbZM5vYq4 > div._3FVpvZ7OLbS_68QzaxplxT > div:nth-child(3) > div._1oREjd5ToMFah-VfX5Zt1z'  # xpath
        self.switch_safe_browsing = '#AppRouter-main-content > div > div._1OrNGmpfcSuSebbZM5vYq4 > div._3FVpvZ7OLbS_68QzaxplxT > div:nth-child(4) > div._1oREjd5ToMFah-VfX5Zt1z'   # xpath

    @staticmethod
    def random_time_for_send_keys():
        return time.sleep(random.randint(300, 800) / 1000)

    @staticmethod
    def random_time_sleep_fast():
        return time.sleep(random.randint(2, 9))

    @staticmethod
    def random_time_sleep_large():
        return time.sleep(random.randint(10, 19))

    @staticmethod
    def random_time_sleep_big():
        return time.sleep(random.randint(20, 30))

    def click_xpath(self, element_on_page):
        try:
            element = self.browser.find_element(By.XPATH, element_on_page)
            self.actions.move_to_element(element).click().perform()
        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось кликнуть по XPATH')
            # print(f'Account{self.count}: {e}')

    def click_id(self, element_on_page):
        try:
            element = self.browser.find_element(By.ID, element_on_page)
            self.actions.move_to_element(element).click().perform()
        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось кликнуть по ID')
            # print(f'Account{self.count}: {e}')

    def click_class(self, element_on_page):
        try:
            element = self.browser.find_element(By.CLASS_NAME, element_on_page)
            self.actions.move_to_element(element).click().perform()
        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось кликнуть по CLASS')
            # print(f'Account{self.count}: {e}')

    def click_css(self, element_on_page):
        try:
            element = self.browser.find_element(By.CSS_SELECTOR, element_on_page)
            self.actions.move_to_element(element).click().perform()
        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось кликнуть по CSS')
            # print(f'Account{self.count}: {e}')

    def click_partial_text(self, element_on_page):
        try:
            element = self.browser.find_element(By.PARTIAL_LINK_TEXT, element_on_page)
            self.actions.move_to_element(element).click().perform()
        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось кликнуть по PARTIAL_TEXT')
            # print(f'Account{self.count}: {e}')

    def click_text(self, element_on_page):
        try:
            element = self.browser.find_element(By.LINK_TEXT, element_on_page)
            self.actions.move_to_element(element).click().perform()
        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось кликнуть по TEXT')
            # print(f'Account{self.count}: {e}')

    def click_name(self, element_on_page):
        try:
            element = self.browser.find_element(By.NAME, element_on_page)
            self.actions.move_to_element(element).click().perform()
        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось кликнуть по NAME')
            # print(f'Account{self.count}: {e}')

    def move_to(self, element_page):
        try:
            element = self.browser.find_element(By.XPATH, element_page)
            width = element.size['width']
            height = element.size['height']
            x_offset = random.randint(0, width)
            y_offset = random.randint(0, height)

            self.actions.move_by_offset(x_offset, y_offset)
            self.actions.perform()
            time.sleep(random.randint(1, 5))

            self.actions.move_to_element(element).perform()
            time.sleep(random.randint(1, 5))

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось навести на XPATH')
            # print(f'Account{self.count}: {e}')

    def move_to_text(self, element_page):
        try:
            element = self.browser.find_element(By.LINK_TEXT, element_page)
            width = element.size['width']
            height = element.size['height']
            x_offset = random.randint(0, width)
            y_offset = random.randint(0, height)

            self.actions.move_by_offset(x_offset, y_offset)
            self.actions.perform()
            time.sleep(random.randint(1, 5))

            self.actions.move_to_element(element).perform()
            time.sleep(random.randint(1, 5))

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось навести на LINK_TEXT')
            # print(f'Account{self.count}: {e}')

    def move_to_partial_text(self, element_page):
        try:
            element = self.browser.find_element(By.PARTIAL_LINK_TEXT, element_page)
            width = element.size['width']
            height = element.size['height']
            x_offset = random.randint(0, width)
            y_offset = random.randint(0, height)

            self.actions.move_by_offset(x_offset, y_offset)
            self.actions.perform()
            time.sleep(random.randint(1, 5))

            self.actions.move_to_element(element).perform()
            time.sleep(random.randint(1, 5))

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось навести на PARTIAL_LINK_TEXT')
            # print(f'Account{self.count}: {e}')

    def move_to_css(self, element_page):
        try:
            element = self.browser.find_element(By.CSS_SELECTOR, element_page)
            width = element.size['width']
            height = element.size['height']
            x_offset = random.randint(0, width)
            y_offset = random.randint(0, height)

            self.actions.move_by_offset(x_offset, y_offset)
            self.actions.perform()
            time.sleep(random.randint(1, 5))

            self.actions.move_to_element(element).perform()
            time.sleep(random.randint(1, 5))

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось навести на CSS_SELECTOR')
            # print(f'Account{self.count}: {e}')

    def move_to_class(self, element_page):
        try:
            element = self.browser.find_element(By.CLASS_NAME, element_page)
            width = element.size['width']
            height = element.size['height']
            x_offset = random.randint(0, width)
            y_offset = random.randint(0, height)

            self.actions.move_by_offset(x_offset, y_offset)
            self.actions.perform()
            time.sleep(random.randint(1, 5))

            self.actions.move_to_element(element).perform()
            time.sleep(random.randint(1, 5))

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось навести на CLASS_NAME')
            # print(f'Account{self.count}: {e}')

    def move_to_id(self, element_page):
        try:
            element = self.browser.find_element(By.ID, element_page)
            width = element.size['width']
            height = element.size['height']
            x_offset = random.randint(0, width)
            y_offset = random.randint(0, height)

            self.actions.move_by_offset(x_offset, y_offset)
            self.actions.perform()
            time.sleep(random.randint(1, 5))

            self.actions.move_to_element(element).perform()
            time.sleep(random.randint(1, 5))

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось навести на ID')
            # print(f'Account{self.count}: {e}')

    def move_to_name(self, element_page):
        try:
            element = self.browser.find_element(By.NAME, element_page)
            width = element.size['width']
            height = element.size['height']
            x_offset = random.randint(0, width)
            y_offset = random.randint(0, height)

            self.actions.move_by_offset(x_offset, y_offset)
            self.actions.perform()
            time.sleep(random.randint(1, 5))

            self.actions.move_to_element(element).perform()
            time.sleep(random.randint(1, 5))

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось навести на NAME')
            # print(f'Account{self.count}: {e}')

    def move_and_click_xpath(self, element):
        self.random_time_sleep_fast()
        self.move_to(element)
        self.click_xpath(element)
        self.random_time_sleep_fast()

    def move_and_click_class(self, element):
        self.random_time_sleep_fast()
        self.move_to_class(element)
        self.click_class(element)
        self.random_time_sleep_fast()

    def move_and_click_css(self, element):
        self.random_time_sleep_fast()
        self.move_to_css(element)
        self.click_css(element)
        self.random_time_sleep_fast()

    def move_and_click_text(self, element):
        self.random_time_sleep_fast()
        self.move_to_text(element)
        self.click_text(element)
        self.random_time_sleep_fast()

    def move_and_click_partial_text(self, element):
        self.random_time_sleep_fast()
        self.move_to_partial_text(element)
        self.click_partial_text(element)
        self.random_time_sleep_fast()

    def move_to_and_click_static_css(self, static_element):
        parent = self.browser.find_element(By.CSS_SELECTOR, static_element)
        button = parent.find_element(By.CSS_SELECTOR, 'button')
        self.actions.move_to_element(button)
        self.random_time_sleep_big()
        self.actions.click().perform()
        self.random_time_sleep_big()

    def move_to_and_click_static_class(self, static_element):
        parent = self.browser.find_element(By.CLASS_NAME, static_element)
        button = parent.find_element(By.CSS_SELECTOR, 'button')
        self.actions.move_to_element(button)
        self.random_time_sleep_big()
        self.actions.click().perform()
        self.random_time_sleep_big()

    def move_to_and_click_static_class_3_button(self, static_element):
        total_scroll = int(random.randint(70, 150))
        num_steps = int(random.randint(1, 3))
        step_size = total_scroll

        try:
            # Находим элементы
            self.browser.refresh()
            parent = self.browser.find_element(By.CLASS_NAME, static_element)
            button = parent.find_elements(By.CSS_SELECTOR, 'button')[2]

            # Прокручиваем страницу с постом
            for i in range(num_steps):
                self.browser.execute_script(f"window.scrollBy(0, {step_size})")
                self.random_time_for_send_keys()
            self.browser.execute_script(f"window.scrollBy(0, {total_scroll % step_size})")

            # Ищем кнопку save и жмем
            self.actions.move_to_element(button)
            self.actions.click().perform()
            self.random_time_sleep_large()

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось нажать на ТРЕТЬЮ кнопку в элменте')
            # print(f'Account{self.count}: {e}')

    def move_to_and_click_static_class_2_button(self, static_element):
        total_scroll = int(random.randint(70, 150))
        num_steps = int(random.randint(1, 3))
        step_size = total_scroll

        try:
            # Находим элементы
            self.browser.refresh()
            parent = self.browser.find_element(By.CLASS_NAME, static_element)
            button = parent.find_elements(By.CSS_SELECTOR, 'button')[1]

            # Прокручиваем страницу с постом
            for i in range(num_steps):
                self.browser.execute_script(f"window.scrollBy(0, {step_size})")
                self.random_time_for_send_keys()
            self.browser.execute_script(f"window.scrollBy(0, {total_scroll % step_size})")

            # Ищем кнопку save и жмем
            self.actions.move_to_element(button)
            self.actions.click().perform()
            self.random_time_sleep_large()

        except Exception as e:
            print(f'Account{self.count}: [-] Не удалось нажать на ВТОРУЮ кнопку в элменте')
            # print(f'Account{self.count}: {e}')

    def enter_word(self, element, word):
        try:
            self.random_time_sleep_fast()
            request = self.browser.find_element(By.CSS_SELECTOR, element)
            for letter in word:
                request.send_keys(letter)
                self.random_time_for_send_keys()  # добавляем задержку между вводом каждой буквы
            request.send_keys(Keys.ENTER)
        except Exception as e:
            print(f'Account{self.count}: [-] Не удаллось ввести текст')
            print(f'Account{self.count}: {e}')

    def start_menu(self):
        try:
            parent = self.browser.find_element(By.CLASS_NAME, '_1DeR7_QiQnu2UK0e2dDfYD')
            parent.send_keys(Keys.ESCAPE)
            time.sleep(random.randint(2, 6))
            parent.send_keys(Keys.ESCAPE)
            print(f'Account{self.count}: [+] Попытался Закрыть это всратое меню')
        # Условие на прохождению стартового меню с интересами
        # num_click_random = int(random.randint(0, 5))
        # try:
        #     if self.browser.find_element(By.CLASS_NAME, '_3miLvWoAksppOIKDbHmCpH'):
        #         # Список переменных для скрипта
        #         print(f'Account{self.count}: Start_menu_found!!')
        #         print(f'Account{self.count}: 1')
        #         parent = self.browser.find_element(By.CLASS_NAME, '_2aK1Wp37TOccNSDJhJiDXo false')
        #         button = parent.find_elements(By.CSS_SELECTOR, 'button')
        #         print(f'Account{self.count}: 2')
        #         print(f'Account{self.count}: {button}')
        #         random_elements_interests = random.sample(button, k=int(random.randint(1, 5)))  # Выбор рандомных интересов в количестве : 1-5 pcs
        #         print(f'Account{self.count}: 3')
        #
        #         # # Пропуск выбора пола
        #         #
        #         # self.move_to_class(self.btn_skip_start_menu)
        #         # self.click_class(self.btn_skip_start_menu)
        #         # self.random_time_sleep_large()
        #         # Выбираем и тыкаем в 3 интереса
        #
        #         for element in random_elements_interests:
        #             print(f'Account{self.count}: 4')
        #             self.move_and_click_css(element)
        #
        #         # Тыкаем продолжить
        #         print(f'Account{self.count}: 5')
        #         self.move_and_click_class(self.btn_continue_start_menu)
        #
        #         # Выбираем сабреддиты на которые нужно подписаться
        #         elements_subred = self.browser.find_elements((By. CLASS_NAME, '_2h_rraB53rhUmsB6cnedRY '))
        #         random_elements_subred = random.sample(elements_subred, k=int(random.randint(1, 3)))  # Выбор рандомных интересов в количестве : 1-3 pcs
        #         for element in random_elements_subred:
        #             print(f'Account{self.count}: 6')
        #             self.move_and_click_class(element)
        #
        #         # Тыкаем продолжить
        #         self.move_and_click_class(self.btn_continue_start_menu)
        #
        #         # Тыкаем рандом, рандомное количество раз
        #         self.move_to_class(self.btn_randomize)
        #         for i in range(num_click_random):
        #             self.click_class(self.btn_randomize)
        #             self.random_time_sleep_large()
        #         print(f'Account{self.count}: [+] Выбрал аватар')
        #
        #         # Тыкаем продолжить
        #         self.move_and_click_class(self.btn_continue_start_menu)
        #
        #         # Выгружаем куки
        #         with open(f"/home/ivan/PycharmProjects/Reddit_Up_Vote_v1/Cookie/{self.username}_cookies", "ab") as f:
        #             pickle.dump(self.browser.get_cookies(), f)
        #         print(f'Account{self.count}: [+] Выгрузил Куки')

        except Exception:
            # with open(f"/home/ivan/PycharmProjects/Reddit_Up_Vote_v1/Cookie/{self.username}_cookies", "ab") as f:
            #     pickle.dump(self.browser.get_cookies(), f)
            # print(f'Account{self.count}: [-] Не смог закрыть ебучее Start_menu')
            pass

    def setting_nsfw(self):
        try:
            # Переменные для старта
            random_element = random.choice(list(self.elements_sex_for_random.values()))

            # Открываем вкладку с настройками аккаунта
            self.browser.get('https://www.reddit.com/settings/')
            self.random_time_sleep_large()

            # Настраиваем пол
            self.move_and_click_xpath(self.btn_setting_sex)
            self.move_and_click_xpath(random_element)

            # Переходим на вкладку профиля
            self.move_and_click_xpath(self.profile_in_setting)
            self.random_time_sleep_fast()

            # Switch_nswf
            self.move_to_and_click_static_css(self.switch_nsfw)
            print(f'Account{self.count}: [+] Переключил NSFW')

            # Всплывающее окно с подтверждением действий
            try:
                if self.browser.find_element(By.CSS_SELECTOR, self.btn_confirm_NSFW):
                    self.move_and_click_css(self.btn_confirm_NSFW)
                    print(f'Account{self.count}: [+] Подтвердил переключение NSFW')
                else:
                    print(f'Account{self.count}: [+] Подтверждение не потребовалось')
            except Exception:
                print(f'Account{self.count}: [-] Подтверждение не потребовалось')

            # Переходим на вкладку настроек ленты
            self.move_and_click_xpath(self.feed_setting)

            # Switch_adult
            try:
                self.move_to_and_click_static_css(self.switch_adult_cont)
                print(f'Account{self.count}: [+] Переключил Adult_Switch')
            except Exception:
                print(f'Account{self.count}: [-] Не удалось переключить Adult_Switch')

            # Switch_safe
            try:
                self.move_to_and_click_static_css(self.switch_safe_browsing)
                print(f'Account{self.count}: [+] Переключил Safe_browser_mode')
            except Exception:
                print(f'Account{self.count}: [-] Не удалось переключить Safe_browser_mode')

            # Safe_search отключить
            try:
                self.browser.get('https://www.reddit.com/search/?q=')
                self.move_to_and_click_static_css(self.btn_safe_search)
                print(f'Account{self.count}: [+] Переключил Safe_Search')
            except Exception:
                print(f'Account{self.count}: [-] Не удалось переключить Safe_Search')

            print(f'Account{self.count}: [+] Аккаунт настроен успешно!')
        except Exception as e:
            print(f'Account{self.count}: [-] Настройки акаунта прошли НЕ КОРРЕКТНО')
            print(f'Account{self.count}: {e}')
            self.start_menu()
