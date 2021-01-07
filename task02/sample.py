# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
import os
import time

# Chromeを起動する関数

def set_driver(driver_path, headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)

# main処理
def main():
    search_keyword = "高収入"
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
# ブラウザを開く。

    driver.get("https://www.yahoo.co.jp")

    # 3秒待機
    time.sleep(3)

    # ログインボタンをクリックする
    login_btn = driver.find_element_by_xpath('//*[@id="Login"]/div/p[1]/a')
    login_btn.click()

    # 1秒待機
    time.sleep(1)
    login_id = driver.find_element_by_name("login")
    login_id.send_keys("hameji_gucchi")

    # 次へボタンをクリック
    next_btn = driver.find_element_by_name("btnNext")
    next_btn.click()

    # 1秒待機
    time.sleep(1)

    # パスワードを入力
    password = driver.find_element_by_name("passwd")
    password.send_keys("walnutcouch350")

    # ログインボタンをクリック
    login_btn = driver.find_element_by_name("btnSubmit")
    login_btn.click()

    # 10秒待機
    time.sleep(10)

    # ブラウザを終了する
    driver.close()


# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
