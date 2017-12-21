from flask import Flask, render_template
import gatherer


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=["GET"])
def test_thing():
    string = 'TESTING'
    gatherer.get_profit_stats()

    return render_template('index_test.html', string=string)


@app.route('/balances', methods=["GET"])
def balances():
    balance_data = gatherer.get_balances()
    return render_template('balances.html', balances=balance_data)


@app.route('/workers/<coin>', methods=['GET'])
def workers(coin=None):
    workers_amount = gatherer.get_current_workers(coin)
    return render_template('workers.html', coin=coin, amount=workers_amount)


@app.route('/my_hashrate/<coin>', methods=['GET'])
def hashrate(coin=None):
    hash_rate = gatherer.get_user_hashrate(coin)
    return render_template('hashrate.html', coin=coin, hashrate=hash_rate)


@app.route('/my_workers/<coin>', methods=['GET'])
def my_workers(coin=None):
    user_workers = gatherer.get_user_workers(coin)
    return render_template('user_workers.html', coin=coin, workers=user_workers)


@app.route('/statistics', methods=['GET'])
def statistics():
    stats = gatherer.get_profit_stats()
    return render_template('stats.html', stats=stats)


if __name__ == '__main__':
    app.run()
