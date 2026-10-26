# CI/CD Starter Template (Python + GitHub Actions)

![CI](https://github.com/samruddhi96-S/ci-cd-pipeline/YOUR-/actions/workflows/ci.yml/badge.svg)

Ek ready-made CI/CD pipeline jo kisi bhi Python project me copy karke use ho sakti hai.
Code push karte hi ye apne aap **lint, test, security scan, Docker build aur publish** karti hai.

## Ye kya karta hai

| Step | Tool | Kaam |
|------|------|------|
| 1. Lint | ruff | Code style aur galtiyan check |
| 2. Test | pytest + coverage | Code sahi chal raha hai ya nahi, aur kitna code test hua (minimum 80%) |
| 3. Security | bandit, pip-audit | Unsafe code aur vulnerable libraries |
| 4. Docker build | Docker | App ko container me pack karke health check |
| 5. Publish (CD) | GitHub Container Registry | Image `ghcr.io` pe publish, koi extra account nahi |

Pipeline flow:

```
push / pull request -> Lint + Test (Python 3.11, 3.12) -> Security -> Docker build -> (main branch pe) Publish
```

## Company me use kaise kare (3 steps)

1. GitHub pe is repo me **"Use this template"** button dabao (ya repo ko apne account me upload karo). *Template repo banane ke liye: Settings -> "Template repository" tick karo.*
2. `app/` me apna code aur `tests/` me apne tests daalo. Libraries `requirements.txt` me likho.
3. Code push karo. **Actions** tab me pipeline apne aap chalti dikhegi. Bas.

Koi secret, token ya extra setup nahi chahiye. Publish step GitHub ka built-in token use karta hai.

## Repo ko GitHub pe upload kaise kare (pehli baar)

1. github.com pe naya repository banao (Public rakho taaki Actions free rahe).
2. Repo page pe **"uploading an existing file"** link pe click karo.
3. Is folder ki saari files drag-drop karo (`.github` folder ke saath) aur **Commit changes** dabao.
4. **Actions** tab kholo, pipeline chal rahi hogi. Green tick = sab pass.

> Dhyan do: `.github` folder hidden hota hai. Upload karte time ye folder zaroor include ho, warna pipeline nahi chalegi.

## Apne computer pe chalana (optional)

```bash
pip install -r requirements-dev.txt   # ya: make install
ruff check .                          # lint
pytest --cov                          # tests
python -m app.main                    # app chalao, phir browser me http://localhost:5000
```

Docker se: `docker build -t cicd-starter .` phir `docker run -p 5000:5000 cicd-starter`

## Sample app ke endpoints

- `/` welcome message
- `/health` health check
- `/calc/add?a=2&b=3` (add, subtract, multiply, divide)

## Customize kaise kare

- **Python version badalna:** `.github/workflows/ci.yml` me `python-version` list.
- **Coverage limit badalna:** `ci.yml` me `--cov-fail-under=80`.
- **Naya test:** `tests/` folder me `test_*.py` file banao.
- **Deploy kisi aur jagah:** `cd.yml` me last step badlo (Render/Railway/server).

## Common errors aur solution

| Error | Wajah | Solution |
|-------|-------|----------|
| Pipeline chal hi nahi rahi | `.github` folder upload nahi hua | Folder dobara upload karo |
| `ruff` fail | Code style issue | `ruff check . --fix` chalao |
| Coverage fail | 80% se kam code test hua | Aur tests likho ya limit kam karo |
| Publish step fail | Package permission | Settings -> Actions -> General -> Workflow permissions -> "Read and write" |

## Folder structure

```
app/                  Python code
tests/                Tests
.github/workflows/    ci.yml (test, security, docker) aur cd.yml (publish)
Dockerfile            Container banane ke liye
Makefile              Short commands (make test, make lint)
```
