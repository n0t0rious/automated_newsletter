from datetime import date
from fpdf import FPDF


def generate_newsletter(content: dict, directory: str = None):
    newsletter = FPDF()
    newsletter.add_page()
    newsletter.add_font("DejaVuSans", "", "/Users/gregflorea/PycharmProjects/automated_newsletter/newsletter_gen/DejaVuSans.ttf", uni=True)
    newsletter.set_font('DejaVuSans', size=8)
    # newsletter.set_font('Arial', size=8)
    for story_num, text in content.items():
        newsletter.multi_cell(
            w=0, h=3, align='L',
            txt=f'{story_num + 1}. {tuple(text.keys())[0]} {tuple(text.values())[0]}'
        )
        newsletter.ln(h=5)
    newsletter.output(f'{directory}/newsletter {date.today().strftime("%m-%d-%Y")}.pdf')
