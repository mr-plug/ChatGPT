import requests

key = "67c86f3aee5d4doc121739594"

DATA = """
------geckoformboundary26044e22996c7e2779207d1af9bf099f
Content-Disposition: form-data; name="msg"

{text}
------geckoformboundary26044e22996c7e2779207d1af9bf099f
Content-Disposition: form-data; name="hidden_msg"


------geckoformboundary26044e22996c7e2779207d1af9bf099f
Content-Disposition: form-data; name="request_number"

67c838591a5a8doc1902459360
------geckoformboundary26044e22996c7e2779207d1af9bf099f
Content-Disposition: form-data; name="psiholog"

{key}
------geckoformboundary26044e22996c7e2779207d1af9bf099f
Content-Disposition: form-data; name="greeting_msg_key"

0
------geckoformboundary26044e22996c7e2779207d1af9bf099f
Content-Disposition: form-data; name="request_human"

13039966
------geckoformboundary26044e22996c7e2779207d1af9bf099f--
"""


def post(text):
    url = "https://gpt-open.ru/admin/functions.php?action=chat_with_gpt"

    headers = {
        "Content-Type": "multipart/form-data; boundary=----geckoformboundary26044e22996c7e2779207d1af9bf099f",
    }

    # Отправка POST-запроса
    response = requests.post(url, headers=headers, data=DATA.format(text=text, key=key).encode("utf-8"))

    # Вывод ответа
    return response.json()["answer"]


def get_key():
    url = "https://gpt-open.ru/admin/functions.php?action=get_stories"

    # Отправка POST-запроса
    response = requests.get(url)

    # Вывод ответа
    return response.json()['Раздел 1']['0']['_id']

# print(get_key())


text = input()
while text:
    print(post(text))
    text = input()
