from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Data.data import user_setting_dict
import zipfile


class SettingBrowserClass:

    def __init__(self, count):
        self.count = int(count)  # Счетчик для загрузки профиле
        self.PROXY_HOST = user_setting_dict[f'profile{self.count}']['PROXY']                 # rotating proxy or host
        self.PROXY_PORT = user_setting_dict[f'profile{self.count}']['HOST']                  # port
        self.PROXY_USER = user_setting_dict[f'profile{self.count}']['PROXY_USER']            # username
        self.PROXY_PASS = user_setting_dict[f'profile{self.count}']['PROXY_PASS']            # password
        self.window_size_setting = user_setting_dict[f'profile{self.count}']['window size']  # Изменение размера окна
        self.user_agent = user_setting_dict[f'profile{self.count}']['user-agent']            # Юзер агент
        self.time_zone_id = user_setting_dict[f'profile{self.count}']['timezoneId']          # Название тайм-зоны
        self.timeOffset = user_setting_dict[f'profile{self.count}']['timeOffset']            # Отклонение в минутах
        self.service = Service('/path/to/chromedriver')

    def setting_browser_bot(self):
        # Настройки для авторизации proxy
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };  
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        
        );
        """ % (self.PROXY_HOST, self.PROXY_PORT, self.PROXY_USER, self.PROXY_PASS)

        def get_chromedriver(use_proxy=True, user_agent=None):
            options = webdriver.ChromeOptions()

            # Настройки прокси
            if use_proxy:
                pluginfile = f'proxy_auth_plugin{self.count}.zip'  # Переменная для создания архива хранящего прокси

                with zipfile.ZipFile(pluginfile, 'w') as zp:
                    zp.writestr("manifest.json", manifest_json)
                    zp.writestr("background.js", background_js)

                options.add_extension(pluginfile)

            if user_agent:
                options.add_argument(f'user-agent={self.user_agent}')  # Юзер агент
                options.add_argument(f"--window-size={self.window_size_setting}")  # Размер окна
                options.add_experimental_option("excludeSwitches", ['enable-automation'])  # Отключение панели с "Работает тестовое ПО"
                options.add_argument("--oobe-timezone-override-for-tests")
                options.add_argument(
                    "--disable-blink-features=AutomationControlled")  # Отключение видимости WevDriver

                # WebRTC
                options.add_extension('driver/WebRTC_Control.crx')

                # Отключаем WebGL
                options.add_argument('--disable-webgl')

                # Отключаем Canvas
                options.add_argument('--disable-canvas')

                # Указываем маску системных шрифтов (Работоспособность не доказана)
                options.add_argument('--font-rendering-hinting=none')
                options.add_argument('--font-rendering-hinting=medium')

                # Указываем маску используемых раскладок клавиатуры
                options.add_experimental_option("prefs", {
                    "intl.accept_languages": "en-US"
                })

                # Отключаем всплвающие окна
                options.add_argument("--disable-popup-blocking")
                options.add_argument("--disable-notifications")
                options.add_argument("--disable-infobars")

            browser = webdriver.Chrome(
                'driver/chromedriver',
                options=options,
                service=self.service,
            )
            # Настройки time_zone ДЛЯ ПЕРВОГО ОТКРЫТОГО URL
            browser.execute_cdp_cmd('Emulation.setTimezoneOverride', {
                'timezoneId': self.time_zone_id,
                'timeOffset': self.timeOffset,
            })

            return browser
        return get_chromedriver(use_proxy=True, user_agent=True)
