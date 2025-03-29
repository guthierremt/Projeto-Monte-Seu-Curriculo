from services import database as db
import threading
import sqlite3

lock = threading.Lock()

def IncluirUsuario(cliente):
    try:
        count = db.cursor.execute("""
        INSERT INTO usuario (nome, telefone, email, endereco)
        VALUES (?,?,?,?)""",(cliente.dados["yourName"], cliente.dados["yourFone"], 
        cliente.dados["yourEmail"], cliente.dados["yourAdress"])).rowcount
        db.cnxn.commit()
        cliente.id_usuario = db.cursor.lastrowid
    except sqlite3.Error as e:
        print("Erro ao Inserir Usuario: {e}")
        return None

def IncluirFormacaoAcademica(cliente):
    try:
        count = db.cursor.execute("""
        INSERT INTO formacaoAcademica (instituicao, curso, anoConclusao, id_usuario)
        VALUES (?,?,?,?)""",(
        cliente.dados["yourUniversity"], cliente.dados["yourCourse"], cliente.dados["conclusionUniversity"], cliente.id_usuario)).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Formacao Academica: {e}")
        return None


def IncluirInfoProfissional(cliente):
    try:
        count = db.cursor.execute("""
        INSERT INTO profissional (empresa, tituloProfissional, cargoEmpresa, tempoEmpresa, descricaoAtv, id_usuario)
        VALUES (?,?,?,?,?,?)""",(
        cliente.dados["company"], cliente.dados["yourTitle"], cliente.dados["yourFunction"],
        cliente.dados["conclusionCompany"], cliente.dados["descriptionAtv"], cliente.id_usuario)).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Experiencia Profissional: {e}")
        return None

def IncluirModelo1(cliente):
    try:
        count = db.cursor.execute("""
        INSERT INTO modelo1 (infoFormacao, especializacao, infoPessoal, interessePessoal, linguas, id_usuario)
        VALUES (?,?,?,?,?,?)""",(
        cliente.dados["formationInfo"], cliente.dados["especialization"], cliente.dados["infoPerson"],
        cliente.dados["interPerson"], cliente.dados["languages"], cliente.id_usuario)).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Modelo 1: {e}")
        return None

def IncluirModelo2(cliente):
    try:
        count = db.cursor.execute("""
        INSERT INTO modelo2 (objetivos)
        VALUES (?)""",(
        cliente.dados["yourObjective"])).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Modelo 2: {e}")
        return None

def IncluirModelo3(cliente):
    try:
        count = db.cursor.execute("""
        INSERT INTO modelo3 (foto, objetivos, cursosTecnicos, qualificacaoProfissional)
        VALUES (?,?,?,?)""",(
        cliente.dados["yourPic"], cliente.dados["yourObjective"], cliente.dados["courseTecn"],
        cliente.dados["qualificationProfiss"])).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Modelo 3: {e}")
        return None




# def MostrarDados(cliente):
#     db.cursor.execute("SELECT * FROM Cliente")
    
#     columns = [index[0] for index in db.cursor.description]
#     lista = []
#     for i in db.cursor.fetchall():
#         dataDict = dict(zip(columns, i))
        
#         lista.append(cliente.Cliente(
#             nome = dataDict['nome'],
#             telefone = dataDict['telefone'],
#             data = dataDict['data_nascimento'],
#             email = dataDict['email'],
#             universidade = dataDict['universidade'],
#             curso = dataDict['curso'],
#             semestre = dataDict['semestre'],
#             experiencia = dataDict['experiencia'],
#             descricao = dataDict['descricao'],
#             competencia = dataDict['competencia']
#         ))
#     return lista

