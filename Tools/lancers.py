import os
from selenium.webdriver import Chrome, ChromeOptions
import time
import pandas as pd

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
    # options.add_argument('--incognito')          # シークレットモードの設定を付与
    options.add_argument('--user-data-dir=profile')

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(executable_path=os.getcwd() + "/" + driver_path, options=options)

def getProgressWork(driver):
    title_list = []
    progressWork = driver.find_element_by_class_name("in-progress")
    titles = progressWork.find_elements_by_css_selector(".work-title")
    for title in titles:
        title_list.append([title.text])
    status_list = []
    statuses = progressWork.find_elements_by_css_selector(".work-status")
    for status in statuses:
        status_list.append(status)
    proposal_list = []
    proposals = progressWork.find_elements_by_css_selector(".work-status.count_data")
    for proposal in proposals:
        proposal_list.append(proposal)
    data = []
    for n in range(len(title_list)-1):
        print(title_list[n])
        print(status_list[n])
        print(proposal_list[n])
        data.append([title_list[n], status_list[n], proposal_list[n]])
    return data

# find_element_by_css_selector

# main処理
def main():
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    # Webサイトを開く
    url = "https://www.lancers.jp/mypage?ref=side_menu"
    driver.get(url)
    time.sleep(5)
 
    data = getProgressWork(driver)
    print(data)

    driver.close()

    # df = pd.DataFrame(job_data)
    # print(df)

    # df.to_csv("data.csv")
        


# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
