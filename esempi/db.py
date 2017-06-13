from flask import Flask
import pymysql

app = Flask(__name__)


@app.route("/")
def hello():
    result = []
    risu = ""
    # (host,port,user, passwd, db
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db="gruppi_musicali")
    cursor = db.cursor()

    sql = "select nome from gruppo"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            risu += "".join(row)
    finally:
        db.close()
    return risu

