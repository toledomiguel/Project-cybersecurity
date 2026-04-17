# 🛡️ CyberWatch: SIEM & Log Analysis System

O **CyberWatch** é um protótipo de sistema SIEM (Security Information and Event Management) desenvolvido para monitoramento de segurança em tempo real. O sistema realiza a ingestão de logs de um banco de dados MySQL, aplica regras de detecção de intrusão e visualiza as métricas de ameaças em um dashboard interativo.

---

## 🚀 Funcionalidades

* **Monitoramento em Tempo Real:** Varredura contínua da tabela de logs do servidor.
* **Análise de Ameaças:** Motor de detecção baseado em padrões (Regex) para identificar ataques comuns.
* **Gestão de Alertas:** Separação automática de eventos normais e incidentes críticos.
* **Interface Visual:** Dashboard dinâmico para análise de severidade e volume de ataques.

---

## 🛠️ Tecnologias e Dependências

* **Linguagem:** Python 3.13+
* **Banco de Dados:** MySQL (via XAMPP ou Local)

### Bibliotecas Python:

* `mysql-connector-python`: Conexão com o banco de dados
* `streamlit`: Framework para o dashboard web
* `pandas`: Manipulação e tratamento dos dados de segurança

---

## 🔧 Estrutura do Projeto

* `app.py`: Motor principal de detecção e monitoramento
* `database.py`: Camada de persistência e conexão SQL
* `detectors.py`: Lógica de processamento e regras de segurança
* `dashboard.py`: Interface visual do sistema

---

## 📋 Como Instalar e Rodar

### 1. Preparação do Ambiente

Certifique-se de que o MySQL está rodando (XAMPP) e crie o banco de dados `cyberwatch`.

### 2. Instalação de Dependências

Abra o terminal na pasta do projeto e execute:

```bash
pip install mysql-connector-python streamlit pandas
```

### 3. Configuração do Banco de Dados

Configure as credenciais de acesso no arquivo `database.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "cyberwatch"
}
```

### 4. Execução do Sistema

#### Rodar o motor de detecção:

```bash
python app.py
```

#### Rodar o dashboard:

```bash
streamlit run dashboard.py
```

---

## 📊 Funcionamento Geral

1. O sistema coleta logs armazenados no banco de dados MySQL.
2. Os logs são analisados pelo módulo `detectors.py` usando padrões de ataque.
3. Eventos suspeitos são classificados como alertas.
4. O dashboard exibe métricas e visualizações em tempo real.

---

## ⚠️ Observações

* Este projeto é um protótipo para fins educacionais.
* Pode ser expandido com machine learning, integração com APIs e monitoramento distribuído.

---

## 📌 Melhorias Futuras

* Integração com sistemas reais de logs (Syslog, APIs, etc.)
* Uso de IA para detecção de anomalias
* Sistema de notificações (Email, SMS, Webhooks)
* Controle de usuários e autenticação no dashboard

---

## 👨‍💻 Autor

Luiz Miguel de Toledo - [**https://www.linkedin.com/in/luiz-miguel-de-toledo-b35701351/**](https://www.linkedin.com/in/luiz-miguel-de-toledo-b35701351/)