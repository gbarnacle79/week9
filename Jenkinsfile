pipeline {
    environment {
        registry = "gbarnacle79/*****"
        registryCredential = "git"
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
                sh "docker-login -u=$git_USR -p=$git_PSW"
                sh "docker-compose push" }
        }
    }

}
