# Best practices to containerize a simple python app
## Docker
### 1 - requirements.txt
Put all your requirements in requirements.txt file for better readability and easy installation.
### 2 - requirements.txt installation
Install requirements.txt before copying the codebase, so the updates in code would not run the installation again.
### 3 - Requirements with cache
Caching requirements will help to avoid long builds.
### 4 - Put exact versions
You should put exact versions for requirements and docker image you use.
That will help you to minimize build time and depend less on new updates.
### 5 - Change user from root
You should change the user from root in your container, so the server wouldn't be hacked in case of a security breach.
