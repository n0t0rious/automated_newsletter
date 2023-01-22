from fpdf import FPDF

PAGE_WIDTH = 220
PAGE_HEIGHT = 297


def generate_newsletter(content: dict):
    newsletter = FPDF()
    newsletter.add_page()
    newsletter.set_font('Courier', size=8)
    for story_num, text in content.items():
        newsletter.multi_cell(w=0, h=3, align='L', txt=f'{story_num + 1}. {text}')
        newsletter.ln(h=5)
    newsletter.output(name='test pdf.pdf')

