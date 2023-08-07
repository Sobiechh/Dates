import requests


def fetch_fun_fact(month: int, day: int) -> str:
    url = f"http://numbersapi.com/{month}/{day}/date"
    response = requests.get(url)
    content = response.text

    return content
