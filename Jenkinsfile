pipeline {
  agent {
    kubernetes {
      yaml """
spec:
  containers:
  - image: "krishbharath/jenkins-slave:triad"
    name: "docker"
    command:
      - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-socket
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
        }
      }
    }

    stage('Test') {
      steps {
        container('docker') {
          script {
            sh "pytest -s -v"
          }
        }
      }
    }

    stage ("Build") {
      steps {
        container('docker') {
          script {
            sh "docker build -t mkdocs_image ."
          }
        }
      }
    }

  }
}