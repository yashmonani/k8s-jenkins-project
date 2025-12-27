# k8s-jenkins-project
# End-to-End DevSecOps Kubernetes Project

## 🚀 Project Overview
This project demonstrates a complete CI/CD pipeline for a microservices-based Python web application. It automates the workflow from code commit to production deployment on a self-managed Kubernetes cluster.

## 🛠 Tech Stack
* **Cloud/Infrastructure:** AWS EC2, Kubernetes (Kubeadm Multi-Node Cluster)
* **CI/CD:** Jenkins (Declarative Pipeline)
* **Containerization:** Docker & Docker Hub
* **Security:** Trivy (Image Vulnerability Scanning)
* **SCM:** Git & GitHub (Webhook Integration)

## 🔄 Pipeline Workflow
1.  **Checkout:** Pulls code from GitHub.
2.  **Build:** Creates a Docker image tagged with the Jenkins Build ID.
3.  **Scan:** Runs `Trivy` to detect Critical vulnerabilities (DevSecOps).
4.  **Push:** Uploads the secure image to Docker Hub.
5.  **Deploy:** Updates the Kubernetes Deployment using dynamic manifest manipulation (`sed`).

## 📊 Features
* **Zero-Downtime Deployment:** Uses Rolling Updates strategy.
* **Load Balancing:** Exposed via NodePort Service to distribute traffic.
* **Visual Validation:** The app displays the serving Pod's Hostname to verify load balancing.

## 📸 Screenshots
<img width="979" height="358" alt="image" src="https://github.com/user-attachments/assets/5b327bd3-0766-4383-a0c4-16997bca9ac1" />
<img width="1365" height="464" alt="image" src="https://github.com/user-attachments/assets/f0ab018a-df68-4b4a-94fc-0a3fa56e799d" />

