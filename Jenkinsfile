pipeline {
  agent {
    // Using kubernetes cloud to create jenkins agent
    kubernetes {
      // Pod spec for agent. Agent image created using jenkins-agent.Dockerfile
      yaml """
spec:
  containers:
  - image: "krishbharath/jenkins-slave:triad"
    imagePullPolicy: Always
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
        container('docker') {
          // chekout mkdocs repo
          git branch: 'jenkins-pipeline', changelog: false, poll: false, url: 'https://github.com/bharath-krishna/mkdocs_docker.git'
        }
      }
    }

    stage('Test') {
      steps {
        container('docker') {
          script {
            // Run tests
            sh "pytest -s -v"
          }
        }
      }
    }

    stage ("Build") {
      steps {
        container('docker') {
          script {
            // Build image only if the above stages succeeds
            withCredentials([usernamePassword(credentialsId: 'docker_hub_creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
              sh """
                docker login --username=$DOCKER_USERNAME --password=$DOCKER_PASSWORD
                docker build -t krishbharath/mkdocs_image .
              """
            }
          }
        }
      }
    }

    stage ("test_serve") {
      steps {
        container('docker') {
          // Create test pod and sleep untill ready and then run tests
          sh """
            kubectl apply -f mkdocs_test_pod.yaml
            sleep 60
            pytest tests/test_mkdocs_image.py::test_serve
            pytest tests/test_mkdocs_image.py::test_run
          """
        }
      }
    }

    // Push production image if above tests passes
    // stage ("Push") {
    //   steps {
    //     container('docker') {
    //       script {
    //         // Build image only if the above stages succeeds
    //         sh """
    //           docker push krishbharath/mkdocs_image
    //         """
    //       }
    //     }
    //   }
    // }

    stage ("CleanUp") {
      steps {
        container('docker') {
          script {
            // Build image only if the above stages succeeds
            sh """
              kubectl delete -f mkdocs_test_pod.yaml
            """
          }
        }
      }
    }


  }
}