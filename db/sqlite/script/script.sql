import sqlite3

# Caminho do banco de dados
conn = sqlite3.connect('../db/sqlite/meubanco.sqlite')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT
)
''')

# Inserir dados
cursor.execute("INSERT INTO alunos (nome, email) VALUES (?, ?)", ("João Silva", "joao@email.com"))
cursor.execute("INSERT INTO alunos (nome, email) VALUES (?, ?)", ("Maria Costa", "maria@email.com"))

# Confirmar as alterações
conn.commit()

# Consultar dados
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()

print("Lista de alunos:")
for aluno in alunos:
    print(aluno)

# Fechar conexão
conn.close()
