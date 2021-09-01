# Best practices for CI
## Github actions
### 1 - Build your app in docker
Building apps in docker allows to test it as the it will be run on the server.
Moreover it allows to utilize caching for shorter building time.
### 2 - Dependencies
Run each stage subsequently, so if one of the stages fails, we won't spend vm time. 
### 3 - Use cache
Using cache for dependency installation allows to save vm time

## Jenkins
### 1 - Using docker socket
Using docker socket volume allows you to run docker pipelines in Jenkins
