pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        "PATH+PYTEST" = "/tmp/pip/bin"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --prefix=/tmp/pip pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=pytest.xml'
            }
        }
    }

    post {
        always {
            junit 'pytest.xml'
        }
        success {
            echo 'Tests passed successfully.'
        }
        failure {
            echo 'Tests failed.'
        }
    }
}
