pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "sky-project-image"
        DOCKER_CONTAINER_NAME = "sky-project-container"
        WEATHER_API_KEY = '03cf0108f3a426eceaf55fd80047b8ef'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Get code from GitHub'
                git branch: 'main', url: 'https://github.com/WeraGitHub/SkyProject.git'
                echo 'Got the code.'
            }
        }
        stage('Build') {
            steps {
                echo 'Check what files are here'
                sh 'ls -la'
                sh 'pwd'
                echo 'Build an image.'
                sh 'docker build -t $DOCKER_IMAGE_NAME .'
                echo 'Image built.'
            }
        }
        stage('Test') {
            steps {
                echo 'Run tests'
                withPythonEnv('python3') {
                    sh 'pip install pytest'
                    sh 'pip install flask'
                    sh 'pip install requests'
                    sh 'python -m pytest tests/'
                }
                echo 'Testing. done..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy.'
                echo 'stop and remove named container if it already exists - just in case'
                sh 'docker stop $DOCKER_CONTAINER_NAME || true'
                sh 'docker rm $DOCKER_CONTAINER_NAME || true'
                echo 'run the container'
                sh 'docker run --name $DOCKER_CONTAINER_NAME -d -p 5000:5000 $DOCKER_IMAGE_NAME'
                echo 'Deployed <3'
            }
        }
    }
}
