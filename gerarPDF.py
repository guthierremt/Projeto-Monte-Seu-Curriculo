# Cria um PDF com base no modelo 3, utilizando os dados da instância da classe Cliente.
# Parametro cliente: Instância da classe Cliente contendo os dados do formulário.

from fpdf import FPDF
import io
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import Image
from PIL import Image, ImageDraw, ImageOps


# Linha para o modelo1
class HorizontalLine(Flowable):
    def __init__(self, width, thickness=1, color=black):
        self.width = width
        self.thickness = thickness
        self.color = color
        self.height = thickness

    def draw(self):
        self.canv.setLineWidth(self.thickness)
        self.canv.setStrokeColor(self.color)
        self.canv.line(0, 0, self.width, 0)

    def wrap(self, *args):
        return self.width, self.height

line_width = 6 * inch
line_thickness = 1


# Separando os nomes pegando somente os dois primeiros
def splitName(cliente):
    name = cliente.dados["yourName"]
    partes = name.split(" ")
    firstName = " ".join(partes[:2])
    
    return firstName
    

def generateModel1(cliente):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.ln(20)
    # Definindo Nome
    pdf.set_font("Helvetica", size=24, style='B')
    pdf.cell(200, 10, txt=f"{cliente.dados["yourName"]}", ln=True, align='C')
    
    pdf.set_font("Helvetica", size=13)
    pdf.cell(200, 10, txt=f"Desenvolvedor Web", ln=True, align='C')
    
    # Estrutura de duas colunas
    left_x = 10
    right_x = 110
    start_y = 60


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
    
    pdf.ln(10)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(90, 10, txt="ESPECIALIZAÇÕES", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(90, 6, txt=cliente.dados['especialization'])
    
    pdf.ln(10)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(90, 10, txt="ENTRE EM CONTATO COMIGO", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(90, 6, txt=f"E-mail: {cliente.dados['yourEmail']}\nTelefone: {cliente.dados['yourFone']}\nEndereço: {cliente.dados['yourAdress']}")

    pdf.ln(10)
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

    pdf.ln(10)
    pdf.set_font("Arial", size=12, style='B')
    pdf.set_xy(right_x, pdf.get_y())
    pdf.cell(90, 10, txt="FORMAÇÃO", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.set_xy(right_x, pdf.get_y())
    pdf.multi_cell(90, 6, txt=f"{cliente.dados['yourUniversity']}\n{cliente.dados['yourCourse']}\n{cliente.dados['conclusionUniversity']}")

    # Salvando o PDF em um objeto em memória
    pdf_output = io.BytesIO()
    pdf_string = pdf.output(dest='S').encode('latin1')
    pdf_output.write(pdf_string)
    pdf_output.seek(0)

    return pdf_output.getvalue()


def generateModel2(cliente):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Definindo estilos personalizados
    styles.add(ParagraphStyle(name='NameStyle', fontSize=34, leading=30, alignment=TA_LEFT, fontName='Helvetica-Bold', spaceAfter=6))
    styles.add(ParagraphStyle(name='TitleStyle', fontSize=14, leading=18, alignment=TA_LEFT, fontName='Helvetica-Bold', spaceAfter=12))
    styles.add(ParagraphStyle(name='ContactStyle', fontSize=12, leading=12, alignment=TA_LEFT, fontName='Helvetica', spaceAfter=12))
    styles.add(ParagraphStyle(name='SectionTitle', fontSize=12, leading=14, alignment=TA_LEFT, fontName='Helvetica-Bold', spaceBefore=12, spaceAfter=6))
    styles.add(ParagraphStyle(name='CustomBodyText', fontSize=10, leading=12, alignment=TA_LEFT, fontName='Helvetica', spaceAfter=6))

    story = []

    # Definindo Nome
    story.append(Paragraph(splitName(cliente), styles["NameStyle"]))
    story.append(Spacer(1, 6))

    # Título Profissional
    story.append(Paragraph(cliente.dados["yourTitle"], styles["TitleStyle"]))
    story.append(Spacer(1, 2))

    # Linha horizontal acima do contato
    story.append(HorizontalLine(line_width, line_thickness))
    story.append(Spacer(1, 16))

    phone_icon_path = "images/phone.png"
    email_icon_path = "images/email.png"
    icon_size = 12
    contact_info = f"""
    <img src="{phone_icon_path}" width="{icon_size}" height="{icon_size}" valign="middle"/> {cliente.dados['yourFone']} | 
    <img src="{email_icon_path}" width="{icon_size}" height="{icon_size}" valign="middle"/> {cliente.dados['yourEmail']}
    """
    story.append(Spacer(1, 2))
    story.append(Paragraph(contact_info, styles["ContactStyle"]))
    story.append(Spacer(1, 6))

    # Linha horizontal abaixo do contato
    story.append(HorizontalLine(line_width, line_thickness))
    story.append(Spacer(1, 12))

    # Objetivo
    story.append(Paragraph("OBJETIVOS", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["yourObjective"], styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    # Formação Acadêmica
    story.append(Paragraph("FORMAÇÃO", styles["SectionTitle"]))
    formation_info = f"<b>{cliente.dados['conclusionUniversity']}</b> | {cliente.dados['yourUniversity']} - {cliente.dados['yourCourse']}"
    story.append(Paragraph(formation_info, styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    # Experiência Profissional
    story.append(Paragraph("EXPERIÊNCIAS", styles["SectionTitle"]))
    experience_info = f"<b>{cliente.dados['conclusionCompany']}</b> | {cliente.dados['company']} - {cliente.dados['yourTitle']}"
    story.append(Paragraph(experience_info, styles["CustomBodyText"]))
    story.append(Paragraph(cliente.dados["yourFunction"], styles["CustomBodyText"]))
    story.append(Paragraph(cliente.dados["descriptionAtv"], styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

# Função pra criar a imagem circular
def createCircularImage(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")

    size = min(img.size)
    img = img.resize((size, size), Image.LANCZOS)

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    circular_image = Image.new("RGBA", (size, size))
    circular_image.paste(img, (0, 0), mask)

    circular_image.save(output_path, format="PNG")

def generateModel3(cliente):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

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
        name='CustomBodyText',
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

    output_path = "images/profile_circular.png"
    createCircularImage(cliente.dados["yourPic"], output_path)

    imagePatch = output_path
    imageSize =180
    
    imageInfo = f"""
    <img src="{imagePatch}" width="{imageSize}" height="{imageSize}" valign="top"/> 
    """
    story.append(Paragraph(imageInfo, styles["PicStyle"]))
    # Nome (yourName)
    story.append(Spacer(1, 10))
    story.append(Paragraph(splitName(cliente), styles["TitleStyle"]))
    story.append(Spacer(1, 14))

    iconInfo = f"""
    {cliente.dados['yourAdress']} <img src="{addresPath}" width="{iconSize}" height="{iconSize}" valign="middle"/><br/>
    {cliente.dados['yourEmail']} <img src="{emailPath2}" width="{iconSize}" height="{iconSize}" valign="middle"/><br/>
    {cliente.dados['yourFone']} <img src="{phonePath2}" width="{iconSize}" height="{iconSize}" valign="middle"/><br/>
    """
    story.append(Spacer(1, 2))
    story.append(Paragraph(iconInfo, styles["SubtitleStyle"]))
    story.append(Spacer(1, 50))

    
    story.append(Paragraph("<hr/>", styles["CustomBodyText"]))
    story.append(Spacer(1, 2))

    # Objetivo
    story.append(Paragraph("Objetivo", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["yourObjective"], styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    # Qualificação Profissional
    story.append(Paragraph("Qualificação Profissional", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["qualificationProfiss"], styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    # Experiência Profissional
    story.append(Paragraph("Experiência Profissional", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["yourFunction"], styles["CustomBodyText"]))
    story.append(Paragraph(cliente.dados["company"], styles["CustomBodyText"]))
    story.append(Paragraph(cliente.dados["conclusionCompany"], styles["CustomBodyText"]))
    story.append(Paragraph(cliente.dados["descriptionAtv"], styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    # Formação
    story.append(Paragraph("Formação", styles["SectionTitle"]))
    formation_info = f"<b>{cliente.dados['conclusionUniversity']}</b> | {cliente.dados['yourCourse']}"
    story.append(Paragraph(formation_info, styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    # Cursos Adicionais
    story.append(Paragraph("Cursos Adicionais", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["courseTecn"], styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    # Idiomas
    story.append(Paragraph("Idiomas", styles["SectionTitle"]))
    story.append(Paragraph(cliente.dados["languages"], styles["CustomBodyText"]))
    story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()