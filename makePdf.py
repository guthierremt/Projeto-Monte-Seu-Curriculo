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
    pdf.multi_cell(90, 6, txt=cliente.descricao, align='L')
    
    pdf.ln(5)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(90, 10, txt="ESPECIALIZAÇÕES", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(90, 6, txt=cliente.competencia)
    
    pdf.ln(5)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(90, 10, txt="ENTRE EM CONTATO COMIGO", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(90, 6, txt=f"E-mail: {cliente.email}\nTelefone: {cliente.telefone}\nData de Nascimento: {cliente.data_nascimento}")

    pdf.ln(5)
    pdf.set_font("Arial", size=12, style='B')
    pdf.cell(90, 10, txt="INTERESSES PESSOAIS", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(90, 6, txt=cliente.descricao, align='L')

    # Segunda coluna - Experiência Profissional
    pdf.set_xy(right_x, start_y)
    pdf.multi_cell(90, 6, txt=cliente.experiencia)

    # Formação alinhada corretamente abaixo da experiência profissional
    pdf.ln(5)
    pdf.set_font("Arial", size=12, style='B')
    pdf.set_xy(right_x, pdf.get_y())
    pdf.cell(90, 10, txt="FORMAÇÃO", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.set_xy(right_x, pdf.get_y())
    pdf.multi_cell(90, 6, txt=f"{cliente.universidade}\n{cliente.curso}\n{cliente.semestre}")

    # Salvar PDF em um objeto em memória
    pdf_output = io.BytesIO()
    pdf_string = pdf.output(dest='S').encode('latin1')
    pdf_output.write(pdf_string)
    pdf_output.seek(0)

    return pdf_output.getvalue()
