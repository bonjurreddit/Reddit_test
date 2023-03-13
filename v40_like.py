from v40_setting_account import SettingAccount
from selenium.webdriver.common.by import By
import random


class UpVote(SettingAccount):

    def __init__(self, count):
        super().__init__(count)
        self.calls_count = 0

        # Элементы Реддит
        self.search_reddit = '#header-search-bar'
        self.tab_new_css = '#AppRouter-main-content > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div._31N0dvxfpsO6Ur5AKx4O5d > div._1OVBBWLtHoSPfGCRaPzpTf._3nSp9cdBpqL13CqjdMr2L_._2OVNlZuUd8L9v0yVECZ2iA > div.wBtTDilkW_rtT2k5x3eie > div._2pUO1Sfe7WlIHvq6goN3Pz > a:nth-child(2)'
        self.btn_join = '#AppRouter-main-content > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div.MSTY2ZpsdupobywLEfx9u > div > div.QscnL9OySMkHhGudEvEya > div > div._2I_YJCANrzkY2DZkeu2nht > div > button'
        self.btn_subscribe = '#AppRouter-main-content > div > div > div._3ozFtOe6WpJEMUtxDOIvtU > div.MSTY2ZpsdupobywLEfx9u > div > div.QscnL9OySMkHhGudEvEya > div > div._2I_YJCANrzkY2DZkeu2nht > div._1Q_zPN5YtTLQVG72WhRuf3 > button'
        self.btn_up_vote = '#upvote-button-t3_11jswna-overlay'
        self.frame_with_share_save = '_1hwEKkB_38tIoal6fcdrt9'
        self.share_menu = '_2uYY-KeuYHKiwl-9aF0UiL PWY92ySDjTYrTAiutq4ty'
        self.block_with_up_vote_top = '#overlayScrollContainer'
        self.block_with_up_vote_side = '#overlayScrollContainer > div._1npCwF50X2J7Wt82SZi6J0 > div.u35lf2ynn4jHsVUwPmNU.Dx3UxiK86VcfkFQVHNXNi > div.uI_hDmU5GSiudtABRz_37'

    def find_communities_use_search(self, sub_name):
        try:
            # Тыкаем в строку поиска саба
            self.move_and_click_css(self.search_reddit)

            # Вводит название саба
            self.enter_word(self.search_reddit, sub_name)

            # Safe_search отключить
            try:
                self.browser.get('https://www.reddit.com/search/?q=')
                self.move_to_and_click_static_css(self.btn_safe_search)
                print(f'Account{self.count}: [+] Переключил Safe_Search')
            except Exception:
                print(f'Account{self.count}: [-] Не удалось переключить Safe_Search')

            # Ищем наш сабреддит в списке и жмем на него
            self.move_and_click_text(f'r/{sub_name}')
            print(f'Account{self.count}: [+] Открыл саб через поиск')

        except Exception as e:
            print(f'Account{self.count}: [-] Не смог открыть саб через поиск')
            print(f'Account{self.count}: {e}')

    def open_communities_url(self, url):
        try:  # Открываем саб через урл
            self.random_time_sleep_fast()
            self.browser.get(f'{url}')
            self.random_time_sleep_fast()
        except Exception as e:
            print(f'Account{self.count}: [-] Не смог открыть саб через URL ')
            print(f'Account{self.count}: {e}')

    def tab_new(self, sub_name):
        self.random_time_sleep_fast()
        self.browser.refresh()
        btn_new = self.browser.find_element(By.CSS_SELECTOR, self.tab_new_css)
        try:
            if btn_new.is_displayed():
                self.move_and_click_css(self.tab_new_css)
                print(f'Account{self.count}: [+] Перешел в NEW напрямую')
            else:
                self.browser.get(f'https://www.reddit.com/r/{sub_name}/new/')
                self.random_time_sleep_large()
                print(f'Account{self.count}: [+] Перешел в NEW через ссылку')

        except Exception as e:
            print(f'Account{self.count}: [-] Возникли проблемы с переходом в NEW')
            print(f'Account{self.count}: {e}')

    def random_subscribe(self):
        try:
            # Находим кнопку подписаться
            subscribe_btn = self.browser.find_element(By.CSS_SELECTOR, self.btn_subscribe)
            # Если уже подписаны, ничего не делаем
            if subscribe_btn.text == 'Joined':
                print(f'Account{self.count}: [+] Уже подписан на этот Саб')
            # Если не подписаны, подписываемся с рандомом
            if subscribe_btn.text == 'Join' and random.random() < 0.5:
                self.random_time_sleep_fast()
                self.browser.refresh()
                self.move_to_css(self.btn_join)
                self.click_css(self.btn_join)
                self.random_time_sleep_large()
                print(f'Account{self.count}: [+] Уже подписан на этот Саб')

        except Exception as e:
            print(f'Account{self.count}: [-] Возникли проблемы с подпиской на саб')
            print(f'Account{self.count}: {e}')

    def search_post_with_title_name(self, post_title):

        # Счетчик на выход из бесконечного цикла, в случае ошибки
        self.calls_count += 1
        if self.calls_count >= 150:
            print(f'Account{self.count}: [-] Не смог найти пост')
            self.close_browser()
            self.calls_count = 0

        # Перменные для поиска
        random_num = int(random.randint(100, 200))
        random_step = int(random.randint(81, 158))

        # Если поста не видно на странице, прокручиваем страницу до отображения поста
        try:
            scroll = self.browser.find_element(By.PARTIAL_LINK_TEXT, post_title)
            print(f'Account{self.count}: [+] Пост появился на странице')
        except Exception:
            self.browser.execute_script(f"window.scrollBy(0, {random_step});")
            self.search_post_with_title_name(post_title)
            return


        try:
            # self.random_time_sleep_fast()
            # # Аккуратно подводим к посту
            # scroll_position = scroll.location['y'] - random_num
            # for i in range(0, scroll_position, random_step):
            #     self.browser.execute_script(f"window.scrollBy(0, {random_step})")
            #     self.random_time_for_send_keys()  # добавляем задержку между прокрутками

            # Открываем пост
            self.move_and_click_partial_text(post_title)
            print(f'Account{self.count}: [+] Пост открыт!')

        except Exception as e:
            print(f'Account{self.count}: [-] НЕ удалось открыть пост!')
            print(f'Account{self.count}: {e}')

    def up_vote_through_post_top(self):
        try:
            self.random_time_sleep_fast()
            self.move_to_and_click_static_css(self.block_with_up_vote_top)
            self.random_time_sleep_large()
            print(f'Account{self.count}: [+] Поставил лайк через ТОП!')

        except Exception as e:
            print(f'Account{self.count}: [-] НЕ подписался на саб')
            print(f'Account{self.count}: {e}')

    def up_vote_through_side(self):
        try:
            self.random_time_sleep_fast()
            self.move_to_and_click_static_css(self.block_with_up_vote_side)
            self.random_time_sleep_large()
            print(f'Account{self.count}: [+] Поставил лайк через боковую панель!')
        except Exception as e:
            print(f'Account{self.count}: [-] НЕ подписался на саб')
            print(f'Account{self.count}: {e}')

    def click_save(self):
        try:
            self.random_time_sleep_fast()
            self.move_to_and_click_static_class_3_button(self.frame_with_share_save)
            self.random_time_sleep_fast()
            print(f'Account{self.count}: [+] Нажал кнопку save...')
        except Exception as e:
            print(f'Account{self.count}: [-] Скорее всего кнопка save скрыта...')
            print(f'Account{self.count}: {e}')

    def up_vote_random(self):
        if random.random() < 0.5:
            self.up_vote_through_post_top()
        else:
            self.up_vote_through_side()

    def save_or_share_or_pass(self):
        if random.random() < 0.5:
            self.click_save()
        else:
            pass

    def open_sub_random(self, sub_name, url):
        if random.random() < 0.5:
            self.find_communities_use_search(sub_name)
        else:
            self.open_communities_url(url)


# Функция лайка 1-2х случайных постов
# Определит как делать рандом между аккаунтами, по способам поиска саба и лайкинга
