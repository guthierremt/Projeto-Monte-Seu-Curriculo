from fpdf import FPDF
import io
import models.Cliente as cliente

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from io import BytesIO

def gerarModelo1(cliente):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Definir título
    pdf.set_font("Helvetica", size=16, style='B')
    pdf.cell(200, 10, txt=f"{cliente.dados['yourName']}", ln=True, align='C')
    
    pdf.set_font("Helvetica", size=13)
    pdf.cell(200, 10, txt=f"Desenvolvedor Web", ln=True, align='C')
    
    # Criar estrutura de duas colunas
    left_x = 10
    right_x = 110
    start_y = 40

    pdf.set_font("Arial", size=12, style='B')
    pdf.set_xy(left_x, start_y)
    pdf.cell(90, 10, txt="INFORMAÇÕES PESSOAIS", ln=True)

    pdf.set_xy(right_x, start_y)
    pdf.cell(90, 10, txt="EXPERIÊNCIA PROFISSIONAL", ln=True)

    pdf.set_font("Arial", size=10)
    start_y += 10

    # Primeira coluna - Informações Pessoais
    pdf.set_xy(left_x, start_y)
    pdf.multi_cell(90, 6, txt=cliente.dados['infoPerson'], align='L')
    
    pdf.ln(5)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(90, 10, txt="ESPECIALIZAÇÕES", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(90, 6, txt=cliente.dados['especialization'])
    
    pdf.ln(5)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(90, 10, txt="ENTRE EM CONTATO COMIGO", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(90, 6, txt=f"E-mail: {cliente.dados['yourEmail']}\nTelefone: {cliente.dados['yourFone']}\nEndereço: {cliente.dados['yourAdress']}")

    pdf.ln(5)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(90, 10, txt="INTERESSES PESSOAIS", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(90, 6, txt=cliente.dados['interPerson'], align='L')

    # Segunda coluna - Experiência Profissional
    pdf.set_xy(right_x, start_y)
    
    pdf.set_font('Arial', style='B', size=11)
    pdf.cell(90, 6, txt=cliente.dados['yourFunction'], ln=1)
    pdf.set_font('Arial', size=9)
    pdf.set_x(right_x)
    pdf.cell(90, 6, txt=cliente.dados['company'], ln=1)
    pdf.set_font('Arial', size=8)
    pdf.set_x(right_x)
    pdf.multi_cell(90, 6, txt=f" - {cliente.dados['descriptionAtv']}")

    # Formação alinhada corretamente abaixo da experiência profissional
    pdf.ln(5)
    pdf.set_font("Arial", size=12, style='B')
    pdf.set_xy(right_x, pdf.get_y())
    pdf.cell(90, 10, txt="FORMAÇÃO", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.set_xy(right_x, pdf.get_y())
    pdf.multi_cell(90, 6, txt=f"{cliente.dados['yourUniversity']}\n{cliente.dados['yourCourse']}\n{cliente.dados['conclusionUniversity']}")

    # Salvar PDF em um objeto em memória
    pdf_output = io.BytesIO()
    pdf_string = pdf.output(dest='S').encode('latin1')
    pdf_output.write(pdf_string)
    pdf_output.seek(0)

    return pdf_output.getvalue()


def create_pdf(cliente):
    """
    Cria um PDF com base nos dados armazenados na instância da classe Cliente.

    :param cliente: Instância da classe Cliente contendo os dados do formulário.
    :return: Bytes do arquivo PDF.
    """
    buffer = BytesIO()  # Cria um buffer de memória para armazenar o PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Nome
    story.append(Paragraph(cliente.dados["yourName"], styles["Title"]))
    story.append(Spacer(1, 12))

    # Contato
    contact_info = f"Telefone: {cliente.dados['yourFone']} | Email: {cliente.dados['yourEmail']}"
    story.append(Paragraph(contact_info, styles["BodyText"]))
    story.append(Spacer(1, 12))

    # Objetivo
    story.append(Paragraph("OBJETIVOS", styles["Heading2"]))
    story.append(Paragraph(cliente.dados["yourObjective"], styles["BodyText"]))
    story.append(Spacer(1, 12))

    # Formação Acadêmica
    story.append(Paragraph("FORMAÇÃO", styles["Heading2"]))
    formation_info = f"{cliente.dados['conclusionUniversity']} | {cliente.dados['yourUniversity']} - {cliente.dados['yourCourse']}"
    story.append(Paragraph(formation_info, styles["BodyText"]))
    story.append(Spacer(1, 12))

    # Experiência Profissional
    story.append(Paragraph("EXPERIÊNCIAS", styles["Heading2"]))
    experience_info = f"{cliente.dados['conclusionCompany']} | {cliente.dados['company']} - {cliente.dados['yourTitle']}"
    story.append(Paragraph(experience_info, styles["BodyText"]))
    story.append(Paragraph(cliente.dados["yourFunction"], styles["BodyText"]))
    story.append(Paragraph(cliente.dados["descriptionAtv"], styles["BodyText"]))
    story.append(Spacer(1, 12))

    # Gera o PDF no buffer
    doc.build(story)
    buffer.seek(0)  # Volta para o início do buffer
    return buffer.getvalue()  # Retorna os bytes do PDF