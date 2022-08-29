from robot.api.deco import library, keyword
import requests
import sqlite3


@library
class apiCall():

    @keyword
    def get_status(self, username, password):
        x = requests.get("http://localhost:8080/api/auth/token", auth=(username, password))
        return x.json()['status']

    @keyword
    def reset_database(self):
        conn = sqlite3.connect('../../instance/demo_app.sqlite')
        conn.execute("delete from user;")
        conn.commit()
        conn.close()

