#!/usr/bin/env python3
"""Generate the public CV from the exact records rendered by Jekyll."""
import hashlib
import json
from pathlib import Path
from xml.sax.saxutils import escape

import reportlab
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak, HRFlowable

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'site/_data/cv.json'
OUTPUT = ROOT / 'site/assets/pdf/Zeyi_Li_CV.pdf'
cv = json.loads(SOURCE.read_text())
fonts = Path(reportlab.__file__).parent / 'fonts'
pdfmetrics.registerFont(TTFont('Body', str(fonts / 'Vera.ttf')))
pdfmetrics.registerFont(TTFont('BodyBold', str(fonts / 'VeraBd.ttf')))
ink, muted, accent = '#23271f', '#535a4f', '#91402d'
styles = {
    'name': ParagraphStyle('name', fontName='Times-Roman', fontSize=35, leading=39, textColor=colors.HexColor(ink)),
    'brand': ParagraphStyle('brand', fontName='Body', fontSize=10, leading=16, textColor=colors.HexColor(accent)),
    'summary': ParagraphStyle('summary', fontName='Body', fontSize=9.1, leading=14, textColor=colors.HexColor(muted), spaceAfter=12),
    'section': ParagraphStyle('section', fontName='BodyBold', fontSize=8, leading=13, textColor=colors.HexColor(accent), spaceBefore=17, spaceAfter=10),
    'entry': ParagraphStyle('entry', fontName='BodyBold', fontSize=10, leading=14, textColor=colors.HexColor(ink), spaceBefore=5),
    'meta': ParagraphStyle('meta', fontName='Body', fontSize=8.1, leading=12, textColor=colors.HexColor(muted), spaceAfter=5),
    'bullet': ParagraphStyle('bullet', fontName='Body', fontSize=8.5, leading=12.5, textColor=colors.HexColor(ink), leftIndent=10, firstLineIndent=-8, spaceAfter=4),
}
story = []
def p(text, style):
    return Paragraph(escape(text), styles[style])

story += [p(cv['name'], 'name'), p(cv['title'], 'brand'), Spacer(1, 8), p(cv['summary'], 'summary')]
story += [p('  |  '.join(c['value'] for c in cv['contacts']), 'meta')]
for section in cv['sections']:
    if section['id'] == 'projects':
        story += [PageBreak(), p(cv['name'], 'name'), p('SELECTED EVENTS, PROJECTS & WRITING', 'brand'), Spacer(1, 6)]
    story += [p(section['title'].upper(), 'section'), HRFlowable(width='100%', thickness=.4, color=colors.HexColor('#b9bcae')), Spacer(1, 7)]
    for entry in section['entries']:
        block = [p(entry['title'], 'entry'), p(entry['role'] + '  |  ' + entry['period'], 'meta')]
        block += [p('• ' + bullet, 'bullet') for bullet in entry['bullets']]
        story += [KeepTogether(block), Spacer(1, 7)]
story += [p('INTERESTS', 'section'), p(' · '.join(cv['interests']), 'summary')]

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#b9bcae'))
    canvas.line(44, 36, A4[0] - 44, 36)
    canvas.setFont('Body', 7)
    canvas.setFillColor(colors.HexColor(muted))
    canvas.drawString(44, 23, 'ZEYILEO  /  ' + cv['updated'])
    canvas.drawRightString(A4[0] - 44, 23, f'{doc.page} / 2')
    canvas.restoreState()

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=44, leftMargin=44, topMargin=38, bottomMargin=48,
                        title='Zeyi Li — Curriculum Vitae', author='Zeyi Li',
                        subject='CV source SHA256: ' + hashlib.sha256(SOURCE.read_bytes()).hexdigest())
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
