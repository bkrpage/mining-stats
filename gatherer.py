import requests
from settings import settings, actions, protocols
import json

# from coins import Coins


URL_SUFFIX = '/index.php?page=api&action='

API_KEY = '080d160f74828ee6a2f24e3b0d1864cbe7c37d64eb69c26b2416d6910ce55196'
URL_API_KEY = '&api_key=' + API_KEY


def get_balances():
    response = make_request(actions['get_user_all_balances'])

    json_data = json.loads(response.text)

    print json_data

    balance_data = json_data["getuserallbalances"]["data"]

    return balance_data


def get_current_workers(coin):
    response = make_request(actions['get_current_workers'], None, coin)

    json_data = json.loads(response.text)

    print json_data

    worker_data = json_data['getcurrentworkers']['data']

    print worker_data

    return worker_data


def get_user_hashrate(coin):
    response = make_request(actions['get_user_hashrate'], settings['id'], coin)

    json_data = json.loads(response.text)

    print json_data

    hashrate_data = json_data['getuserhashrate']['data']

    print hashrate_data

    return hashrate_data


def get_user_workers(coin):
    response = make_request(actions['get_user_workers'], settings['id'], coin)

    json_data = json.loads(response.text)

    print json_data

    workers_data = json_data['getuserworkers']['data']

    print workers_data

    return workers_data


def get_dashboard_data():
    response = make_request(actions['get_dashboard_data'], settings['id'])

    json_data = json.loads(response.text)

    print json_data

    dashboard_data = json_data[actions['get_dashboard_data']]['data']

    print dashboard_data

    return dashboard_data


def get_profit_stats():
    response = make_request(actions['get_mining_and_profit_statistics'])

    json_data = json.loads(response.text)

    profit_data = json_data['return']

    print profit_data

    return profit_data


def make_request(action, user_id=None, coin=None):
    req = url_builder(protocols['https'], action, user_id, coin)

    response = requests.Session().get(req)

    return response


def url_builder(protocol, action, user_id=None, coin=None):
    url_with_action = settings['base_url'] + URL_SUFFIX + action + URL_API_KEY

    if user_id is not None:
        id_param = '&id=' + user_id
    else:
        id_param = ''

    if coin is None:
        url = protocol + url_with_action + id_param
    else:
        url = protocol + coin + '.' + url_with_action + id_param

    print 'Built URL: ' + url
    return url
