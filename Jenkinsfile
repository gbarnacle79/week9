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
        }  stage('Build images and push to dockerhub'){
            steps{
                sh "docker-compose --d"
                sh "docker-login $git"
                sh "docker-compose push" }
        }
    }

