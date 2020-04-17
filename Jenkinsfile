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
    stage ("Checkout") {
      steps {
        git checkout
      }

    }
    stage('Build') {
      steps {
        container('docker') {
          sh 'docker ps -a'
          sh 'docker version'
        }
      }
    }
  }
}