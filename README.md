# Weather Application
## developed during my DevOps course with Sky
#### This is a Flask web application that uses the OpenWeather API to display weather forecasts for cities around the world.


### Features
Users can search for weather forecasts by city name. The application displays the current weather conditions, as well as a five-day forecast
The application uses the OpenWeather API to retrieve weather data.


### Requirements
Python 3.7 or higher

Flask

Requests


### Getting started - locally
1. Clone the repository:
`git clone https://github.com/WeraGitHub/bits_please_project.git`

2. Navigate to the project directory:
`cd weather-forecast-app`

3. Install the required packages:
`pip install -r requirements.txt`

4. You should generate your own OpenWeather API key in order to use this application. You can get a free API key by signing up here. https://openweathermap.org/

5. Start the application:
`python app.py`

6. Open your web browser and go to http://localhost:5000.


### Usage
Navigate to the Weather page within this application.
Enter a city name in the search bar and click "Search".
The current weather conditions and a five-day forecast will be displayed.


# CI/CD
### for video step by step tutorials go to the DevOps section of this web application when running, alternatively you can see the videos straight away in the static folder
## AWS, Jenkins and Docker

### AWS - create and connect to an EC2 instance
Create your ec2 instance with the elastic IP address and right security group

### Connect to your instance via SSH

### Install Jenkins

`sudo yum update -y`

`sudo yum install -y git`

`sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo`

`sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key`

`sudo yum upgrade`

`sudo amazon-linux-extras install java-openjdk11 -y`

`sudo yum install jenkins -y`

`sudo systemctl enable jenkins`

`sudo systemctl start jenkins`

`sudo cat /var/lib/jenkins/secrets/initialAdminPassword`


Browse to your PublicIP:8080 to unlock Jenkins
Then install suggested plugins
Then create first admin user with the following values:
Username: jenkinsadmin
Password: ***
Confirm password: ***
Fullname: jenkinsadmin
Email: jenkins@jenkins.com

###	Install Docker

`sudo yum -y install docker`

`sudo systemctl start docker`

`sudo docker info`

### Also, to not have to type sudo before docker commands everytime you can add your user to the group by:

`sudo gpasswd -a ec2-user docker`

Make sure you restart your ssh connection after that.


### Add jenkins to a docker group

`sudo usermod -aG docker jenkins`

`sudo systemctl restart jenkins`


###	Create and add Dockerfile to your project stored on GitHub
Dockerfile content:

```
# Use an official Python runtime as a parent image
FROM python:3

# Introduce maintainer of this document
MAINTAINER Weronika "weronikalimberger@gmail.com"

# Set the working directory to /app
WORKDIR /app

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set Flask environment to production
ENV FLASK_ENV=production

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
```

And make sure app.py content is:
```
from application import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```


### Create a webhook in Github

Copy public IP of your instance

Navigate to Settings -> Webhook -> Add webhook

In Payload URL paste:

http://*your-public-IP-here*:8080/github-webhook/ 

In content type drop down choose: *application/x-www-form-urlencoded*

Select trigger option of *Just the push event.*

And click *Add webhook*
![image](https://user-images.githubusercontent.com/67145460/235289714-4d8fe2e8-6c86-43f5-b493-7fe8f4e49de2.png)




#### If youre GitHub repo is private you need to create credentials in Jenkins – using ssh key and make sure you configure GitHub repo in a matching manner, before you start creating your Jenkins pipeline



### Create Pipeline in Jenkins
Make sure you have downloaded 'Pyenv Pipeline' plugin in your Jenkins (https://plugins.jenkins.io/pyenv-pipeline)
Your Jenkinsfile has this content:
```
pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "sky-project-image"
        DOCKER_CONTAINER_NAME = "sky-project-container"
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
                echo 'Testing is done now.'
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
```
And now back in Jenkins:
1. Create new item (job) - make it a pipeline
2. Tick Build Trigger: *GitHub hook trigger for GITScm polling*
3. In the Pipeline section: ![image](https://user-images.githubusercontent.com/67145460/235289498-9de3dee7-43bb-475b-8678-97f348edab00.png)
4. Click *Apply* then *Save*
5. *Build Now*
![image](https://user-images.githubusercontent.com/67145460/235289597-58ebbb0f-acec-40ad-90b9-199b96bcb724.png)

Our web app should be now available on http://*your-public-IP-here*:5000 



# 	:tada:	:tada:	:tada:  Done :) 	:tada: 	:tada: 	:tada:
