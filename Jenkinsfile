pipeline {
    environment {
        D_USER = credentials('docker_username')
        D_PASS = credentials('docker_password')
        SSH = credentials('Ansible-ssh')
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
                sh "docker login -u=$D_USER -p=$D_PASS"
                sh "docker-compose push" 
            }
        }
        stage('Ansible Deploy') {
             steps {
           sh 'scp -i ~/.ssh/id_rsa docker-compose.yaml 34.105.178.165:'
           sh 'scp -i ~/.ssh/id_rsa nginx.conf 34.105.178.165:'
           sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"}
        }
}
}
