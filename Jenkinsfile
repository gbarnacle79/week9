pipeline {
    environment {
        registry = "gbarnacle79/*****"
        registryCredential = credentials("git")
    }
    agent any
    stages {
        stage('Unit testing') {
            steps {
                sh "bash test.sh"
             }
        }  
        stage('Build images and push to dockerhub'){
            steps{
                sh "docker-compose up -d"
                sh "docker-login -u=$registryCredentials_USR -p=$registryCredentials_PSW"
                sh "docker-compose push" }
        }
    }

}
