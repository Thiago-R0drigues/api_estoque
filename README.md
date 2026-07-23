# API de Estoque

Sistema de controle de estoque com CRUD completo, desenvolvido para aprendizado prático de backend com FastAPI.

## Tecnologias

- **Backend:** FastAPI, SQLAlchemy 2.0, SQLite
- **Frontend:** React (Vite)

## Funcionalidades

- Cadastro, listagem, edição e exclusão de produtos
- Validação de dados com Pydantic
- Documentação automática da API (Swagger)

## Como rodar

### Backend
\`\`\`bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`

### Frontend
\`\`\`bash
cd frontend-estoque
npm install
npm run dev
\`\`\`

A API sobe em `http://127.0.0.1:8000` (documentação em `/docs`) e o frontend em `http://localhost:5173`.