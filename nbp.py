import requests
import json


BASE_URL = "http://api.nbp.pl/api/"
TABLES_URL = BASE_URL + "exchangerates/" + "tables/"
RATES_URL = BASE_URL + "exchangerates/" + "rates/"


def get_json(url):
    reqest_result = requests.get(url)
    if reqest_result.status_code != 404 and reqest_result.status_code != 400:
        json_reqest = json.loads(reqest_result.text)
    else:
        json_reqest = None

    return json_reqest


def get_table(table):
    url = TABLES_URL + table + "/"
    return get_json(url)


def get_last_table(table, count):
    url = TABLES_URL + table + "/" + "last/" + str(count)
    return get_json(url)


def get_today_table(table):
    url = TABLES_URL + table + "/" + "today"
    return get_json(url)


def get_date_table(table, date):
    url = TABLES_URL + table + "/" + str(date)
    return get_json(url)


def get_between_table(table, start_date, end_date):
    url = TABLES_URL + table + "/" + str(start_date) + "/" + str(end_date) + "/"
    return get_json(url)


def get_current_rate(table, code):
    url = RATES_URL + table + "/" + code + "/"
    return get_json(url)


def get_last_rate(table, code, count):
    url = RATES_URL + table + "/" + code + "/" + "last/" + str(count) + "/"
    return get_json(url)


def get_today_rate(table, code):
    url = RATES_URL + table + "/" + code + "/" + "today/"
    return get_json(url)


def get_date_rate(table, code, date):
    url = RATES_URL + table + "/" + code + "/" + str(date) + "/"
    return get_json(url)


def get_between_rate(table, code, start_date, end_date):
    url = RATES_URL + table + "/" + code + "/" + str(start_date) + "/" + str(end_date) + "/"
    return get_json(url)
