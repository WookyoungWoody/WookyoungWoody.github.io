# Archived: Kami CV

The Kami-styled CV (`/cv/html/`, `/cv/standalone.html`, `assets/pdf/cv_WKIM.pdf`)
was retired from the site in October 2026. Files keep their original repo-relative
paths under this folder. Jekyll skips `_archive/`, so nothing here is built or served.

To restore, move each file back to its original path, re-add `cv_html: /cv/html/`
to `_pages/cv.md` together with the `{% if page.cv_html %}` icon link that
`_layouts/cv.liquid` carried before this archive commit, and restore `_pages/cv_dropdown.md` (then set `nav: false` on
`_pages/cv.md` again).
