node {
    def venvDir = 'venv'

    stage('Build') {
        docker.image('python:3.9.11').inside('--mount source=pip-cache,target=/root/.cache/pip -p 5000:5000') {
            sh '''
            python -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt --cache-dir /root/.cache/pip
            echo "✅ Build berhasil!"
            '''
        }
    }

    stage('Test') {
        docker.image('python:3.9.11').inside() {
            sh '''
            . venv/bin/activate
            pytest --junitxml=report.xml
            echo "✅ Test berhasil!"
            '''
        }
    }
}
