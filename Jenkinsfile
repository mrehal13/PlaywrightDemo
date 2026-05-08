/* groovylint-disable CompileStatic */
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/mrehal13/PlaywrightDemo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    source venv/bin/activate
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest HTML Report'
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }

        success {
            echo "✅ Tests Passed"
        }

        failure {
            echo "❌ Tests Failed"
        }
    }
}
