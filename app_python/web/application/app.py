"""A simple python app that shows current Moscow time"""

import pytz
import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Main page"""
    timezone = pytz.timezone('Europe/Moscow')
    return render_template(
        'main.html',
        time=str(datetime.datetime.now().astimezone(timezone)),
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
