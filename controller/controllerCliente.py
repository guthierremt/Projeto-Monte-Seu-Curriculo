from services import database as db
import threading
import sqlite3

lock = threading.Lock()

def IncludeUser(cliente):
    try:
        db.cursor.execute("""
        INSERT INTO usuario (nome, telefone, email, endereco)
        VALUES (?,?,?,?)""",(cliente.dados["yourName"], cliente.dados["yourFone"], 
        cliente.dados["yourEmail"], cliente.dados["yourAdress"])).rowcount
        db.cnxn.commit()
        cliente.id_usuario = db.cursor.lastrowid
    except sqlite3.Error as e:
        print("Erro ao Inserir Usuario: {e}")
        return None

def IncludeEducation(cliente):
    try:
        db.cursor.execute("""
        INSERT INTO formacaoAcademica (instituicao, curso, anoConclusao, id_usuario)
        VALUES (?,?,?,?)""",(
        cliente.dados["yourUniversity"], cliente.dados["yourCourse"], cliente.dados["conclusionUniversity"], cliente.id_usuario)).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Formacao Academica: {e}")
        return None


def IncludeInfoProfessional(cliente):
    try:
        db.cursor.execute("""
        INSERT INTO profissional (empresa, tituloProfissional, cargoEmpresa, tempoEmpresa, descricaoAtv, id_usuario)
        VALUES (?,?,?,?,?,?)""",(
        cliente.dados["company"], cliente.dados["yourTitle"], cliente.dados["yourFunction"],
        cliente.dados["conclusionCompany"], cliente.dados["descriptionAtv"], cliente.id_usuario)).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Experiencia Profissional: {e}")
        return None

def IncludeModel1(cliente):
    try:
        db.cursor.execute("""
        INSERT INTO modelo1 (infoFormacao, especializacao, infoPessoal, interessePessoal, linguas, id_usuario)
        VALUES (?,?,?,?,?,?)""",(
        cliente.dados["formationInfo"], cliente.dados["especialization"], cliente.dados["infoPerson"],
        cliente.dados["interPerson"], cliente.dados["languages"], cliente.id_usuario)).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Modelo 1: {e}")
        return None

def IncludeModel2(cliente):
    try:
        db.cursor.execute("""
        INSERT INTO modelo2 (objetivos, id_usuario)
        VALUES (?, ?)""",(
        cliente.dados["yourObjective"], cliente.id_usuario)).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print("Erro ao Inserir Modelo 2: {e}")
        return None

def IncludeModel3(cliente):
    try:
        path = "images/profile_circular.png"
        db.cursor.execute("""
        INSERT INTO modelo3 (foto, objetivos, cursosTecnicos, qualificacaoProfissional, id_usuario)
        VALUES (?,?,?,?, ?)""",(
        path, cliente.dados["yourObjective"], cliente.dados["courseTecn"],
        cliente.dados["qualificationProfiss"], cliente.id_usuario)).rowcount
        db.cnxn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao Inserir Modelo 3: {e}")
        return None


