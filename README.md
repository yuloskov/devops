# Moscow time web app
## Description
This app is built using python flask framework and containerized using docker. It shows current Moscow time. 
## How to build
```docker build -t tag_name .```
## How to run
```docker run yuloskov/time:latest```
## How to test
```
cd app_python/web
pip install pytest
pytest -v
```

The app will run on port 5000.
