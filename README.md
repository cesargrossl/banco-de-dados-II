
# 🐳 Ambiente de Banco de Dados com Docker

Este projeto fornece um ambiente Docker pré-configurado com **MySQL**, **SQL Server** e **MongoDB** para facilitar testes, desenvolvimento e aprendizado.

## 🚀 Como iniciar o ambiente

Na pasta raiz do projeto, execute:

```sh
docker-compose up -d
```

Para parar e remover os containers, utilize:

```sh
docker-compose down
```

---

## 📦 Serviços Disponíveis

- **MySQL**
- **SQL Server**
- **MongoDB**

---

## 🐬 Conexão com o MySQL

![MySQL Logo](https://raw.githubusercontent.com/github/explore/main/topics/mysql/mysql.png)

- **Host:** `localhost`
- **Porta:** `3306`
- **Usuário:** `root`
- **Senha:** *(defina em seu docker-compose, se aplicável)*

Você pode usar ferramentas como **MySQL Workbench**, **DBeaver**, **HeidiSQL** ou qualquer cliente de sua preferência.

---

## 🖥️ Conexão com o SQL Server

![SQL Server Logo](https://raw.githubusercontent.com/github/explore/main/topics/sql-server/sql-server.png)

- **Host:** `localhost`
- **Porta:** `1433`
- **Usuário:** `sa`
- **Senha:** *(defina em seu docker-compose, se aplicável)*

Utilize clientes como **SQL Server Management Studio (SSMS)**, **Azure Data Studio** ou similares.

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

### 📑 Dica: Usando a extensão MongoDB para VS Code

1. Instale a extensão **MongoDB for VS Code**.
2. Abra a paleta de comandos (`Ctrl+Shift+P`) e pesquise por "MongoDB: Connect".
3. Cole a string de conexão acima para acessar o banco de dados direto pelo VS Code.

---

## 📚 Referências

- [Docker Compose Docs](https://docs.docker.com/compose/)
- [MySQL](https://www.mysql.com/)
- [SQL Server](https://www.microsoft.com/en-us/sql-server/)
- [MongoDB](https://www.mongodb.com/)

---

## ✨ Sugestões

- Altere as senhas padrão no arquivo `docker-compose.yml` para garantir segurança no seu ambiente.
- Se precisar expor para acesso externo, atente-se às portas configuradas.
- Para reiniciar os containers sem perder dados, use apenas `docker-compose restart`.

---

> Desenvolvido para facilitar seus estudos e experimentos com bancos de dados usando Docker.
