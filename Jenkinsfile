node {
    def venvDir = "${env.WORKSPACE}/venv"

    docker.image('python:3.9.11').inside('-p 5000:5000') {
        
        stage('Checkout') {
            checkout scm
        }

        stage('Setup') {
            sh """
            python -m venv ${venvDir}
            . ${venvDir}/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
            echo "✅ Build berhasil!"
            """
        }

        stage('Test') {
            sh """
            . ${venvDir}/bin/activate
            pytest --junitxml=report.xml
            echo "✅ Test berhasil!"
            """
        }
    }
}
