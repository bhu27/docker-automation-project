pipeline {
agent any

stages {

    stage('Build Docker Image') {
        steps {
            bat 'docker build -t docker-automation-app .'
        }
    }

    stage('Trivy Scan') {
        steps {
            bat '"C:\\Users\\BHUMIKA.G\\AppData\\Local\\Microsoft\\WinGet\\Links\\trivy.exe" image docker-automation-app'
        }
    }

    stage('Push to Docker Hub') {
        steps {
            echo 'Docker Hub push will be configured next.'
        }
    }
}


}