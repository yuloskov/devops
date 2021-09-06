![app_python](https://github.com/yuloskov/devops/actions/workflows/test.yml/badge.svg)
# Moscow time web app
## Description
This app is built using python flask framework and containerized using docker. It shows current Moscow time. 
## How to build
```docker build -t tag_name .```
## How to run
```docker run yuloskov/time:master```
The app will run on port 5000.

## How to test
```
cd app_python/web
pip install pytest
pytest -v
```
## Jenkins
Run jenkins with
```
docker run --rm --name jenkins -p 8080:8080 -p 50000:50000 -u 0 -v `pwd`:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean
```

## Terraform
Run terraform with
```
terraform init
terraform apply
```

## Ansible
Rin with
```
cd ansible/playbooks
ansible-playbook -i ../inventory/aws.yml main.yml 
```
