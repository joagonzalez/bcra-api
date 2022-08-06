pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing stage..'
            }
        }
        stage('Build') {
            when {
                // Only say hello if a "greeting" is requested
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                echo 'Building stage..'
            }
        }
        stage('Deploy') {
            when {
                // Only say hello if a "greeting" is requested
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                echo 'Deploying stage..'
            }
        }
    }
}