"""Rebuild site/pages, site/thumbs and site/pages.json from a PDF exported from Canva.

usage: python3 scripts/make_pages.py path/to/export.pdf

Export the Canva design "Micah Social Writings" as PDF (Share > Download > PDF Standard),
run this, check the pages, then copy the PDF to site/book.pdf. Needs PyMuPDF and Pillow.
If the page count changes, update N in site/index.html.
"""
import json, os, sys
import pymupdf
from PIL import Image

WIDTH = 1800  # longest edge of each page image, in pixels
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, '..', 'site')


def main(pdf):
    doc = pymupdf.open(pdf)
    os.makedirs(os.path.join(SITE, 'pages'), exist_ok=True)
    os.makedirs(os.path.join(SITE, 'thumbs'), exist_ok=True)
    alts = []
    for i, page in enumerate(doc):
        zoom = WIDTH / page.rect.width
        pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
        im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        name = '%02d.jpg' % (i + 1)
        im.save(os.path.join(SITE, 'pages', name), quality=80, optimize=True, progressive=True)
        im.resize((360, round(360 * im.height / im.width)), Image.LANCZOS).save(
            os.path.join(SITE, 'thumbs', name), quality=75, optimize=True)
        text = ' '.join(page.get_text().split()) or 'A page of photographs.'
        alts.append('Page %d. %s' % (i + 1, text))
    with open(os.path.join(SITE, 'pages.json'), 'w') as f:
        json.dump(alts, f, ensure_ascii=False)
    print(len(alts), 'pages')


if __name__ == '__main__':
    main(sys.argv[1])
