from fpdf import FPDF
import io
import models.Cliente as cliente

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import Image

class HorizontalLine(Flowable):
    def __init__(self, width, thickness=1, color=black):
        self.width = width
        self.thickness = thickness
        self.color = color
        self.height = thickness  # A altura da linha é igual à sua espessura

    def draw(self):
        self.canv.setLineWidth(self.thickness)
        self.canv.setStrokeColor(self.color)
        self.canv.line(0, 0, self.width, 0)

    def wrap(self, *args):
        """
        Método obrigatório para Flowable.
        Retorna a largura e a altura da linha.
        """
        return self.width, self.height

# Adicionando as linhas horizontais
line_width = 6 * inch  # Largura da linha (ajuste conforme necessário)
line_thickness = 1  # Espessura da linha


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

    # Definindo estilos personalizados
    styles.add(ParagraphStyle(name='NameStyle', fontSize=34, leading=30, alignment=TA_LEFT, fontName='Helvetica-Bold', spaceAfter=6))
    styles.add(ParagraphStyle(name='TitleStyle', fontSize=14, leading=18, alignment=TA_LEFT, fontName='Helvetica-Bold', spaceAfter=12))
    styles.add(ParagraphStyle(name='ContactStyle', fontSize=12, leading=12, alignment=TA_LEFT, fontName='Helvetica', spaceAfter=12))
    styles.add(ParagraphStyle(name='SectionTitle', fontSize=12, leading=14, alignment=TA_LEFT, fontName='Helvetica-Bold', spaceBefore=12, spaceAfter=6))
    styles.add(ParagraphStyle(name='CustomBodyText', fontSize=10, leading=12, alignment=TA_LEFT, fontName='Helvetica', spaceAfter=6))  # Nome alterado para evitar conflito

    story = []

    # Nome (yourName)
    story.append(Paragraph(cliente.dados["yourName"], styles["NameStyle"]))
    story.append(Spacer(1, 6))

    # Título Profissional (yourTitle)
    story.append(Paragraph(cliente.dados["yourTitle"], styles["TitleStyle"]))
    story.append(Spacer(1, 2))

    # Linha horizontal acima do contato
    story.append(HorizontalLine(line_width, line_thickness))  # Usando o estilo personalizado
    story.append(Spacer(1, 16))

    phone_icon_path = "images/phone.png"
    email_icon_path = "images/email.png"
    icon_size =12
    contact_info = f"""
    <img src="{phone_icon_path}" width="{icon_size}" height="{icon_size}" valign="middle"/> {cliente.dados['yourFone']} | 
    <img src="{email_icon_path}" width="{icon_size}" height="{icon_size}" valign="middle"/> {cliente.dados['yourEmail']}
    """
    story.append(Spacer(1, 2))
    story.append(Paragraph(contact_info, styles["ContactStyle"]))
    story.append(Spacer(1, 6))

    # Linha horizontal abaixo do contato
    story.append(HorizontalLine(line_width, line_thickness))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Objetivo (yourObjective)
    story.append(Paragraph("OBJETIVOS", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["yourObjective"], styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Formação Acadêmica
    story.append(Paragraph("FORMAÇÃO", styles["SectionTitle"]))
    formation_info = f"<b>{cliente.dados['conclusionUniversity']}</b> | {cliente.dados['yourUniversity']} - {cliente.dados['yourCourse']}"
    story.append(Paragraph(formation_info, styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Experiência Profissional
    story.append(Paragraph("EXPERIÊNCIAS", styles["SectionTitle"]))
    experience_info = f"<b>{cliente.dados['conclusionCompany']}</b> | {cliente.dados['company']} - {cliente.dados['yourTitle']}"
    story.append(Paragraph(experience_info, styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Paragraph(cliente.dados["yourFunction"], styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Paragraph(cliente.dados["descriptionAtv"], styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Gera o PDF no buffer
    doc.build(story)
    buffer.seek(0)  # Volta para o início do buffer
    return buffer.getvalue()  # Retorna os bytes do PDF


def create_pdf_modelo3(cliente):
    """
    Cria um PDF com base no modelo 3, utilizando os dados da instância da classe Cliente.

    :param cliente: Instância da classe Cliente contendo os dados do formulário.
    :return: Bytes do arquivo PDF.
    """
    buffer = BytesIO()  # Cria um buffer de memória para armazenar o PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Definindo estilos personalizados
    styles.add(ParagraphStyle(
        name='PicStyle',
        fontSize=22,
        leading=22,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold',
        spaceAfter=0,
    ))
    styles.add(ParagraphStyle(
        name='TitleStyle',
        fontSize=22,
        leading=22,
        alignment=TA_RIGHT,
        leftIndent=40,
        fontName='Helvetica-Bold',
        spaceBefore=-20
    ))
    styles.add(ParagraphStyle(
        name='SubtitleStyle',
        fontSize=12,
        leading=20,
        alignment=TA_RIGHT,
        fontName='Helvetica',
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name='SectionTitle',
        fontSize=16,
        leading=14,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold',
        spaceBefore=12,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        name='CustomBodyText',  # Nome alterado para evitar conflito
        fontSize=10,
        leading=12,
        alignment=TA_LEFT,
        fontName='Helvetica',
        spaceAfter=6
    ))

    story = []

    phonePath2 = "images/phone-call.png"
    emailPath2 = "images/email2.png"
    addresPath = "images/navigation.png"
    iconSize = 12

    imagePatch = "images/profile.jpg"
    imageSize =180
    
    imageInfo = f"""
    <img src="{imagePatch}" width="{imageSize}" height="{imageSize}" valign="top"/> 
    """
    story.append(Paragraph(imageInfo, styles["PicStyle"]))
    # Nome (yourName)
    story.append(Spacer(1, -20))
    story.append(Paragraph(cliente.dados["yourName"], styles["TitleStyle"]))
    story.append(Spacer(1, 14))

    iconInfo = f"""
    {cliente.dados['yourAdress']} <img src="{addresPath}" width="{iconSize}" height="{iconSize}" valign="middle"/><br/>
    {cliente.dados['yourEmail']} <img src="{emailPath2}" width="{iconSize}" height="{iconSize}" valign="middle"/><br/>
    {cliente.dados['yourFone']} <img src="{phonePath2}" width="{iconSize}" height="{iconSize}" valign="middle"/><br/>
    """
    story.append(Spacer(1, 2))
    story.append(Paragraph(iconInfo, styles["SubtitleStyle"]))
    story.append(Spacer(1, 70))

    # Linha horizontal
    story.append(Paragraph("<hr/>", styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Objetivo (yourObjective)
    story.append(Paragraph("Objetivo", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["yourObjective"], styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Qualificação Profissional (yourQualification)
    story.append(Paragraph("Qualificação Profissional", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["qualificationProfiss"], styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Experiência Profissional (yourExperience)
    story.append(Paragraph("Experiência Profissional", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["yourExperience"], styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Formação (yourEducation)
    story.append(Paragraph("Formação", styles["SectionTitle"]))
    formation_info = f"<b>{cliente.dados['conclusionUniversity']}</b> | {cliente.dados['yourCourse']}"  # Usando o estilo personalizado
    story.append(Paragraph(formation_info, styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    # Cursos Adicionais (yourCourses)
    story.append(Paragraph("Cursos Adicionais", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["courseTecn"], styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Idiomas (yourLanguages)
    story.append(Paragraph("Idiomas", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["languages"], styles["CustomBodyText"]))  # Usando o estilo personalizado
    story.append(Spacer(1, 12))

    # Gera o PDF no buffer
    doc.build(story)
    buffer.seek(0)  # Volta para o início do buffer
    return buffer.getvalue()  # Retorna os bytes do PDF