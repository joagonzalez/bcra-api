pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing stage..'
            }
        }
        if(env.BRANCH_NAME == 'master'){
            stage('Build') {
                steps {
                    echo 'Building stage..'
                }
            }
        }
        if(env.BRANCH_NAME == 'master'){
            stage('Deploy') {
                steps {
                    echo 'Deploying stage..'
                }
            }
        }
    }
}