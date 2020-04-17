pipeline {
  agent {
    kubernetes {
      yaml """
spec:
  containers:
  - image: "krishbharath/jenkins-slave"
    name: "docker"
    command:
      - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-socket
  - image: "python:3.7"
    name: "python"
    command:
      - cat
    tty: true
  restartPolicy: "Never"
  securityContext: {}
  volumes:
  - name: docker-socket
    hostPath:
      path: /var/run/docker.sock
      """
    }
  }
  stages {
    stage ("Checkout_and_build") {
      steps {
        container('docker') {
          git branch: 'jenkins-pipeline', changelog: false, poll: false, url: 'https://github.com/bharath-krishna/mkdocs_docker.git'
          script {
            sh "docker build -t mkdocs_image ."
          }
        }
      }
    }
    stage('Run') {
      steps {
        container('python') {
          git branch: 'jenkins-pipeline', changelog: false, poll: false, url: 'https://github.com/bharath-krishna/mkdocs_docker.git'
          script {
            sh "python3 -m pip install python docker"
            sh "pytest -s -v"
          }
        }
      }
    }
  }
}