pipeline {
    agent {
        docker {
            image 'python:3.10'  // Use official Python Docker image
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --user pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_calculator.py'
            }
            steps{
                sh 'pytest --junitxml=pytest.xml'
            }    
        }
    }

    post {
        always {
            junit 'pytest.xml' // optional, if using junit-style test results
        }
        success {
            echo 'Tests passed successfully.'
        }
        failure {
            echo 'Tests failed.'
        }
    }
}
