**Nome do Projeto:** Sistema de Automação Residencial

**Descrição:**

Este projeto visa desenvolver um sistema de automação residencial usando Python e Flask para o backend e HTML, CSS e JavaScript para o frontend. O sistema permitirá aos usuários controlar diversos aspectos de sua casa, como iluminação, temperatura, segurança e cortinas, usando comandos de voz ou uma interface web.

**Recursos:**

* Controle de iluminação usando comandos de voz ou uma interface web
* Definição e manutenção de uma temperatura desejada usando um comando de voz ou uma interface web
* Ativação e desativação do sistema de segurança usando um comando de voz ou uma interface web
* Abertura e fechamento de cortinas usando um comando de voz ou uma interface web
* Monitoramento e análise de dados de consumo de energia
* Visualização de padrões de consumo de energia ao longo do tempo

**Requisitos:**

* Python 3.x
* Flask
* SpeechRecognition
* sqlite3
* pandas
* matplotlib
* TensorFlow.js (para reconhecimento de voz)

**Instalação:**

1. Crie um ambiente virtual Python:

```
virtualenv venv
```

2. Ative o ambiente virtual:

```
source venv/bin/activate
```

3. Instale as dependências necessárias:

```
pip install flask speech_recognition sqlite3 pandas matplotlib tensorflowjs
```

4. Crie o banco de dados:

```
python creatdb.py
```

5. Execute o backend:

```
python app.py
```

6. Inicie o servidor web:

```
flask run
```

**Uso:**

1. Abra um navegador da web e vá para http://localhost:5000.
2. Você pode controlar diversos aspectos de sua casa usando a interface web.
3. Para usar comandos de voz, certifique-se de ter um microfone conectado ao seu computador.
4. Fale comandos como "Ligar Luz", "Desligar Luz", "Definir Temperatura para 25", "Ativar Sistema de Segurança" ou "Abrir Cortinas".

**Exemplo de saída:**

```
Comando recebido: ligar luz
Ligando luz...
Operação realizada com sucesso.

Comando recebido: definir temperatura para 25
Definindo temperatura para 25...
Operação realizada com sucesso.

Comando recebido: ativar sistema de segurança
Ativando sistema de segurança...
Operação realizada com sucesso.
```

**Problemas conhecidos:**

* O sistema atualmente só suporta um conjunto limitado de comandos de voz.
* O sistema não possui nenhum recurso de segurança embutido para impedir acesso não autorizado.

**Trabalhos futuros:**

* Implementar mais comandos de voz para controlar diversos dispositivos domésticos.
* Adicionar mais recursos à interface web, como monitoramento em tempo real do status dos dispositivos.
* Implementar autenticação e autorização de usuário para a interface web.
* Integrar com dispositivos domésticos inteligentes de diferentes fabricantes.

**Observação:**

Este projeto ainda está em andamento, mas já é possível usá-lo para controlar alguns dispositivos domésticos básicos.
