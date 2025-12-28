pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'yashrajmonani'
        APP_NAME = 'flask-k8s-demo'
        IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKER_IMAGE = "${DOCKER_HUB_USER}/${APP_NAME}:${IMAGE_TAG}"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/yashmonani/k8s-jenkins-project.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Vulnerability Scan (Trivy)') {
            steps {
                script {
                    echo 'Scanning for vulnerabilities...'
                    sh "trivy image --severity CRITICAL --exit-code 1 ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Pushing to Registry...'
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                        sh "echo $PASS | docker login -u $USER --password-stdin"
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo 'Deploying to Kubeadm Cluster...'
                    withKubeConfig([credentialsId: 'my-k8s-config']) {
                        sh "sed -i 's|IMAGE_NAME|${DOCKER_IMAGE}|g' deployment.yaml"
                        sh "/bin/kubectl apply -f service.yaml"
                        sh "/bin/kubectl apply -f deployment.yaml"
                        sh "/bin/kubectl rollout status deployment/flask-app"
                    }
                }
            }
        }
    }
    
    post {
        always {
            sh "docker rmi ${DOCKER_IMAGE} || true"
        }
    }
}
