node {
    def venvDir = "${env.WORKSPACE}/venv"
    def dockerImage = "rivalhaikakhafizh/wortel-app:latest" 

    docker.image('python:3.9.11').inside('-p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock') {

        stage('Checkout') {
            checkout scm
        }

        stage('Build') {
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

        stage('Manual Approval') {
            input message: 'Lanjutkan ke tahap Deploy Local Env?', ok: 'Proceed'
        }

        stage('Deploy Local Env') {
            sh """
            . ${venvDir}/bin/activate
            python app.py &  # Menjalankan aplikasi di background
            sleep 2  # Menjeda eksekusi selama 1 menit
            pkill -f app.py  # Menghentikan aplikasi setelah 1 menit
            echo "✅ Deploy selesai!"
            """
        }

        stage('Manual Approval for Live Env') {
            input message: 'Apakah Anda ingin deploy ke Live Environment?', ok: 'Proceed'
        }

        stage('Build Docker Image') {
            sh """
            docker build -t ${dockerImage} .
            echo "✅ Docker Image berhasil dibuat!"
            """
        }

        stage('Push Docker Image') {
            withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                sh "docker push ${dockerImage}"
                echo "✅ Docker Image berhasil di-push ke Docker Hub!"
            }
        }
    }
}
