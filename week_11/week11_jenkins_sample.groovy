# Jenkins is an automation server for building, testing, and deploying
# Works using pipelines or freestyle jobs
# Can trigger tasks from Git pushes, cron, or manual clicks

pipeline {
  agent any
  stages {
    stage('Pull') {
      steps {
        git 'https://github.com/your/repo.git'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest'
      }
    }
    stage('Deploy') {
      steps {
        sh 'ansible-playbook deploy.yaml'
      }
    }
  }
}
