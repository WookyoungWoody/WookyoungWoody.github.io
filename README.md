# wookyoungwoody.github.io — Academic Portfolio of Wookyoung Kim

I am a Senior Researcher at the Heat Pump Research Center, [Korea Institute of Machinery and Materials (KIMM)](https://www.kimm.re.kr), specializing in thermal engineering. I hold a Ph.D. in Mechanical Engineering from [KAIST](https://www.kaist.ac.kr) (2021), advised by [Prof. Sung Jin Kim](https://scholar.google.com/citations?user=1YqQxnkAAAAJ). My research focuses on thermal systems—including data center cooling (immersion and direct liquid cooling), high-heat-flux electronics cooling, compact heat exchangers (PCHE), heat pump systems, and two-phase heat transfer phenomena.

This repository hosts my academic portfolio at **[https://wookyoungwoody.github.io](https://wookyoungwoody.github.io)**, powered by the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## Site Structure

- **Publications** – Peer-reviewed papers and conference contributions managed via [`_bibliography/papers.bib`](/_bibliography/papers.bib) and rendered through [jekyll-scholar](https://github.com/inukshuk/jekyll-scholar)
- **CV** – Single-source resume data in [`assets/json/resume.json`](/assets/json/resume.json), rendered at [`/cv/`](https://wookyoungwoody.github.io/cv/)
- **Projects** – Research and software projects: data center cooling, heat pump systems, PCHE design, and software tools in [`_projects/`](/_projects)
- **Repositories** – GitHub statistics and links to public repositories

## Local Development

Use Docker Compose for a quick local development environment:

```bash
# Initial setup and start the dev server
docker compose pull && docker compose up

# Site runs at http://localhost:8080
```

After rebuilding dependencies or the Dockerfile:

```bash
docker compose up --build
```

To stop containers and free port 8080:

```bash
docker compose down
```

**Before every commit**, format all files with Prettier:

```bash
# First time only
npm install --save-dev prettier @shopify/prettier-plugin-liquid

# Format all files
npx prettier . --write
```

See [AGENTS.md](AGENTS.md) for detailed development instructions, code-specific guidelines, and troubleshooting.

## Deployment

The site deploys automatically via GitHub Actions:

- Push changes to the `main` branch
- [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) builds and deploys to GitHub Pages
- Live site: [https://wookyoungwoody.github.io](https://wookyoungwoody.github.io)

Citation counts are automatically updated via the `update-citations` workflow.

## Credits

This site is built with the [al-folio](https://github.com/alshedivat/al-folio) v0.16.3 Jekyll theme, released under the [MIT License](https://github.com/alshedivat/al-folio/blob/main/LICENSE). **al-folio** was originally based on the [\*folio theme](https://github.com/bogoli/-folio) by [Lia Bogoev](https://liabogoev.com).
