from bs4 import BeautifulSoup
from time import sleep
from values import desc
from dotenv import load_dotenv
import lxml
import os
import requests

load_dotenv()

auth_url = os.getenv("auth_url")
main_url = os.getenv("main_url")
url = os.getenv("url")
login = os.getenv("login")
password = os.getenv("password")
data = {
    "backurl": "/auth/",
    "POPUP_AUTH": "N",
    "Login": "Войти",
    "AUTH_FORM": "Y",
    "TYPE": "AUTH",
    "POPUP_AUTH": "N",
    "USER_LOGIN": f"{login}",
    "USER_PASSWORD": f"{password}",
    "Login": "Войти",
    "Login": "Войти",
}
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en;q=0.9",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"YaBrowser\";v=\"23\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.739 Yowser/2.5 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6519a642-47ad74a42355c68f53f9bec9",
  }
session = requests.Session()
session.get(main_url, headers=headers)
session.post(auth_url, headers=headers, data=data)
response = session.get(url, headers=headers, data=data)
soup = BeautifulSoup(response.text, "lxml")
max_page = int(soup.find_all("a", class_="dark_link")[-1].text) + 1


def get_url():
    for count in range(1, 2):
        url_page = f"{url}{count}"
        response = session.get(url_page, headers=headers, data=data)
        soup = BeautifulSoup(response.text, "lxml")
        cards = soup.find_all("div",
            class_="item_block js-notice-block grid-list__item grid-list-border-outer")
        if len(cards) != 0:
            for i in cards:
                card_url = main_url + i.find("a").get("href")
                yield card_url
        else:
            break


def array():
    for card_url in get_url():
        response = session.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="container")
        name = data.find("div", class_="preview_text").text
        char_values = data.find_all("div", class_="char_value")
        char_names = data.find_all("div", class_="char_name")
        row = range(len(char_names))
        image = main_url + data.find("a").get("href")
        chars = {'Название': f'{name}',
                 'Фото': f'{image}'}
        # Блок итераций по характеристикам
        for i in row:
            for k in desc:
                if k in char_names[i].text:
                    char = char_values[i].text.strip()
                    if char:
                        chars[k] = char
                    else:
                        continue
                else:
                    continue
            # Суть происходящего выше здесь
            # if "Тип" in char_names[i].text:
            #     type_of_good = char_values[i].text.strip()
            #     if type_of_good:
            #         chars[char_names[i].find("div", class_="props_item whint").text] = type_of_good
            #         continue
            #     else:
            #         pass
            # elif "Бренд" in char_names[i].text:
            #     brand = char_values[i].text.strip()
            #     if brand:
            #         chars[char_names[i].text] = brand
            #         #chars.append(brand)
            #         continue
            #     else:
            #         pass
            # elif "Модель" in char_names[i].text:
            #     model = char_values[i].text.strip()
            #     if model:
            #         chars[char_names[i].text] = model
            #         #chars.append(model)
            #         continue
            #     else:
            #         pass
            # elif "Длина" in char_names[i].text:
            #     length = char_values[i].text.strip()
            #     if length:
            #         chars[char_names[i].text] = length
            #         #chars.append(length)
            #         continue
            #     else:
            #         pass
            # elif "Транспортная длина" in char_names[i].text:
            #     trans_length = char_values[i].text.strip()
            #     if trans_length:
            #         chars[char_names[i].text] = trans_length
            #         #chars.append(trans_length)
            #         continue
            #     else:
            #         pass
            # elif "Кол-во секций" in char_names[i].text:
            #     sections_number = char_values[i].text.strip()
            #     if sections_number:
            #         chars[char_names[i].text] = sections_number
            #         #chars.append(sections_number)
            #         continue
            #     else:
            #         pass
            # elif "Вес" in char_names[i].text:
            #     weight = char_values[i].text.strip()
            #     if weight:
            #         chars[char_names[i].text] = weight
            #         #chars.append(weight)
            #         continue
            #     else:
            #         pass
            # elif "Тест от" in char_names[i].text:
            #     test_least = char_values[i].text.strip()
            #     if test_least:
            #         chars[char_names[i].text] = test_least
            #         #chars.append(test_least)
            #         continue
            #     else:
            #         pass
            # elif "Тест до" in char_names[i].text:
            #     test_most = char_values[i].text.strip()
            #     if test_most:
            #         chars[char_names[i].text] = test_most
            #         #chars.append(test_most)
            #         continue
            #     else:
            #         pass
            # else:
            #     pass
        yield chars
