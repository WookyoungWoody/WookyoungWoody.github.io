# CV Documents

Binder of CV evidence (papers, patents, software registrations, degree
certificates). The repo is **public** (GitHub Pages), so this folder
is split:

| Subfolder | Tracked in git? | Reason |
|---|---|---|
| `papers/` | yes (public) | Author's own peer-reviewed publications |
| `patents/` | no — local only | Korean patent docs include inventor signatures & internal IDs |
| `software/` | no — local only | KIMM internal S-codes in software registration PDFs |
| `degrees/` | no — local only | Personal identifiers on degree certificates |

The split is enforced in the repo `.gitignore` (`cv_documents/*` then
allow-list `papers/` + this README).

## Layout

```
cv_documents/
├── papers/              # tracked
│   ├── sci/             # SCI (international, peer-reviewed) — 11 PDFs + JCI/JIF screenshots
│   └── kci/             # KCI (Korean, peer-reviewed) — 8 PDFs
├── patents/             # local-only
│   └── korean/          # 17 Korean inventions, each in its own subfolder
├── software/            # local-only — 8 program registrations × 2 PDFs each
└── degrees/             # local-only — B.S. / M.S. / Ph.D. certificates
```

## SCI papers (`papers/sci/`)

11 PDFs total — the 9-paper UST submission bundle plus 2 PhD-era
first-author papers added back in. JCI/JIF screenshots for ATE, ICHMT,
and POF live alongside (used in application packets).

PhD-era SCI papers (KAIST 2017–2021, advisor Prof. Sung Jin Kim, all
first-author):

1. W. Kim & S.J. Kim, "Effect of reentrant cavities on the thermal
   performance of a pulsating heat pipe," *Appl. Therm. Eng.* 133 (2018)
2. W. Kim & S.J. Kim, "Effect of a flow behavior on the thermal performance
   of closed-loop and closed-end pulsating heat pipes," *Int. J. Heat Mass
   Transfer* 149 (2020) — manuscript + corrigendum
3. W. Kim & S.J. Kim, "Fundamental issues and technical problems about
   pulsating heat pipes," *J. Heat Transfer – ASME* 143 (2021)

## KCI papers (`papers/kci/`)

8 PDFs — Korean-language peer-reviewed journals.

## Source

Copied 2026-06-24 from:

- `/Volumes/Woody_KIMM/KIMM/Progress/04_개인/2026UST지원/제출/` — UST 2026
  application bundle (papers, patents, programs, degree certificates)
- `/Volumes/Woody_KIMM/Ph.D./All I want/SCI journal/` — PhD reentrant
  cavities paper
- `/Volumes/Woody_KIMM/Ph.D./All I want/SCI Journal 2/` — PhD flow behavior
  paper (manuscript+corrigendum version)

Filenames preserved as-is (mixed Korean/English); only folder names are
normalized to English so the structure is easy to navigate from any tool.
