pipeline {
    agent {
        docker {
            image 'python:3.9.11'
            args '-p 5000:5000'  // Port Flask biasanya 5000
        }
    }
    environment {
        VENV_DIR = 'venv'  // Direktori virtual environment
    }
    stages {
        stage('Setup') {
            steps {
                sh '''
                python -m venv $VENV_DIR
                . $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                . $VENV_DIR/bin/activate
                pytest --junitxml=report.xml
                '''
            }
        }
    }
}
