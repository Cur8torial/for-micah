# Remembering Micah Bielert

Micah Bielert, June 28, 1986 – March 8, 2025. A memorial page kept by Rae (his cousin) for the family, and his book of social posts and poetry, *I've Gripped the Phantom*, which Rae put together in Canva.

Live at https://micah-bielert.netlify.app (Netlify project `micah-bielert`, linked to `main`).

- `site/` is the published site and nothing else:
  - `index.html` lays out the memorial page; `content.js` holds everything about Micah it shows (name, dates, tributes, the book, photos, videos, loved ones). To change the words, edit `content.js`. The family's tributes are kept exactly as they wrote them.
  - `photos/` are the photos from his Keeper memorial, re-saved without any hidden metadata; `videos/` are its four videos.
  - `book/` is the book reader: `index.html`, `pages/` (one image per page), `thumbs/` (the All pages grid), `pages.json` (each page's words, for screen readers), and `book.pdf` (the full export, for Save the PDF). Old links like `/#44` are sent on to `/book/#44`.
- The source is the Canva design "Micah Social Writings" (87 pages, 11 × 8.5 in landscape). To update the book, edit it in Canva, export a PDF, and run `python3 scripts/make_pages.py export.pdf`, then replace `site/book.pdf`.
- Links: `/book/#44` opens page 44 of the book; `#tributes`, `#book`, `#photos`, `#videos` and `#loved` open those parts of the page.
- The site asks search engines not to list it (`<meta name="robots" content="noindex">` in `index.html`). Remove that line to let people find it by searching.
- No build step, no trackers, no accounts. Keep this repo private.
