pipeline {
agent any

stages {

    stage('Build Docker Image') {
        steps {
            bat 'docker build -t YOUR_DOCKERHUB_USERNAME/docker-automation-app:latest .'
        }
    }

    stage('Trivy Scan') {
        steps {
            bat '"C:\\Users\\BHUMIKA.G\\AppData\\Local\\Microsoft\\WinGet\\Links\\trivy.exe" image YOUR_DOCKERHUB_USERNAME/docker-automation-app:latest'
        }
    }

    stage('Push to Docker Hub') {
        steps {
            withCredentials([usernamePassword(
                credentialsId: 'dockerhub-credentials',
                usernameVariable: 'DOCKER_USERNAME',
                passwordVariable: 'DOCKER_PASSWORD'
            )]) {
                bat 'docker login -u "%DOCKER_USERNAME%" -p "%DOCKER_PASSWORD%"'
                bat 'docker push bhu27/docker-automation-app:latest'
            }
        }
    }
}


}