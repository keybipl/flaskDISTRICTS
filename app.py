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


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        db = get_db()
        lubuskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'lubuskie'")
        lubuskie_powiaty = lubuskie_cur.fetchall()

        wielkopolskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'wielkopolskie'")
        wielkopolskie_powiaty = wielkopolskie_cur.fetchall()

        zachodniopomorskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'zachodniopomorskie'")
        zachodniopomorskie_powiaty = zachodniopomorskie_cur.fetchall()

        return render_template('index.html', lubuskie_powiaty=lubuskie_powiaty, wielkopolskie_powiaty=wielkopolskie_powiaty,
                           zachodniopomorskie_powiaty=zachodniopomorskie_powiaty)

    else:
        db = get_db()
        powiatl = request.form['powiatl']
        powiatw = request.form['powiatw']
        powiatz = request.form['powiatz']

        gminyl_cur = db.execute('select * from gminy where powiat = ?', [powiatl])
        gminyl = gminyl_cur.fetchall()

        gminyw_cur = db.execute('select * from gminy where powiat = ?', [powiatw])
        gminyw = gminyw_cur.fetchall()

        gminyz_cur = db.execute('select * from gminy where powiat = ?', [powiatz])
        gminyz = gminyz_cur.fetchall()

        lubuskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'lubuskie'")
        lubuskie_powiaty = lubuskie_cur.fetchall()

        wielkopolskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'wielkopolskie'")
        wielkopolskie_powiaty = wielkopolskie_cur.fetchall()

        zachodniopomorskie_cur = db.execute("SELECT DISTINCT powiat FROM gminy where wojewodztwo = 'zachodniopomorskie'")
        zachodniopomorskie_powiaty = zachodniopomorskie_cur.fetchall()

        return render_template('index.html', powiatl=powiatl, gminyl=gminyl, gminyw=gminyw, gminyz=gminyz,
                               lubuskie_powiaty=lubuskie_powiaty, wielkopolskie_powiaty=wielkopolskie_powiaty,
                           zachodniopomorskie_powiaty=zachodniopomorskie_powiaty)


if __name__ == '__main__':
    app.run()
