# Projeto Integrador - Class01

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

    ### Instale as dependências do Django-Tailwind com o seguinte comando:
    
    ```bash
    python manage.py tailwind install
    ```

    ### Agora construa toda a estilização do site usando o Tailwind CSS

    ```bash
    python manage.py tailwind build
    ```

    ### Agora seu projeto está pronto para ser visualizado, só falta iniciar o servidor local

    ```bash
    python manage.py runserver
    ```

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

### URL's

As urls do projeto Django servem para conectar os links e retornar a visualização referente à aquela `URL`, dependendo do projeto se ele tiver vários apps as urls podem serem maiores e para facilitar na busca do usuário e identificação em possíveis manutenções dos desenvolvedores.




## Desenvolvido por: Arthur Rodrigues