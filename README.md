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
* **Bibliotecas Python:**
    * `mysql-connector-python`: Conexão com o banco de dados.
    * `streamlit`: Framework para o dashboard web.
    * `pandas`: Manipulação e tratamento dos dados de segurança.

---

## 🔧 Estrutura do Projeto

* `app.py`: Motor principal de detecção e monitoramento.
* `database.py`: Camada de persistência e conexão SQL.
* `detectors.py`: Lógica de processamento e regras de segurança.
* `dashboard.py`: Interface visual do sistema.

---

## 📋 Como Instalar e Rodar

### 1. Preparação do Ambiente
Certifique-se de que o MySQL está rodando (XAMPP) e crie o banco de dados `cyberwatch`.

### 2. Instalação de Dependências
Abra o terminal na pasta do projeto e execute:
```bash
pip install mysql-connector-python streamlit pandas