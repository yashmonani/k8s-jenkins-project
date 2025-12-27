from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello! I was deployed via Jenkins to a Kubeadm Cluster!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
