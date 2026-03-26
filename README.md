# Polls API - Django Tutorial

Um projeto prático desenvolvido para dominar os fundamentos do **Django** e do **Django REST Framework (DRF)**. O objetivo foi criar uma plataforma de enquetes onde é possível gerenciar perguntas e opções através de uma interface web e uma API robusta.

---

## O que este projeto faz?

- **Gestão de Enquetes:** Criação de perguntas e múltiplas opções de escolha.
- **API REST Profissional:** Endpoints para listar, criar e votar em enquetes.
- **Nested Serialization:** O grande diferencial! Permite criar uma pergunta e todas as suas opções em **um único envio de JSON**.
- **Painel Administrativo:** Interface completa para gerenciar os dados.

---

## Tecnologias Utilizadas

- **Python** 3.x
- **Django** (Web Framework)
- **Django REST Framework** (API Toolkit)
- **SQLite** (Banco de dados leve para desenvolvimento)

---

## Como rodar o projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/django-tuto.git
   cd django-tuto
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # .venv\Scripts\activate   # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install django djangorestframework
   ```

4. **Rode as migrações e inicie o servidor:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Acesse em: `http://127.0.0.1:8000/`

---

## Exemplos de uso da API

### Criar uma Enquete Completa (Nested JSON)
**Endpoint:** `POST /add/poll/` (ou sua rota de criação)

**Payload:**
```json
{
    "question_text": "Qual sua linguagem favorita?",
    "pub_date": "2026-03-26T10:00:00Z",
    "choices": [
        {"choice_text": "Python"},
        {"choice_text": "JavaScript"},
        {"choice_text": "Go"}
    ]
}
```

---
Desenvolvido com Python por Arthur 👋
