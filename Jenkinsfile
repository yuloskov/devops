pipeline {
    agent {
        docker {
            image 'python:3.9.6-alpine3.14'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r app_python/web/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest -v'
            }
        }
    }
}