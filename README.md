# treinamento
🐳 Docker Image com ambiente Mysql, Sql Server e MongoDB

Estando dentro da pasta raíz ou via terminal do VSCode, execute o comando abaixo:

```sh
docker-compose up -d
```

Para parar o container, use:

```sh
docker-compose down
```

---

## Conectar 🐬 MySQL

![MySQL Logo](https://raw.githubusercontent.com/github/explore/main/topics/mysql/mysql.png)

Com ferramenta de manipulação como (Workbench, DBeaver...)

- **Host:** `localhost`
- **Port:** `3306`
- **User:** `root`

---

## Conectar 🖥️ SQL Server

![SQL Server Logo](https://raw.githubusercontent.com/github/explore/main/topics/sql-server/sql-server.png)

Com ferramenta de manipulação como (Microsoft SQL Server Management Studio...)

- **Host:** `localhost`
- **User:** `sa`

---

## Conectar 🍃 MongoDB

![MongoDB Logo](https://raw.githubusercontent.com/github/explore/main/topics/mongodb/mongodb.png)

Você pode conectar ao MongoDB usando a string de conexão abaixo:

```
mongodb://root:Cg5020%401223@localhost:27017/?authSource=admin
```

### Usando a extensão MongoDB para VS Code

1. Instale a extensão **MongoDB for VS Code** no marketplace do VS Code.
2. Abra a paleta de comandos (`Ctrl+Shift+P`) e procure por "MongoDB: Connect".
3. Cole a string de conexão acima para acessar o banco de dados diretamente pelo VS Code.

---
