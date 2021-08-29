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


docker run --rm --name jenkins -p 8080:8080 -p 50000:50000 -u 0 -v `pwd`:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean
dfb9eaee773c424dbd2f4899c86b6376
