import simplejson
from flask import Flask, render_template, request
from flask_cors import CORS
from pusher import Pusher

from dbsetup import create_connection, select_all_items, update_item

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# configure pusher object
pusher = Pusher(
    app_id='1496812',
    key='78cb33fbb8155e3d5ed5',
    secret='d886ad050060dc1aacf3',
    cluster='eu',
    ssl=True)

database = "./pythonsqlite.db"
conn = create_connection(database)
c = conn.cursor()


def main():
    global conn, c


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/vote', methods=['POST'])
def vote():
    data = simplejson.loads(request.data)
    update_item(c, [data['member']])
    output = select_all_items(c, [data['member']])
    pusher.trigger(u'poll', u'vote', output)
    return request.data


if __name__ == '__main__':
    main()
    app.run(debug=True)
