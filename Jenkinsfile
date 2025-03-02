node {
    def venvDir = "${env.WORKSPACE}/venv"

    docker.image('python:3.9.11').inside('-p 5000:5000') {

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
            input message: 'Lanjutkan ke tahap Deploy?', ok: 'Proceed'
        }

        stage('Deploy') {
            sh """
            . ${venvDir}/bin/activate
            python app.py &  # Menjalankan aplikasi di background
            sleep 60  # Menjeda eksekusi selama 1 menit
            pkill -f app.py  # Menghentikan aplikasi setelah 1 menit
            echo "✅ Deploy selesai!"
            """
        }
    }
}
