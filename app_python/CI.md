# Best practices for CI
## Github actions
### 1 - Build your app in docker
Building apps in docker allows to test it as the it will be run on the server.
Moreover it allows to utilize caching for shorter building time.

## Jenkins
### 1 - Using docker socket
Using docker socket volume allows you to run docker pipelines in Jenkins
