from flask import Flask, render_template
import redis
import mysql.connector
import os


app = Flask(__name__)

r = redis.Redis(host="redis", port=6379)


@app.route("/")
def home():
    count = r.incr("hits")
    
    return render_template("index.html", count = count)



def db_connection(host, username, password, database):
    '''
    - Take host
    - take username
    - Take password
    - database

    '''
    connection = mysql.connector.connect(
        host=host, 
        user=username,
        password=password,
        database=database
    )
    return connection



if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
