import database as db

db.cursor.execute('''
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL,
    endereco TEXT NOT NULL
        )
''')

db.cursor.execute('''
CREATE TABLE IF NOT EXISTS formacaoAcademica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    instituicao TEXT NOT NULL,
    curso TEXT NOT NULL,
    anoConclusao TEXT NOT NULL,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE ON UPDATE CASCADE
        )
''')


db.cursor.execute('''
CREATE TABLE IF NOT EXISTS profissional (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa TEXT NOT NULL,
    tituloProfissional TEXT NOT NULL,
    cargoEmpresa TEXT NOT NULL,
    tempoEmpresa TEXT NOT NULL,
    descricaoAtv TEXT NOT NULL,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE ON UPDATE CASCADE
        )
''')


db.cursor.execute('''
CREATE TABLE IF NOT EXISTS modelo1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    infoFormacao TEXT NOT NULL,
    especializacao TEXT NOT NULL,
    infoPessoal TEXT NOT NULL,
    interessePessoal TEXT NOT NULL,
    linguas TEXT NOT NULL,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE ON UPDATE CASCADE
        )
''')


db.cursor.execute('''
CREATE TABLE IF NOT EXISTS modelo2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    objetivos TEXT NOT NULL,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE ON UPDATE CASCADE
        )
''')

db.cursor.execute('''
CREATE TABLE IF NOT EXISTS modelo3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    foto TEXT NOT NULL,
    objetivos TEXT NOT NULL,
    cursosTecnicos TEXT NOT NULL,
    qualificacaoProfissional TEXT NOT NULL,
    id_usuario INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id) ON DELETE CASCADE ON UPDATE CASCADE
        )
''')
