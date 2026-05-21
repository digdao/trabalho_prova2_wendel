pipeline {
    agent any

    environment {
        // Caminho do seu Python (mantenha o caminho que funcionou na etapa de dependências)
        PYTHON_PATH = "C:\\Users\\Rodrigo\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe"
        
        // Caminho do compilador do Inno Setup
        INNO_SUITE  = "C:\\Program Files (x86)\\Inno Setup 6\\ISCC.exe"
    }

    stages {
        stage('Limpar Ambiente') {
            steps {
                echo 'Removendo artefatos de builds anteriores...'
                bat 'if exist dist rmdir /s /q dist'
                bat 'if exist build rmdir /s /q build'
                bat 'if exist setup_out rmdir /s /q setup_out'
            }
        }

        stage('Instalar Dependências') {
            steps {
                echo 'Configurando pacotes do Python...'
                bat "\"${PYTHON_PATH}\" -m pip install --upgrade pip"
                bat "\"${PYTHON_PATH}\" -m pip install pyinstaller"
            }
        }

        stage('Compilar Executável (PyInstaller)') {
            steps {
                echo 'Transformando script Python em binário Windows...'
                // Mudança crucial: Chamando o PyInstaller através do executável do Python ativo
                bat "\"${PYTHON_PATH}\" -m PyInstaller --onefile --noconsole app.py"
            }
        }

        stage('Gerar Instalador Oficial (Inno Setup)') {
            steps {
                echo 'Criando o assistente de instalação (.exe)...'
                bat "\"${INNO_SUITE}\" script.iss"
            }
        }
    }

    post {
        success {
            echo 'Sucesso! Arquivando o instalador final...'
            archiveArtifacts artifacts: 'setup_out/Instalador_Tarefas_Setup.exe', fingerprint: true
        }
        failure {
            echo 'Ocorreu um erro na geração do build. Verifique os logs.'
        }
    }
}