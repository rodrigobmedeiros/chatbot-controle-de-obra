# Chatbot Controle de Obra

Chatbot para WhatsApp integrado com planilhas de custos de obra no Google Sheets.

## Arquitetura

```
┌──────────────┐       ┌─────────────┐       ┌──────────────────────────────┐       ┌──────────────┐
│              │       │             │       │                              │       │              │
│   WhatsApp   │◄─────►│   Twilio    │◄─────►│   Chatbot Controle de Obra   │◄─────►│ Google Sheets│
│   (usuário)  │       │  (webhook)  │       │        (aplicação)           │       │ (planilhas)  │
│              │       │             │       │                              │       │              │
└──────────────┘       └─────────────┘       └──────────────────────────────┘       └──────────────┘
```

**Fluxo:**
1. Usuário envia mensagem pelo **WhatsApp**
2. **Twilio** recebe e encaminha via webhook para a aplicação
3. **Chatbot** processa a mensagem e consulta/atualiza os dados no **Google Sheets**
4. Resposta volta pelo caminho inverso até o **WhatsApp** do usuário

## Requisitos

- Python 3.11
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
# Criar o ambiente virtual com Python 3.11
uv venv --python 3.11

# Ativar o ambiente virtual
source .venv/bin/activate

# Instalar dependências
uv pip install -r requirements.txt
```

## Configuração

Copie o arquivo de exemplo e preencha com suas credenciais:

```bash
cp .env_example .env
```

## Ferramentas de Qualidade

### Ruff (linting + formatting)

```bash
# Lint
ruff check .

# Lint com auto-fix
ruff check . --fix

# Formatar código
ruff format .
```

### mypy (type checking)

```bash
mypy .
```
