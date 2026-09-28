# I've Gripped the Phantom

Micah Bielert's book of social posts and poetry (June 28, 1986 – March 8, 2025), put together by Rae in Canva and re-hosted here as a page-turning reader.

Live at https://micah-bielert.netlify.app (Netlify project `micah-bielert`).

- `site/` is the published site and nothing else: `index.html` (the reader), `pages/` (one image per page), `thumbs/` (the All pages grid), `pages.json` (each page's words, for screen readers), and `book.pdf` (the full export, for Save the PDF).
- The source is the Canva design "Micah Social Writings" (87 pages, 11 × 8.5 in landscape). To update the book, edit it in Canva, export a PDF, and run `python3 scripts/make_pages.py export.pdf`, then replace `site/book.pdf`.
- Links: `#44` opens page 44.
- The site asks search engines not to list it (`<meta name="robots" content="noindex">` in `index.html`). Remove that line to let people find it by searching.
- No build step, no trackers, no accounts. Keep this repo private.
