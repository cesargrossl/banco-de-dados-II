# 🐳 Ambiente de Bancos de Dados com Docker

Este projeto fornece um ambiente Docker pré-configurado com múltiplos **SGBDs** (MySQL, SQL Server, MongoDB, Oracle e PostgreSQL) para facilitar testes, desenvolvimento e aprendizado.

---

## 🚀 Como rodar o ambiente Docker

Na pasta raiz do projeto, execute:

```sh
docker compose up -d
```

Para parar e remover os containers:

```sh
docker compose down
```

> 💡 Você pode subir apenas um ou alguns serviços específicos:
>
> ```sh
> docker compose up -d mysql
> docker compose up -d postgres mongo
> ```

---

## 📦 Serviços Disponíveis

- 🐬 **MySQL 8.3**
- 🖥️ **SQL Server 2019**
- 🍃 **MongoDB 4.4**
- 🏛️ **Oracle XE 21c**
- 🐘 **PostgreSQL 16**

---

## 🐬 Conexão com o MySQL

![MySQL Logo](https://raw.githubusercontent.com/github/explore/main/topics/mysql/mysql.png)

- **Host:** `localhost`
- **Porta:** `3306`
- **Usuário:** `usuario` (ou `root`)
- **Senha:** `Cg5020@1223`
- **Banco padrão:** `meubanco`

Ferramentas recomendadas: **MySQL Workbench**, **DBeaver**, **HeidiSQL**.

---

## 🖥️ Conexão com o SQL Server

![SQL Server Logo](https://raw.githubusercontent.com/github/explore/main/topics/sql-server/sql-server.png)

- **Host:** `localhost`
- **Porta:** `1433`
- **Usuário:** `sa`
- **Senha:** `Cg5020@1223`

Ferramentas recomendadas: **SQL Server Management Studio (SSMS)**, **Azure Data Studio**.

---

## 🍃 Conexão com o MongoDB

![MongoDB Logo](https://raw.githubusercontent.com/github/explore/main/topics/mongodb/mongodb.png)

- **Host:** `localhost`
- **Porta:** `27017`
- **Usuário:** `root`
- **Senha:** `Cg5020@1223`
- **Auth Source:** `admin`

**String de conexão:**

```sh
mongodb://root:Cg5020%401223@localhost:27017/?authSource=admin
```

### 📑 Dica: Usando MongoDB no VS Code

1. Instale a extensão **MongoDB for VS Code**.
2. Abra a paleta de comandos (`Ctrl+Shift+P`) → "MongoDB: Connect".
3. Cole a string de conexão acima.

---

## 🏛️ Conexão com o Oracle XE

![Oracle Logo](https://raw.githubusercontent.com/github/explore/main/topics/oracle/oracle.png)

- **Host:** `localhost`
- **Porta:** `1521`
- **Usuário padrão:** `system`
- **Senha:** `Cg5020@1223`
- **Banco:** `meubanco`

Ferramentas recomendadas: **Oracle SQL Developer**, **DBeaver**.

---

## 🐘 Conexão com o PostgreSQL

![PostgreSQL Logo](https://raw.githubusercontent.com/github/explore/main/topics/postgresql/postgresql.png)

- **Host:** `localhost`
- **Porta:** `5432`
- **Usuário:** `usuario`
- **Senha:** `Cg5020@1223`
- **Banco padrão:** `meubanco`

Ferramentas recomendadas: **pgAdmin**, **DBeaver**, **TablePlus**.

---

## 📚 Referências

- [Documentação Docker Compose](https://docs.docker.com/compose/)
- [MySQL](https://www.mysql.com/)
- [SQL Server](https://www.microsoft.com/sql-server)
- [MongoDB](https://www.mongodb.com/)
- [Oracle XE](https://www.oracle.com/database/technologies/appdev/xe.html)
- [PostgreSQL](https://www.postgresql.org/)

---

## ✨ Boas práticas

- 🔑 Altere as senhas padrão no `docker-compose.yml` antes de uso em produção.
- 🔒 Restrinja o acesso às portas se for expor para rede externa.
- ♻️ Para reiniciar sem perder dados, use:
  ```sh
  docker compose restart
  ```

---

> 🛠️ Desenvolvido para apoiar estudos, testes e experimentos com diferentes bancos de dados em ambiente Docker.
