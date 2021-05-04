import requests
import json


def get_json(url):
    x = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
    j = json.loads(x.text)
    return j


BASE_URL = "http://api.nbp.pl/api/"

TABLES_URL = BASE_URL + "exchangerates/" + "tables/"


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


RATES_URL = BASE_URL.join("exchangerates/").join("rates/")


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
