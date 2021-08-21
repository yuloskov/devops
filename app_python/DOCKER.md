# Best practices to containerize a simple python app
## Docker
### 1 - requirements.txt
Put all your requirements in requirements.txt file for better readability and easy installation.
### 2 - requirements.txt installation
Install requirements.txt before copying the codebase, so the updates in code would not run the installation again.
