pipeline {
    environment {
        registry = "gbarnacle79/Cheesepuffs1"
        registryCredential = "git"
    }
    agent any
    stages {
        stage('Unit testing') {
            steps {
                sh "bash test.sh"
                
            }

        }
    }
}
