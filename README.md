# Projeto Integrador - Class01

## O Projeto
Aplicação Web Class01

## Desenvolvedor responsável
Arthur Rodrigues

## Introdução

- ### Visão geral do projeto

    O Class01 é uma aplicação que foi desenvolvido com a principal ideia de ajudar as pessoas que querem começar na área de programação e ainda não sabem como fazer para dar o primeiro passo. Dentro do site será possível encontrar tópicos desde diagramas até linguagens de programação e suas principais bibliotecas.

- ### Funcionalidades principais

    O Class01 tem como funcionalidade principal entregar uma breve descrição sobre cada tópico e redireciona o usuário para uma página especifíca onde ele pode se aprofundar no assunto.
    
    Logo em seguida são apresentadas algumas das 3 principais ferramentas daquele tópico e também com um botão de redirecionamento para a página principal daquela ferramenta onde o usuário poderá saber mais sobre a ferramenta e até mesmo começar a usá-la.

- ### Tecnologias utilizadas

    Nesse projeto as principais tecnologias utizadas foram Django para a construção de todo o backend e Tailwind CSS para criação das estilizações das páginas.

    Todas as linguagens que estão sendo utilizadas são: HTML, CSS, JavaScript, Python

    Também foram utilizados alguns frameworks, como: Django, e Tailwind CSS.

- ### Público alvo

    Os principais usuários do Class01 serão os iniciantes na área de programação que ainda não sabem por onde começar e querem aprender o básico e ter um guia inicial.

## Instalação e configuração (Clonando o repositório do Github)

- ## Requisitos

    Certifique-se de que tenha os seguintes requisitos instalados em seu sistema
    
    - Python (versões a partir da 3.x)
    - Node.js (versões a partir da 18.x)
    - Outras dependências listadas no `requirements.txt`

- ## Instalação

    ### Clone o repositório

    ```bash
    git clone https://github.com/Tuts9/Projeto-Integrador.git
    ```

    ### Acesse a pasta com o terminal e crie um ambiente virtual

    ```bash
    python -m venv .venv
    ```

    ### Ative seu ambiente virtual

    ```bash
    .venv\Scripts\activate
    ```

    ### Instale todas as dependências com o requirements.txt

    ```bash
    pip install -r requirements.txt
    ```

    ### Após a instalação entre na pasta seguinte

    ```bash
    cd class01
    ```

    ### Em seguida realize as migrações para configurar o banco de dados

    ```bash
    python manage.py migrate
    ```

    ### Agora construa toda a estilização do site usando o Tailwind CSS

    ```bash
    python manage.py tailwind build
    ```

    ### Agora seu projeto está pronto para ser visualizado, só falta iniciar o servidor local

    ```bash
    python manage.py runserver
    ```

## Instalação e configuração (Criando seu próprio projeto)

- ## Requisitos

    Certifique-se de que tenha os seguintes requisitos instalados em seu sistema
    
    - Python (versões a partir da 3.x)

- ## Crie seu próprio projeto

    ### Dentro do seu computador crie uma pasta com o nome do seu projeto

    ### Com seu editor de código aberto prepare o ambiente de desenvolvimento crie um ambiente virtual

    ```bash
    python -m venv .venv
    ```

    ### Logo em seguida ative seu ambiente virtual

    ```bash
    .venv\Scripts\activate
    ```

    ### Instale o Django dentro do seu ambiente

    ```bash
    pip install django
    ```

    ### Já com o Django instalado crie o projeto com o seguinte comando

    ```bash
    django-admin startproject myproject
    ```

    ### Em seguida entre na pasta do projeto

    ```bash
    cd class01
    ```

    ### Crie o app do seu projeto

    ```bash
    python manage.py startapp myapp
    ```

    ### Teste a sua aplicação no 'localhost'

    ```bash
    python manage.py runserver
    ```

    ### Criando as migrações do banco de dados

    ```bash
    python manage.py makemigrations
    ```

    ### Aplique as migrações para o banco de dados

    ```bash
    python manage.py migrate
    ```

    ### Crie um super usuário para acesso ao painel de administrador

    ```bash
    python manage.py createsuperuser
    ```

    ### Finalização

    Para continuar o desenvolvimento do seu projeto consulte a documentação oficial do Django, também disponível em PT-BR, e construa seu projeto do seu jeito. [Django Docs](https://docs.djangoproject.com/pt-br/5.0/intro/tutorial01/)

## Estrutura do projeto

### Arquitetura MVT

- No projeto Class01 foi utilizado a arquitetura MVT (Models, Views, Templates)
    - Models: Mapeamento do banco de dados para o projeto, usando a ORM do Django para facilitar o uso do banco de dados da preferência do desenvolvedor.
    - Views: Lógica de negócio. É aqui que determinamos o que irá acontecer em nosso projeto, onde acontece a conexão das funções, envios de formulários e apresentação de dados nas interfaces, tudo estando linkado com as urls referentes. Essa é a parte do lado do servidor
    - Templates: Pasta do projeto em que ficam os arquivos HTML que renderizam toda a visualização para os usuários. Este é a parte do lado do cliente.

### Arquivos estáticos

- Também existe a pasta dos arquivos estáticos, onde ficam todos os arquivos que são importados nas páginas como imagens, arquivos de estilização e arquivos de scripts.

### Framework CSS (opcional)

- No caso de projetos usando Tailwind CSS, caso esteja usando o módulo de Python `django-tailwind` também será possível encontrar uma pasta chamada `themes` que é onde ficam todos os arquivos de configuração do Tailwind CSS que por sua vez usa também o `Node.js`.

## Configuração Django

### Arquivo 'settings.py'
- Em `Static_URL = 'static/'`, vamos criar o `static_Root`. Inserir abaixo: `static_Root = os.path.join(BASE_DIR, 'staticfiles)`. Importe a biblioteca no início do código: `import os`.
- No tópico templates TEMPLATES no arquivo settings.py, insira: Na linha `dirs['templates]`.
- Após criar o seu app adicione o nome do seu app em `INSTALLED_APPS`.
- Configure a linguagem do projeto para PT-BR como padrão, em `LANGUAGE_CODE` adicione `'pt-br'`,
e em `TIME_ZONE` adicione `'America/Sao_Paulo'`.

### URL's

As urls do projeto Django servem para conectar os links e retornar a visualização referente à aquela `URL`, dependendo do projeto se ele tiver vários apps as urls podem serem maiores e para facilitar na busca do usuário e identificação em possíveis manutenções dos desenvolvedores.