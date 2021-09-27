"""A simple python app that shows current Moscow time"""

import datetime

import os
import pytz
from flask import Flask, render_template


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)


    # pylint: disable=unused-variable
    @app.route("/")
    def index():
        """Main page"""
        timezone = pytz.timezone("Europe/Moscow")
        cur_time = str(datetime.datetime.now().astimezone(timezone))

        writepath = os.environ.get("DATA_PATH", 'times.txt')
        mode = "a" if os.path.exists(writepath) else "w"
        with open(writepath, mode, encoding="utf-8") as file:
            file.write(f"{cur_time}\n")

        return (
            render_template(
                "main.html",
                time=cur_time,
            ),
            200,
        )

    @app.route("/visits")
    def visits():
        writepath = os.environ.get("DATA_PATH")
        try:
            with open(writepath, "r", encoding="utf-8") as file:
                content = file.read()
        except OSError as err:
            print(err)
            content = "No visits yet \n"

        return (
            render_template(
                "visits.html",
                visits=content.split("\n")[:-1],
            ),
            200,
        )

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(host="0.0.0.0")
