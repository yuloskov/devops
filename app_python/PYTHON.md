# Best practices to develop a simple python app
## Python App
### 1 - Git Ignore
Using .gitignore helps to avoid adding unnecessary files to git.
### 2 - Use Pylint
Linter helps you to better organize your code in terms of style in structure.
### 3 - Docstring
Docstrings are good for code readability.
### 4 - Imports
Sort imports by the length.
### 5 - __name__ == "__main__"
It is good to add this comparison to the module, so that module could be run separately. 
### 6 - Using templates
With templates you can write html in your python app. Later, when we add nginx or smthing, we will add static files like css and images.

## Unit tests
### 1 - pytest
Pytest is an easy-to-use framework well compatible with flask app.
### 2 - Using fixture
Client fixture will be called by each individual test. It gives us a simple interface to the application, where we can trigger test requests to the application. The client will also keep track of cookies for us.