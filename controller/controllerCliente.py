import services.database as db

def IncluirDados(cliente):
    count = db.cursor.execute("""
    INSERT INTO Cliente (nome, telefone, data_nascimento, email, universidade, 
    curso, semestre, experiencia, descricao, competencia)
    VALUES (?,?,?,?,?,?,?,?,?,?)""",
    cliente.nome, cliente.telefone, cliente.data_nascimento, cliente.email,
    cliente.universidade, cliente.curso, cliente.semestre, cliente.experiencia, cliente.descricao, cliente.competencia).rowcount
    db.cnxn.commit()

def MostrarDados(cliente):
    db.cursor.execute("SELECT * FROM Cliente")
    
    columns = [index[0] for index in db.cursor.description]
    lista = []
    for i in db.cursor.fetchall():
        dataDict = dict(zip(columns, i))
        
        lista.append(cliente.Cliente(
            nome = dataDict['nome'],
            telefone = dataDict['telefone'],
            data = dataDict['data_nascimento'],
            email = dataDict['email'],
            universidade = dataDict['universidade'],
            curso = dataDict['curso'],
            semestre = dataDict['semestre'],
            experiencia = dataDict['experiencia'],
            descricao = dataDict['descricao'],
            competencia = dataDict['competencia']
        ))
    return lista

