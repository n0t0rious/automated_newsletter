from fpdf import FPDF

PAGE_WIDTH = 220
PAGE_HEIGHT = 297

contents = {1: 'Jan 20 (Reuters) - Federal prosecutors have seized nearly $700 million in assets from FTX founder Sam '
               'Bankman-Fried in January, largely in the form of Robinhood stock, according to a Friday court filing. '
               'Bankman-Fried, who has been accused of stealing billions of dollars from FTX customers to pay debts '
               'incurred by his crypto-focused hedge fund, has pleaded not guilty to fraud charges. He is scheduled '
               'to face trial in October.'}


def generate_newsletter(content: dict):
    newsletter = FPDF()
    newsletter.add_page()
    newsletter.set_font('Courier', size=8)
    for story_num, text in content.items():
        newsletter.multi_cell(w=0, h=3, align='L', txt=f'{story_num + 1}. {text}')
        newsletter.ln(h=5)
    newsletter.output(name='test pdf.pdf')

