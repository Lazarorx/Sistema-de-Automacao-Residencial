from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import sqlite3
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Variáveis simuladas para o estado do sistema
security_system_armed = False
blinds_open = False

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect('consumo_energia.db')

# Função para criar a tabela no banco de dados se não existir
def criar_tabela_consumo_energia():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consumo_energia (
            timestamp TEXT PRIMARY KEY,
            valor_consumo INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Inicializar tabela no início da execução
criar_tabela_consumo_energia()

# Inicializar DataFrame para armazenar dados de consumo
consumo_energia = pd.DataFrame(columns=['timestamp', 'consumo'])

def ouvir_comando():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando de voz...")
        audio = reconhecedor.listen(source)

    try:
        comando = reconhecedor.recognize_google(audio, language="pt-BR")
        print(f"Comando recebido: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao solicitar reconhecimento de fala: {e}")
        return None

# Rota para armar/desarmar o sistema de segurança por voz
@app.route('/api/security/command', methods=['POST'])
def arm_security_voice():
    global security_system_armed
    comando = ouvir_comando()

    if comando and ("armar" in comando or "ativar" in comando):
        security_system_armed = True
    elif comando and ("desarmar" in comando or "desativar" in comando):
        security_system_armed = False

    # Gravar no banco de dados
    gravar_consumo_energia(security_system_armed)

    return jsonify({'status': 'Operação realizada com sucesso', 'armed': security_system_armed})

# Rota para obter o estado do sistema de segurança
@app.route('/api/security/status')
def security_status():
    return jsonify({'status': 'Operação realizada com sucesso', 'armed': security_system_armed})

# Rota para abrir/fechar cortinas e persianas por voz
@app.route('/api/blinds/command', methods=['POST'])
def control_blinds_voice():
    global blinds_open
    comando = ouvir_comando()

    if comando and ("abrir" in comando):
        blinds_open = True
    elif comando and ("fechar" in comando):
        blinds_open = False

    # Gravar no banco de dados
    gravar_consumo_energia(blinds_open)

    return jsonify({'status': 'Operação realizada com sucesso', 'blinds_open': blinds_open})

# Função para gravar no banco de dados
def gravar_consumo_energia(valor_consumo):
    conn = conectar_banco()
    cursor = conn.cursor()

    timestamp_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('INSERT INTO consumo_energia (timestamp, valor_consumo) VALUES (?, ?)', (timestamp_atual, valor_consumo))

    conn.commit()
    conn.close()

# Rota para armazenar dados de consumo
@app.route('/api/energy/consume', methods=['POST'])
def consume_energy():
    global consumo_energia
    consumo = request.json.get('consumo')

    if consumo is not None:
        novo_dado = {'timestamp': pd.to_datetime('now'), 'consumo': consumo}
        consumo_energia = consumo_energia.append(novo_dado, ignore_index=True)
        return jsonify({'status': 'Dados de consumo armazenados com sucesso.'})
    else:
        return jsonify({'error': 'Parâmetro de consumo ausente ou inválido.'}), 400

# Rota para obter dados de consumo
@app.route('/api/energy/data')
def energy_data():
    return jsonify(consumo_energia.to_dict(orient='records'))

# Rota para realizar análises e visualizações
@app.route('/api/energy/analyze')
def analyze_energy():
    # Algumas análises de exemplo
    media_consumo = consumo_energia['consumo'].mean()
    max_consumo = consumo_energia['consumo'].max()
    min_consumo = consumo_energia['consumo'].min()

    # Visualização de exemplo
    plt.plot(consumo_energia['timestamp'], consumo_energia['consumo'])
    plt.xlabel('Timestamp')
    plt.ylabel('Consumo')
    plt.title('Padrões de Consumo de Energia ao Longo do Tempo')
    plt.show()

    return jsonify({
        'media_consumo': media_consumo,
        'max_consumo': max_consumo,
        'min_consumo': min_consumo,
        'status': 'Análises e visualizações realizadas com sucesso.'
    })

# Rota padrão para renderizar a interface web
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
