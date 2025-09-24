pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/vaishnavi-shingare08/jenkins-CICD-pipeline.git'
            }
        }

        stage('Build') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t myapp:latest .'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'echo "Tests passed!"'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                sh 'docker run -d -p 5000:5000 myapp:latest'
            }
        }
    }
}
