from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from part_nine.config import basic_config

class BrowserEngine:
    # 関数を呼ぶ時にどのdriverを使用するのか,指定があった方がいい気がする
    @staticmethod
    def init_local_driver():
        """
        util関数,localのdriverを初期化
        プロパティーなければ,defaultはchrome_driver
        :return: driverオブジェクトを返す
        """
        # ここではdriverのタイプも判断する必要がある
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=option,
                                  executable_path=basic_config.EXECUTABLE_PATH)
        return driver

    # 関数を呼ぶ時にどのdriverを使用するのか,指定があった方がいい気がする
    @staticmethod
    def init_remote_driver():
        """
        util関数,remoteのdriverを初期化
        何を起動するのかは,basic_configで設定
        詳細はbasic_configファイルに設置してある
        :return: result_dict はdict,構造{"名前":driver}
        """
        remote_browser_dict = basic_config.REMOTE_DRIVER_DICT
        # 返り値を保存, 構造{"名前":driver}
        result_dict = {}
        for name,url in remote_browser_dict.items():
            # ここではdriverのタイプも判断する必要がある
            option = webdriver.ChromeOptions()
            option.add_argument("disable-infobars")
            driver = webdriver.Remote(
                command_executor=url,
                # ここでドライブを設定可能
                desired_capabilities=DesiredCapabilities.CHROME
            )
            result_dict[name] = driver

        return result_dict