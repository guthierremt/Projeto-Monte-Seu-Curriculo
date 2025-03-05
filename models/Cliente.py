class Cliente:
    # def __init__(self, nome=None, telefone= None, data=None, email=None, universidade=None, curso=None, semestre=None, experiencia=None, descricao=None, competencia=None):
    #     self.nome = nome
    #     self.telefone = telefone
    #     self.data = data
    #     self.email = email
    #     self.universidade = universidade
    #     self.curso = curso
    #     self.semestre = semestre
    #     self.experiencia = experiencia
    #     self.descricao = descricao
    #     self.competencia = competencia

    def modelo1(self, nome, titulo, telefone, endereco, email, objetivos, universidade, 
        curso, uniConclusao, infoFormacao, cargoEmpresa, empresa, empConclusao, descricaoAtv, idiomas, especializacao, infoPessoal, interPessoal):
        self.nome = nome
        self.titulo = titulo
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.objetivos = objetivos
        self.universidade = universidade
        self.curso = curso
        self.uniConclusao = uniConclusao
        self.infoFormacao = infoFormacao
        self.cargoEmpresa = cargoEmpresa
        self.empresa = empresa
        self.empConclusao = empConclusao
        self.descricaoAtv = descricaoAtv
        self.idiomas = idiomas
        self.especializacao = especializacao
        self.infoPessoal = infoPessoal
        self.interPessoal = interPessoal
        
    
    def modelo2(self, nome, titulo, telefone, email, objetivos, universidade, 
        curso, uniConclusao, cargoEmpresa, empresa, empConclusao, descricaoAtv):
        self.nome = nome
        self.titulo = titulo
        self.telefone = telefone
        self.email = email
        self.objetivos = objetivos
        self.universidade = universidade
        self.curso = curso
        self.uniConclusao = uniConclusao
        self.cargoEmpresa = cargoEmpresa
        self.empresa = empresa
        self.empConclusao = empConclusao
        self.descricaoAtv = descricaoAtv
    
    def modelo3(self, nome, telefone, email, endereco, objetivos,
        curso, uniConclusao, cargoEmpresa, empresa, empConclusao, descricaoAtv, cursosTecnicos, idiomas, qualificacaoProfi):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.objetivos = objetivos
        self.curso = curso
        self.uniConclusao = uniConclusao
        self.cargoEmpresa = cargoEmpresa
        self.empresa = empresa
        self.empConclusao = empConclusao
        self.descricaoAtv = descricaoAtv
        self.cursosTecnicos = cursosTecnicos
        self.idiomas = idiomas
        self.qualificacaoProfi = qualificacaoProfi
        