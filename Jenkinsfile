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

                pip3 install --break-system-packages pandas numpy matplotlib scikit-learn pytest
                '''
            }
        }

        stage('Run Application') {
            steps {
                sh 'python3 main.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh '~/.local/bin/pytest || true'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My Sonar Server') {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=delivery-optimization \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://localhost:9000 \
                      -Dsonar.login=squ_80b05dd0a6ad27fddbb99cb3558725823ebb7854

                    '''
                }
            }
        }

        stage("Quality Gate") {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
