from flask import Flask, g, render_template, request
import sqlite3

app = Flask(__name__)


def connect_db():
    sql = sqlite3.connect('gminy.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.route('/')
def index():
    db = get_db()
    lubuskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'lubuskie'")
    lubuskie_powiaty = lubuskie_cur.fetchall()

    wielkopolskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'wielkopolskie'")
    wielkopolskie_powiaty = wielkopolskie_cur.fetchall()

    zachodniopomorskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'zachodniopomorskie'")
    zachodniopomorskie_powiaty = zachodniopomorskie_cur.fetchall()

    # powiatl = request.form['powiatl']
    # powiatw = request.form['powiatw']
    # powiatz = request.form['powiatz']
    return render_template('index.html', lubuskie_powiaty=lubuskie_powiaty, wielkopolskie_powiaty=wielkopolskie_powiaty,
                           zachodniopomorskie_powiaty=zachodniopomorskie_powiaty)


if __name__ == '__main__':
    app.run()
