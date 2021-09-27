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

    writepath = os.environ.get('DATA_PATH')

    # pylint: disable=unused-variable
    @app.route("/")
    def index():
        """Main page"""
        timezone = pytz.timezone("Europe/Moscow")
        cur_time = str(datetime.datetime.now().astimezone(timezone))

        mode = 'a' if os.path.exists(writepath) else 'w'
        with open(writepath, mode) as f:
            f.write(f'{cur_time}\n')

        return (
            render_template(
                "main.html",
                time=cur_time,
            ),
            200,
        )

    @app.route("/visits")
    def visits():
        try:
            with open(writepath, 'r') as f:
                content = f.read()
        except:
            content = 'No visits yet \n'
        
        return (
            render_template(
                "visits.html",
                visits=content.split('\n')[:-1],
            ),
            200
        )


    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(host="0.0.0.0")
