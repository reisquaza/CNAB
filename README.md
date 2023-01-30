# CNAB 

Um projeto que recebe um arquivo CNAB com dados de movimentações financeiras de lojas. </br></br>
A aplicação recebe o arquivo através de um formalário, formata os dados recebidos, armazena no banco de dados e depois renderiza uma tabela mostrando os dados renderizados

## Tecnologias

---

Lista das tecnologias utilizadas no projeto:

- [Django](https://www.djangoproject.com)
- [Technology name](https://www.django-rest-framework.org)
- [PostgreSQL](https://www.postgresql.org)

## Introdução

---

### 1. Crie seu ambiente virtual

```bash
python -m venv venv
```

### 2. Ative seu venv:

```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

### 3. Instale as dependencias

```bash
pip install -r requirements.txt
```

### 4. Executar localmente

- gerar as migrações

```
python manage.py migrate
```

- rodar o servidor local

```
python manage.py runserver
```
