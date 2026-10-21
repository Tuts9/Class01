# Class01 — Trilhas para quem está começando a programar

Case de portfólio: plataforma em português que ajuda iniciantes a **escolher uma trilha**, explorar tópicos e **acompanhar o progresso**.

**Problema:** quem chega na área se perde em tutoriais aleatórios.  
**Solução:** roadmaps guiados (Fundamentos + Frontend), biblioteca de tópicos/ferramentas e conta com progresso salvo.

## Stack

- Python 3.12 + **Django 4.2**
- **Tailwind CSS** (django-tailwind)
- SQLite (local) / PostgreSQL (produção via `DATABASE_URL`)
- WhiteNoise + Gunicorn

## Funcionalidades

- Trilhas com etapas ordenadas (roadmap)
- Conta (registro/login) e marcação de progresso
- Catálogo de tópicos com busca e filtros
- Ferramentas recomendadas por tópico
- Formulário de suporte + acessibilidade (VLibras, contraste, fonte)

## Como rodar localmente

```bash
git clone https://github.com/Tuts9/Class01.git
cd Class01

uv venv .venv --python 3.12
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

uv pip install -r requirements.txt
copy .env.example .env   # ou cp .env.example .env

cd class01
python manage.py migrate
python manage.py seed_demo
python manage.py tailwind install
python manage.py tailwind build
python manage.py runserver
```

Em desenvolvimento no Windows, use o script que **sempre rebuilda o Tailwind** antes de subir o server:

```powershell
.\scripts\dev.ps1
```

Sempre que criar templates/classes novas, rode `python manage.py tailwind build` (ou o script acima). O CSS antigo em `theme/static/css/dist/` não inclui utilitários novos até o rebuild.

Abra http://127.0.0.1:8000/

## Demo / deploy (Render)

Arquivos prontos: `render.yaml`, `build.sh`, `Procfile`, `runtime.txt`.

1. Faça push deste repositório para o GitHub
2. Em [Render Dashboard](https://dashboard.render.com) → **New** → **Blueprint**
3. Selecione o repo e confirme o `render.yaml` (web + Postgres free)
4. Após o primeiro deploy, ajuste as env vars:
   - `ALLOWED_HOSTS` = `seu-servico.onrender.com`
   - `CSRF_TRUSTED_ORIGINS` = `https://seu-servico.onrender.com`
5. O `build.sh` já roda `migrate`, `collectstatic` e `seed_demo`

Sem conta Render no ambiente de CI local, o deploy precisa ser disparado uma vez pelo painel (ou Deploy Hook).

## Estrutura

```
Class01/
├── class01/           # projeto Django (manage.py)
│   ├── home/          # app principal (tópicos, trilhas, auth)
│   ├── theme/         # Tailwind
│   └── media/         # uploads
├── assets-p.i/        # assets de conteúdo (seed)
├── requirements.txt
├── render.yaml
└── build.sh
```

## Comandos úteis

```bash
python manage.py seed_demo   # trilhas + ferramentas demo
python manage.py test home   # testes
python manage.py createsuperuser
```

## Autor

Arthur Rodrigues — projeto originado no Projeto Integrador (ADS), reativado como case de portfólio com trilhas e progresso.
