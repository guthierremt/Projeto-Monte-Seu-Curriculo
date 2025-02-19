from fpdf import FPDF
import io
import models.Cliente as cliente

def gerar_pdf(cliente):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Definir título
    pdf.set_font("Helvetica", size=16, style='B')
    pdf.cell(200, 10, txt=f"{cliente.nome}", ln=True, align='C')

    # Adicionando os dados pessoais
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"E-mail: {cliente.email}", ln=True)
    pdf.cell(200, 10, txt=f"Telefone: {cliente.telefone}", ln=True)
    pdf.cell(200, 10, txt=f"Data de Nascimento: {cliente.data_nascimento}", ln=True)

    # Adicionando formação acadêmica
    pdf.ln(10)
    pdf.cell(200, 10, txt="Formação Acadêmica:", ln=True)
    pdf.cell(200, 10, txt=f"Universidade: {cliente.universidade}", ln=True)
    pdf.cell(200, 10, txt=f"Curso: {cliente.curso}", ln=True)
    pdf.cell(200, 10, txt=f"Semestre Atual: {cliente.semestre}", ln=True)

    # Adicionando a experiência profissional e habilidades
    pdf.ln(10)
    pdf.cell(200, 10, txt="Experiência Profissional:", ln=True)
    pdf.multi_cell(0, 10, txt=cliente.experiencia)

    pdf.ln(10)
    pdf.cell(200, 10, txt="Descrição Pessoal:", ln=True)
    pdf.multi_cell(0, 10, txt=cliente.descricao)

    pdf.ln(10)
    pdf.cell(200, 10, txt="Competências:", ln=True)
    pdf.multi_cell(0, 10, txt=cliente.competencia)

    # Salvar PDF em um objeto em memória
    pdf_output = io.BytesIO()
    pdf_string = pdf.output(dest='S').encode('latin1')
    pdf_output.write(pdf_string)
    pdf_output.seek(0)

    return pdf_output.getvalue()

