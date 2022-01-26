pipeline {
    agent any 

    stages {
        stage('Get Latest Sourcecode') {
            steps {
                git 'https://github.com/sajjavenkey50/sample.git'
            }
        }
        stage('Function to conversion of excel sheet into Data frame') {
            steps {
                sh "python3 parametercoverage1.py"
            }
        }
        stage('Read the xml and convert to data frame') {
            steps {
                sh "python3 parametercoverage2.py" 
            }
        }
        stage('Function to find the Parameter in the xml data frame') {
            steps {
                sh "python3 parametercoverage3.py"
            }
        }
    }
}
