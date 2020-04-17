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
    stage ("Checkout_and_build") {
      steps {
        container('docker') {
            git branch: 'jenkins-pipeline', changelog: false, poll: false, url: 'https://github.com/bharath-krishna/mkdocs_docker.git'
            script {
                sh """
                    ls -lha
                    docker build -t mkdocs_image .
                """
            }
        }
      }
    }
    stage('Run') {
      steps {
        container('docker') {
            git branch: 'master', changelog: false, poll: false, url: 'https://github.com/bharath-krishna/triad_challenge.git'
            script {
                sh """
                    ls -lha $WORKSPACE
                    docker rm mkdocs_container
                    docker run --name mkdocs_container -v $WORKSPACE/:/shared_dir -p 8000:8000 mkdocs_image produce
                    ls -lha
                    docker rm mkdocs_container
                """
            }
        }
      }
    }
  }
}