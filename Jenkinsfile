pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sowbagya-049/Delivery-optimization.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 --version
                pip3 --version

                pip3 install --break-system-packages pandas numpy matplotlib scikit-learn pytest coverage
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh 'python3 main.py'
            }
        }

        stage('Run Tests with Coverage') {
            steps {
                sh '''
                coverage run -m pytest
                coverage xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My Sonar Server') {
                    sh '''
                    /opt/sonar-scanner/bin/sonar-scanner \
                      -Dsonar.projectKey=delivery-optimization \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://sonarqube:9000 \
                      -Dsonar.token= squ_80b05dd0a6ad27fddbb99cb3558725823ebb7854\
                      -Dsonar.python.coverage.reportPaths=coverage.xml
                    '''
                }
            }
        }

        stage("Quality Gate") {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
