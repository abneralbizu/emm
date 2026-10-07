# EMM website

A bilingual (Spanish first, English second) static website for
Excelencia en la Administración del Ministerio / Excellence Ministry Management (EMM),
formerly the Red Nacional de Iglesias y Ministerios Cristianos / National Christian Churches & Ministries Network (NCCMN).

It is built from the same code as the new NCCMN site, which replaced an old WordPress site that had
been hacked (see `SECURITY.md`).

## Logo

The mark is a stone arch held together by a gold keystone that carries a cross: the keystone is the
stone that locks an arch in place, the way sound administration holds a ministry together.

* `brand/` – logo files to use elsewhere (letterhead, email signature, social media):
  English and Spanish versions, light and dark, plus the mark alone as SVG and an app icon.
* `tools/emm_mark.py` draws the mark; `python3 tools/make_icons.py` regenerates every logo file,
  icon and the social-sharing image from it.
* Colors: spruce `#14403C`, keystone gold `#B8862B` (light `#D9A846`), bronze for buttons `#8F5F14`.
* Typefaces: Literata (EMM, headings) and Libre Franklin (name line, text).

## Still to decide for EMM

* **Web address.** Pages still use nccmn.org for links, emails and the sitemap. When EMM has its own
  domain, change `SITE_URL` in `build.py` and the emails in `content/data.py`.
* **Legal name.** Checks and the Give page use `legal_name` in `content/data.py`
  (National Christian Churches and Ministries Network, Inc.). Change it once the name change or DBA is filed.
* **Donation link** still points to the NCCMN invoice page.
* PDFs (membership application, retirement plan, CRECE) still carry the NCCMN name inside.
There is no database, no PHP, no plugins and no admin login on the server, so there is nothing for
an attacker to log into or exploit. The site is plain HTML files.

---

## Folder guide

| Folder / file | What it is |
|---|---|
| `site/` | **The finished website.** This is the only folder that gets published. Don't edit it by hand; it is rebuilt every time. |
| `templates/es/` | Spanish pages, one file per page (`about.html` = Nosotros, `churches.html` = Servicios para iglesias…). |
| `templates/en/` | The same pages in English. |
| `templates/base.html` | Header, menu, footer and language switch shared by every page. |
| `content/data.py` | Lists used in several places: contact info, leaders, affiliated churches, documents, videos, articles. |
| `content/articles/` | The text of each reflection/blog post. |
| `static/` | CSS, fonts, logo, PDFs. Copied into `site/` as-is. |
| `static/documents/` | Downloadable PDFs. Keep the same file names so old links keep working. |
| `deploy/_headers` | Security headers sent with every page. |
| `deploy/_redirects` | Sends old WordPress addresses to the matching new page. |
| `netlify.toml` | Hosting settings for Netlify. |

## Looking at the site on your computer

Open `preview/index.html` in Chrome or Safari. The `preview` folder is a copy of the site with links
that work straight from disk (`python3 build.py --preview` regenerates it). The forms and PDF downloads only work
once the site is on Netlify (the PDFs are left out of `preview` to keep it small).

## Making a change

1. Edit the file (for example, a phone number lives in `content/data.py` under `ORG`).
2. Rebuild: `pip install jinja2` (first time only), then `python3 build.py`
3. The build stops and lists the problem if any internal link is broken.
4. Publish (see below).

Common edits:

* **Contact details, donation link, emails** – `content/data.py`, `ORG` and `LEADERS`.
* **Add an affiliated church** – `content/data.py`, `AFFILIATES`.
* **Add a PDF** – put it in `static/documents/`, then add an entry to `ADMIN_DOCS` or `CRECE_DOCS`.
* **Add a video** – add a line to the right collection in `VIDEO_COLLECTIONS` (the YouTube id is the part after `watch?v=`).
* **Add a reflection** – save the body as `content/articles/<name>.html`, then add an entry to `ARTICLES`.
* **Change page text** – edit `templates/es/<page>.html` and the matching `templates/en/<page>.html`.

## GitHub and the preview address

The project lives in a GitHub repository. Every change pushed to the `main` branch runs
`.github/workflows/preview.yml`, which rebuilds the site and publishes a preview to GitHub Pages at
`https://<account>.github.io/<repository>/`. The preview is marked "noindex" so Google ignores it.

GitHub Pages is only the preview. It can't receive the contact and prayer forms or send the security
headers, so the public site at nccmn.org should be served by Netlify connected to this same repository
(Option B below).

One-time setup in the repository: *Settings → Pages → Build and deployment → Source: GitHub Actions*.

## Publishing (Netlify, free plan)

Netlify was chosen because it hosts static sites free, adds HTTPS automatically, applies the
security headers in `_headers`, and receives the contact and prayer forms without any server code.

**Option A – simplest (drag and drop)**
1. Create an account at netlify.com and turn on two-factor authentication (User settings → Security).
2. Go to *Sites → Add new site → Deploy manually* and drag the `site` folder onto the page.
3. To update later, rebuild and drag the new `site` folder onto the site's *Deploys* tab.

**Option B – automatic (recommended once someone maintains it)**
1. Put this whole folder in a private GitHub repository.
2. In Netlify, *Add new site → Import from Git*, pick the repository. `netlify.toml` already tells
   Netlify how to build. Every change pushed to GitHub publishes itself.

**Then, in both cases:**
1. *Domain management → Add a domain* → `nccmn.org` (and `www.nccmn.org`). Netlify shows the DNS
   records to set at the domain registrar. HTTPS is issued automatically after DNS updates.
2. *Forms* → enable form detection, then *Form notifications* → email to `info@nccmn.org`.
   Two forms will appear after the first deploy: `contact` and `prayer`.
3. Visit `https://nccmn.org/contacto/`, send a test message, confirm the email arrives.

Cloudflare Pages also works (it reads the same `_headers` and `_redirects` files), but its free plan
has no built-in form handling; you would need to connect the forms to a service such as Formspree.

## Before going live: please confirm

These came from the 2021 version of the old NCCMN site and may be out of date:

* Phone (407-759-9003) and fax (321-445-9900) – `ORG` in `content/data.py` (the Winter Springs and New York addresses were confirmed in October 2026)
* Public email `info@nccmn.org` and `apply@nccmn.org` actually receive mail
* Leaders and their emails – `LEADERS`
* The online donation link (`https://go.payinvoice.com/nccmn/`, from the old “Blessings” page)
* The list of affiliated churches is still current
* New copy written for this rebuild: the “Nuestra razón de ser / Why we exist” section on the About page,
  the How-to-join steps, the privacy policy and the Give page. Everything else is the old site's wording,
  lightly edited.
* The old 501(c)(3) page quoted IRS fines of “$25,000 per claim / $75,000”. Those figures were removed
  because they could not be verified; the page now speaks of penalties in general terms.
* “Have You Noticed?” (2014) is an opinion piece touching on the Ferguson shooting and politics. It was
  carried over because it was published on the old site; remove it from `ARTICLES` if it no longer fits.

## Files that need originals

The backup tool stopped downloading at 1 MB, so these PDFs arrived cut off and are **not** on the new
site. If you have the originals, put them in `static/documents/` (same names) and add them to the lists
in `content/data.py`. The full list is `MISSING_DOCS` in `content/data.py`; the most important are the
Cash Management Procedure, *Un momento para mayordomía*, and the reopening guide.
The Cine Foro presentations were not in the backup at all; the page invites churches to request them.
