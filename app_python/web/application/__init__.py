"""A simple python app that shows current Moscow time"""

import pytz
import datetime
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

    @app.route("/")
    def index():
        """Main page"""
        timezone = pytz.timezone('Europe/Moscow')
        return render_template(
            'main.html',
            time=str(datetime.datetime.now().astimezone(timezone)),
        ), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")
