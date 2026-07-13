from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def render_pdf(title: str, markdown: str) -> bytes:
    output = BytesIO(); styles = getSampleStyleSheet()
    story = [Paragraph(title, styles['Title']), Spacer(1, 16)]
    for line in markdown.splitlines():
        if line.startswith('# '): story.append(Paragraph(line[2:], styles['Heading1']))
        elif line.startswith('## '): story.append(Paragraph(line[3:], styles['Heading2']))
        elif line: story.append(Paragraph(line.replace('&', '&amp;'), styles['BodyText']))
        story.append(Spacer(1, 5))
    SimpleDocTemplate(output, pagesize=letter, title=title).build(story)
    return output.getvalue()
