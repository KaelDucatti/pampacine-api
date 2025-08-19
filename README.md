# pampacine-api

API RESTful para gerenciamento de filmes, gêneros, atores e avaliações, desenvolvida com Django, Django REST Framework e outras ferramentas.

## Índice

- [Introdução](#introdução)
- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Instalação e Configuração](#instalação-e-configuração)
- [Execução](#execução)
- [Endpoints Principais](#endpoints-principais)
- [Autenticação e Segurança](#autenticação-e-segurança)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

Esta documentação descreve a API do projeto **pampacine-api**, que permite o gerenciamento de conteúdos relacionados a filmes, gêneros, atores e avaliações, oferecendo uma estrutura robusta para aplicações web e mobile.

## Visão Geral

O **pampacine-api** é uma API para cadastro e consulta de filmes, gêneros, atores e avaliações, com endpoints RESTful, pronta para ser utilizada em aplicações web ou mobile.

## Funcionalidades

- CRUD completo de filmes, gêneros, atores, nacionalidades e avaliações.
- Suporte a filtros, buscas e paginação em endpoints.
- Interface administrativa integrada com Django Admin.
- Estrutura modular preparada para escalabilidade e manutenção.

## Tecnologias

- **Django**: Framework web robusto e escalável.
- **Django REST Framework**: Ferramenta poderosa para criação de APIs RESTful.
- **SQLite/PostgreSQL**: Banco de dados para persistência de dados.
- **Python 3.13**: Linguagem de programação de alto nível.

## Instalação e Configuração

1. Clone o repositório:
    ```sh
    git clone https://github.com/KaelDucatti/pampacine-api.git
    cd pampacine-api
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Realize as migrações:
    ```sh
    python manage.py migrate
    ```

5. (Opcional) Crie um superusuário para acessar o Django Admin:
    ```sh
    python manage.py createsuperuser
    ```

## Execução

Inicie o servidor de desenvolvimento:
```sh
python manage.py runserver
```
Acesse a interface administrativa em: [http://localhost:8000/admin/](http://localhost:8000/admin/).

## Endpoints Principais

A API está acessível pelo prefixo `/api/v1/`. Exemplos de endpoints:

- **Filmes**
    - `GET    /api/v1/movies/` — Lista filmes
    - `POST   /api/v1/movies/` — Cria filme
    - `GET    /api/v1/movies/<id>/` — Detalha filme
    - `PUT    /api/v1/movies/<id>/` — Atualiza filme
    - `DELETE /api/v1/movies/<id>/` — Remove filme

- **Gêneros**
    - `GET    /api/v1/genres/`
    - `POST   /api/v1/genres/`
    - `GET    /api/v1/genres/<id>/`
    - `PUT/PATCH/DELETE /api/v1/genres/<id>/`

- **Atores**
    - `GET    /api/v1/actors/`
    - `POST   /api/v1/actors/`
    - `GET    /api/v1/actors/<id>/`
    - `PUT/PATCH/DELETE /api/v1/actors/<id>/`

- **Nacionalidades**
    - `GET    /api/v1/nationality/`
    - `POST   /api/v1/nationality/`
    - `GET    /api/v1/nationality/<id>/`
    - `PUT/PATCH/DELETE /api/v1/nationality/<id>/`

- **Avaliações**
    - `GET    /api/v1/reviews/`
    - `POST   /api/v1/reviews/`
    - `GET    /api/v1/reviews/<id>/`
    - `PUT/PATCH/DELETE /api/v1/reviews/<id>/`

## Autenticação e Segurança

Atualmente, os endpoints públicos não exigem autenticação. Para áreas restritas, implemente mecanismos de autenticação e autorização no arquivo [`config/settings.py`](config/settings.py).

## Testes

Execute os testes automatizados para garantir o funcionamento da API:
```sh
python manage.py test
```

## Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Realize os commits necessários (`git commit -am 'Adiciona nova feature'`).
4. Envie sua branch para o repositório (`git push origin feature/nova-feature`).
5. Abra um Pull Request com uma descrição das alterações.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [`static/admin/img/LICENSE`](static/admin/img/LICENSE) para mais informações.
