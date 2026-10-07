# Security notes

This site shares its code with the new nccmn.org. The history below is about the old NCCMN WordPress site;
the same rules (static site, no admin login, two-factor everywhere) apply to EMM.

## What happened to the old site

The WordPress backup shows a classic SEO-spam compromise:

* `robots.txt` had been rewritten to list about 80 fake sitemaps (`sitemap4171.xml` to `sitemap4248.xml`
  plus `sitemap-index-1..8.xml`). This tells Google to crawl thousands of junk pages under your domain.
* The backup contains **249 junk folders** with random names (`Ictonyx`, `Lygodium`, `arthriticine-479541-…`,
  `agedly=10863&…`) holding **331 spam URLs**. When the backup was made these returned “page not found”,
  so the spam content itself had already been cleaned or blocked, but the URLs were still being advertised.
* A second, unrelated church site (`/LPCOG/`) was installed inside the same hosting account.
* The old site ran eight plugins (Jetpack, Ninja Forms, Form Maker, bbPress, Paid Memberships Pro,
  WP Courseware, WP e-Commerce, Gutenberg) and three themes. Several of these have had serious published
  vulnerabilities, and WP e-Commerce is abandoned. Any one of them, or a reused password, is a likely way in.

None of the old code, plugins, uploads or spam pages were carried into the new site. Only text and
PDF documents were reused, and every PDF was checked for embedded scripts (none found).

## Why the new site is safer

* **Nothing to hack on the server.** Plain HTML files: no database, no PHP, no plugins, no admin login.
* **Strict security headers** (`deploy/_headers`): a Content Security Policy that only allows the site's
  own scripts, styles and fonts (plus YouTube thumbnail images), blocks the site from being framed,
  forces HTTPS (HSTS), and turns off browser features the site doesn't use.
* **No third-party scripts.** No analytics, no tracking, no external fonts. The only script is a 20-line
  mobile-menu toggle, and the site works without it.
* **Forms without server code.** Contact and prayer forms are received by Netlify, with a hidden
  “honeypot” field that catches most spam bots. Forms ask people not to send confidential data.
* **Old WordPress paths** (`/wp-admin`, `/wp-login.php`, `/xmlrpc.php`, `/wp-content/…`) return “not found”.
* A clean `robots.txt` with one real sitemap.

## Clean-up checklist (do these once)

1. **Before shutting off the old hosting**, download any original files you still need (especially the
   PDFs listed in `README.md` under “Files that need originals”).
2. **Change every password** connected to the old site: hosting control panel, WordPress admins, FTP/SFTP,
   database, and any email account that shared a password. Assume they were exposed.
3. **Domain registrar:** turn on two-factor authentication and *registrar lock*; turn on DNSSEC if offered.
4. **Point DNS to Netlify**, confirm the new site loads over HTTPS, then **cancel the old WordPress hosting**
   so the compromised copy is gone for good.
5. **Google Search Console** (search.google.com/search-console):
   * Verify ownership of `nccmn.org`.
   * *Sitemaps*: remove the fake sitemaps if listed, submit `https://nccmn.org/sitemap.xml`.
   * *Security & Manual actions*: check for warnings and request a review if any appear.
   * *Removals*: the spam URLs now return 404 and will drop out on their own; use temporary removal
     for any that still show in search results.
6. **Email protection for the domain:** make sure SPF, DKIM and DMARC records exist for nccmn.org
   (your email provider gives the values). This stops others from sending email pretending to be you.
7. **Netlify account:** turn on two-factor authentication; only give access to people who need it.

## Keeping it safe

* Every 3–6 months: log in to Netlify and the registrar, check who has access, check the domain's
  renewal date, read any security notices.
* Only add outside scripts (chat widgets, analytics, donation embeds) if truly needed. Each one must also
  be added to the Content-Security-Policy in `deploy/_headers`, which is a good moment to ask whether it's
  worth it.
* Check headers after each major change at securityheaders.com and observatory.mozilla.org.
* Keep a copy of this folder (or the GitHub repository) as the backup. Restoring the site is just
  publishing the `site` folder again.
