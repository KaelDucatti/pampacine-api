# pampacine-api

API RESTful para gerenciamento de filmes, gêneros, atores e avaliações, desenvolvida com Django e Django REST Framework.

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Endpoints Principais](#endpoints-principais)
- [Autenticação](#autenticação)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Visão Geral

O **pampacine-api** é uma API para cadastro e consulta de filmes, gêneros, atores e avaliações, com endpoints RESTful, pronta para ser utilizada em aplicações web ou mobile.

## Funcionalidades

- CRUD de filmes, gêneros, atores e nacionalidades
- Cadastro e consulta de avaliações de filmes
- Filtros e buscas nos principais recursos
- Estrutura modular e escalável

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/pampacine-api.git
    cd pampacine-api
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Configuração

1. Configure as variáveis de ambiente no arquivo [`config/settings.py`](config/settings.py), especialmente as informações do banco de dados PostgreSQL.
2. Realize as migrações:
    ```sh
    python manage.py migrate
    ```

3. (Opcional) Crie um superusuário:
    ```sh
    python manage.py createsuperuser
    ```

## Execução

Para rodar o servidor de desenvolvimento:

```sh
python manage.py runserver
```

Acesse a documentação administrativa em `http://localhost:8000/admin/`.

## Endpoints Principais

A API está disponível sob o prefixo `/api/v1/`. Exemplos de endpoints:

- **Filmes**
    - `GET /api/v1/movies/` — Lista filmes
    - `POST /api/v1/movies/` — Cria filme
    - `GET /api/v1/movies/<id>/` — Detalha filme
    - `PUT/PATCH/DELETE /api/v1/movies/<id>/` — Atualiza/Remove filme

- **Gêneros**
    - `GET /api/v1/genres/`
    - `POST /api/v1/genres/`
    - `GET /api/v1/genres/<id>/`
    - `PUT/PATCH/DELETE /api/v1/genres/<id>/`

- **Atores**
    - `GET /api/v1/actors/`
    - `POST /api/v1/actors/`
    - `GET /api/v1/actors/<id>/`
    - `PUT/PATCH/DELETE /api/v1/actors/<id>/`

- **Nacionalidades**
    - `GET /api/v1/nationality/`
    - `POST /api/v1/nationality/`
    - `GET /api/v1/nationality/<id>/`
    - `PUT/PATCH/DELETE /api/v1/nationality/<id>/`

- **Avaliações**
    - `GET /api/v1/reviews/`
    - `POST /api/v1/reviews/`
    - `GET /api/v1/reviews/<id>/`
    - `PUT/PATCH/DELETE /api/v1/reviews/<id>/`

## Autenticação

Atualmente, a API não exige autenticação para acesso aos endpoints públicos. Para proteger endpoints, configure autenticação no [`config/settings.py`](config/settings.py) conforme necessário.

## Testes

Execute os testes automatizados com:

```sh
python manage.py test
```

## Contribuição

Contribuições são bem-vindas! Siga os passos:

1. Fork este repositório
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [`static/admin/img/LICENSE`](static/admin/img/LICENSE) para mais detalhes.
