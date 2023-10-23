from celery import shared_task
from time import sleep

import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
import os

CUR_DIR = os.getcwd()


@shared_task
def task_2():
    # Chromeの場所を指定
    options = Options()
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    )
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")

    chrome_service = service.Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=chrome_service, options=options)

    driver.implicitly_wait(10)

    # URL作成用
    driver.get("https://news.yahoo.co.jp/")

    print(driver.title)

    driver.quit()

    return driver.title
