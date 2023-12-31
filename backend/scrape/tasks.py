from celery import shared_task, current_task
from time import sleep
import json
import math

import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)

from user.serializers import ResearchResultSerializer

from celery.result import AsyncResult

CUR_DIR = os.getcwd()


def setup_webdriver():
    options = Options()
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    )
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=200,1000")

    chrome_service = service.Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service=chrome_service,
        options=options,
    )

    return driver


def product_name_serializer(product_name, exclusion, exclusion_size, search_word_list):
    if len(product_name) <= exclusion_size:
        return False
    if exclusion:
        # 検索文字のうちいずれかが入っている
        # for word in search_word_list:
        #     if word in product_name:
        #         return True
        # return False

        # 検索文字の最初の文字が入っている
        # if search_word_list[0] in product_name:
        #     return True

        # 検索文字のすべてが入っている
        return all((word in product_name for word in search_word_list))

    return True


def get_item_data(
    site,
    search_amount,
    driver,
    task_id,
    exclusion,
    exclusion_size,
    search_word_list,
    url,
):
    url_list = []
    i = 0

    if site == "メルカリ":
        while len(url_list) < search_amount:
            search_url = f"{url}&page_token=v1:{i}"
            driver.get(search_url)
            sleep(1)
            clientHeight = driver.execute_script('return document.documentElement.clientHeight')+100
            scrollHeight = driver.execute_script('return document.documentElement.scrollHeight')
            window_ratio = math.ceil(scrollHeight / clientHeight)
            try:
                for t in range(window_ratio):
                    driver.execute_script(f"window.scrollBy(0, {clientHeight})")
                    sleep(0.1)
                items = driver.find_elements(
                    By.CSS_SELECTOR, 'li[data-testid="item-cell"] > div > a'
                )
            except NoSuchElementException:
                driver.refresh()
                sleep(5)
                for t in range(window_ratio):
                    driver.execute_script(f"window.scrollBy(0, {clientHeight})")
                    sleep(0.1)
                items = driver.find_elements(
                    By.CSS_SELECTOR, 'li[data-testid="item-cell"] > div > a'
                )

            for item in items:
                try:
                    item_url = item.get_attribute("href")
                except NoSuchElementException:
                    driver.refresh()
                    sleep(5)
                    item_url = item.get_attribute("href")
                url_list.append(item_url)

            i += 1
        print(len(item_url))

        print("")
        for n, url in enumerate(url_list[:search_amount]):
            print(f"商品データ取得中…({n+1}/{search_amount})", end="")
            driver.get(url)
            sleep(1)

            try:
                product_name = driver.find_element(
                    By.CSS_SELECTOR,
                    "#item-info > section > div > .merHeading > div > h1",
                ).text
                if product_name_serializer(
                    product_name, exclusion, exclusion_size, search_word_list
                ):
                    seller_url = driver.find_element(
                        By.CSS_SELECTOR, 'a[data-location="item_details:seller_info"]'
                    ).get_attribute("href")
                    seller_id = seller_url.split("/")[-1]
                    product_price = int(
                        driver.find_element(
                            By.CSS_SELECTOR,
                            'div[data-testid="price"] span:nth-of-type(2)',
                        ).text.replace(",", "")
                    )
                    img_elms = driver.find_elements(
                        By.CSS_SELECTOR,
                        ".sticky-outer-wrapper img",
                    )[:3]
                    img_list = []
                    for img_elm in img_elms:
                        img_list.append(img_elm.get_attribute("src"))
                    while len(img_list) < 3:
                        img_list.append("")
                    product_img1 = img_list[0]
                    product_img2 = img_list[1]
                    product_img3 = img_list[2]
                    sell_status_elm = driver.find_element(
                        By.CSS_SELECTOR, "div[data-testid='image-0']"
                    )
                    sell_status = sell_status_elm.get_attribute("aria-label")
                    if sell_status == "商品サムネイル":
                        sell_status = "販売中"
                    condition = driver.find_element(
                        By.CSS_SELECTOR, "span[data-testid='商品の状態']"
                    ).text
                    data = {
                        "product_img1": product_img1,
                        "product_img2": product_img2,
                        "product_img3": product_img3,
                        "url": url,
                        "product_name": product_name,
                        "seller_id": seller_id,
                        "product_price": product_price,
                        "task_id": task_id,
                        "sell_status": sell_status,
                        "condition": condition,
                    }
                    serializer = ResearchResultSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                else:
                    print(f"商品名:{product_name}", "リスト:{search_word_list}")
            except NoSuchElementException as e:
                print(str(e))
            print("\r", end="")

    elif site == "ヤフオク":
        while len(url_list) < search_amount:
            search_url = f"{url}&n=50:{50*i + 1}"
            driver.get(search_url)
            print(search_url)
            sleep(1)
            try:
                items = driver.find_elements(By.CSS_SELECTOR, ".Product__detail")
            except NoSuchElementException:
                driver.refresh()
                sleep(5)
                items = driver.find_elements(By.CSS_SELECTOR, ".Product__detail")

            for item in items:
                try:
                    item_url = item.find_element(
                        By.CSS_SELECTOR, "a.Product__titleLink"
                    ).get_attribute("href")
                except NoSuchElementException:
                    driver.refresh()
                    sleep(5)
                    item_url = item.find_element(
                        By.CSS_SELECTOR, "a.Product__titleLink"
                    ).get_attribute("href")
                url_list.append(item_url)

            i += 1

        print("")
        for n, url in enumerate(url_list[:search_amount]):
            print(f"商品データ取得中…({n+1}/{search_amount})", end="")
            driver.get(url)
            sleep(1)

            try:
                product_name = driver.find_element(
                    By.CSS_SELECTOR,
                    "h1.ProductTitle__text",
                ).text
                if product_name_serializer(
                    product_name, exclusion, exclusion_size, search_word_list
                ):
                    seller_url = driver.find_element(
                        By.CSS_SELECTOR, "p.Seller__name a"
                    ).get_attribute("href")
                    seller_id = seller_url.split("/")[-1]
                    price_tax = driver.find_element(
                        By.CSS_SELECTOR,
                        "dd.Price__value > span",
                    ).text

                    product_price = int(
                        driver.find_element(
                            By.CSS_SELECTOR,
                            "dd.Price__value",
                        )
                        .text.replace(price_tax, "")
                        .replace(",", "")
                        .replace("円", "")
                    )
                    img_elms = driver.find_elements(
                        By.CSS_SELECTOR,
                        ".ProductImage__inner img",
                    )[:3]
                    img_list = []
                    for img_elm in img_elms:
                        img_list.append(img_elm.get_attribute("src"))
                    while len(img_list) < 3:
                        img_list.append("")
                    product_img1 = img_list[0]
                    product_img2 = img_list[1]
                    product_img3 = img_list[2]
                    sell_status = "販売中"
                    condition = driver.find_element(
                        By.CSS_SELECTOR, "span.Count__detail > a"
                    ).text
                    data = {
                        "product_img1": product_img1,
                        "product_img2": product_img2,
                        "product_img3": product_img3,
                        "url": url,
                        "product_name": product_name,
                        "seller_id": seller_id,
                        "product_price": product_price,
                        "task_id": task_id,
                        "sell_status": sell_status,
                        "condition": condition,
                    }
                    serializer = ResearchResultSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print(serializer.errors)
                    print(data)
                else:
                    print(f"商品名:{product_name}", "リスト:{search_word_list}")
            except NoSuchElementException as e:
                print(str(e))
            print("\r", end="")


@shared_task
def merscraper(data):
    task_id = current_task.request.id
    driver = setup_webdriver()
    driver.implicitly_wait(5)
    exclusion = data["exclusion"]
    exclusion_size = data["exclusion_size"]

    # # 以下クローリング
    print("☆" * 30)
    print("リサーチ開始")

    for dict in data["urlLists"]:
        url = dict["url"]
        search_amount = dict["search_amount"]
        site = dict["site"]
        search_word_list = dict["searchWords"]

        get_item_data(
            site,
            search_amount,
            driver,
            task_id,
            exclusion,
            exclusion_size,
            search_word_list,
            url,
        )

    driver.quit()

    return True
