# Gere seu Currículo

Este projeto é uma aplicação desenvolvida utilizando Streamlit, que permite gerar currículos de forma prática e interativa. A aplicação coleta os dados inseridos pelo usuário diretamente no formulário e os utiliza para criar um currículo personalizado. Todas as informações são armazenadas no banco de dados SQLite.

### Bibliotecas usadas no Projeto
#### Streamlit 
Uma biblioteca em Python que facilita a criação de aplicativos web interativos, ideal para visualização de dados e prototipagem rápida.

#### SQLITE 
SQLite é um sistema de gerenciamento de banco de dados leve e integrado. Neste projeto, ele é usado para armazenar os dados fornecidos pelos usuários de forma eficiente e prática.

#### FPDF e REPORTLAB
Bibliotecas Python para criar documentos PDF.

# Alguns prints do projeto ⬇️

# Inicio

![image](https://github.com/user-attachments/assets/192a2084-a99b-4cf4-a032-493c11587a7a)


Na tela inicial, o usuário pode visualizar os modelos de currículos disponíveis e as características de cada um.

#### Logo abaixo há também um botão que leva diretamente à página de seleção de modelos.
![image](https://github.com/user-attachments/assets/39e60a94-02ad-49aa-80ec-e51f180bccb2)

# Seleção dos modelos

![image](https://github.com/user-attachments/assets/b6922847-465f-44c6-9c01-ea43d3626f94)

Nesta etapa, o usuário escolhe seu modelo de currículo preferido e é redirecionado para uma página onde pode preencher as informações necessárias.

# Preencher com as informações

![image](https://github.com/user-attachments/assets/58a2df12-b574-448e-b41a-daac9a9e691e)

Depois de preencher os campos com as informações pessoais, acadêmicas e profissionais, o usuário tem acesso ao botão para download do currículo gerado.

![image](https://github.com/user-attachments/assets/c5262b6e-b5d7-4aae-80c9-9cd98b922d6c)

## Exemplo de Perfil usando o Modelo 3
![image](https://github.com/user-attachments/assets/5f5ccfce-58b7-4641-8ed2-c66d4e2844c7)
## Como Executar o Projeto

Abra o terminal e execute os seguintes comandos:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
```
```bash
# Navegue até o diretório do projeto
cd seu-repositorio
```
```bash
# Instale as dependências
pip install -r requirements.txt
```
```bash
# Execute a aplicação
streamlit run app.py
```


---

### Se estiver com problemas em rodar o Streamlit com o comando acima, tente esse:
```bash

python -m streamlit run app.py
```



