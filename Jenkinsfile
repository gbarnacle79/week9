pipeline {
    environment {
        AUTH = credentials("dockerhub_id")
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
                sh "docker login -u=$AUTH_USR -p=$AUTH_PSW ${env.AUTH}"
                sh "docker-compose push" }
        }
    }

}
