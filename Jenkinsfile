pipeline {
    agent any

    environment {
        // UPDATE THESE TWO VARIABLES
        DOCKER_HUB_USER = 'yashrajmonani'
        APP_NAME = 'flask-k8s-demo'
        
        // Dynamic variables
        IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKER_IMAGE = "${DOCKER_HUB_USER}/${APP_NAME}:${IMAGE_TAG}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Replace with your actual GitHub Repo URL
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
                    // If trivy is not found, try installing it or finding its path like kubectl
                    sh "trivy image --severity CRITICAL --exit-code 1 ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    echo 'Pushing to Registry...'
                    // Ensure you created the 'docker-hub-creds' in Manage Jenkins > Credentials
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
                    withKubeConfig([credentialsId: 'k8s-kubeconfig']) {
                        // 1. Update the image in the deployment file ONLY
                        sh "sed -i 's|IMAGE_NAME|${DOCKER_IMAGE}|g' deployment.yaml"
                        
                        // 2. Apply the Service (Networking)
                        // (We do this first so the IP/Port exists before the new pods roll out)
                        sh "/bin/kubectl apply -f service.yaml"

                        // 3. Apply the Deployment (Application)
                        sh "/bin/kubectl apply -f deployment.yaml"
                        
                        // 4. Verify Rollout
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
