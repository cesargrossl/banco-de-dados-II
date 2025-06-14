import sqlite3

# Caminho do banco de dados
conn = sqlite3.connect('db/sqlite/meubanco.sqlite')
cursor = conn.cursor()

# Criar tabela alunos
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (s
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT
)
''')

# Criar tabela cursos
cursor.execute('''
CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
)
''')

# Criar tabela de relacionamento (matriculas)
cursor.execute('''
CREATE TABLE IF NOT EXISTS matriculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
)
''')

# Inserir dados em alunos
cursor.execute("INSERT INTO alunos (nome, email) VALUES (?, ?)", ("João Silva", "joao@email.com"))
cursor.execute("INSERT INTO alunos (nome, email) VALUES (?, ?)", ("Maria Costa", "maria@email.com"))

# Inserir dados em cursos
cursor.execute("INSERT INTO cursos (nome, descricao) VALUES (?, ?)", ("Matemática", "Curso de matemática básica"))
cursor.execute("INSERT INTO cursos (nome, descricao) VALUES (?, ?)", ("Português", "Curso de português avançado"))

# Inserir dados em matriculas (relacionando alunos e cursos)
cursor.execute("INSERT INTO matriculas (aluno_id, curso_id) VALUES (?, ?)", (1, 1))  # João em Matemática
cursor.execute("INSERT INTO matriculas (aluno_id, curso_id) VALUES (?, ?)", (2, 2))  # Maria em Português

# Confirmar as alterações
conn.commit()

# Consultar dados de alunos
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()
print("Lista de alunos:")
for aluno in alunos:
    print(aluno)

# Consultar dados de cursos
cursor.execute("SELECT * FROM cursos")
cursos = cursor.fetchall()
print("\nLista de cursos:")
for curso in cursos:
    print(curso)

# Consultar dados de matriculas (relacionamento)
cursor.execute('''
SELECT alunos.nome, cursos.nome
FROM matriculas
JOIN alunos ON matriculas.aluno_id = alunos.id
JOIN cursos ON matriculas.curso_id = cursos.id
''')
matriculas = cursor.fetchall()
print("\nLista de matrículas (aluno, curso):")
for matricula in matriculas:
    print(matricula)

# Fechar conexão
conn.close()
