pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/bhu27/docker-automation-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t docker-automation-app .'
            }
        }

        stage('Trivy Scan') {
            steps {
                bat 'trivy image docker-automation-app'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Docker Hub push will be configured next.'
            }
        }
    }
}
