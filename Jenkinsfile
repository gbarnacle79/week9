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
           sh 'scp -i $SSH /home/gbarnacle79/week9/docker-compose.yaml manager:'
           sh 'scp -i $SSH /home/gbarnacle79/week9/nginx.conf manager:'
           sh "ansible-playbook -i week9/inventory.yaml week9/playbook.yaml"}
        }
}
}
