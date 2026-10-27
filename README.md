# CI/CD Starter Template (Python + GitHub Actions)

![CI](https://github.com/samruddhi96-S/ci-cd-pipeline/actions/workflows/ci.yml/badge.svg)

A ready-made CI/CD pipeline that you can copy into any Python project.
On every push it automatically **lints, tests, scans for security issues, builds a Docker image and publishes it**.

## What it does

| Step | Tool | Purpose |
|------|------|---------|
| 1. Lint | ruff | Checks code style and common mistakes |
| 2. Test | pytest + coverage | Runs the tests and enforces at least 80% coverage |
| 3. Security | bandit, pip-audit | Finds unsafe code and vulnerable libraries |
| 4. Docker build | Docker | Packages the app in a container and runs a health check |
| 5. Publish (CD) | GitHub Container Registry | Publishes the image to `ghcr.io`, no extra account needed |

Pipeline flow:

```
push / pull request -> Lint + Test (Python 3.11, 3.12) -> Security scan -> Docker build -> Publish (main branch only)
```

## How to use it in your company (3 steps)

1. Click **"Use this template"** on the GitHub repository page. (To enable this button, go to Settings and tick "Template repository".)
2. Put your code in `app/` and your tests in `tests/`. List your libraries in `requirements.txt`.
3. Push your code. Open the **Actions** tab and the pipeline runs automatically.

No secrets, tokens or extra setup are required. The publish step uses GitHub's built-in token.

## Uploading to GitHub for the first time

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

Make sure the hidden `.github` folder is included, otherwise the pipeline will not run.

## Running locally (optional)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (on Mac/Linux: source .venv/bin/activate)
pip install -r requirements-dev.txt
ruff check .                    # lint
pytest --cov                    # tests with coverage
python -m app.main              # start the app at http://localhost:5000
```

With Docker:

```bash
docker build -t cicd-starter .
docker run -p 5000:5000 cicd-starter
```

## Sample app endpoints

- `/` welcome message
- `/health` health check
- `/calc/add?a=2&b=3` (supports add, subtract, multiply, divide)

## Customizing

- **Change the Python versions:** edit the `python-version` list in `.github/workflows/ci.yml`.
- **Change the coverage limit:** edit `--cov-fail-under=80` in `ci.yml`.
- **Add a test:** create a `test_*.py` file in the `tests/` folder.
- **Deploy somewhere else:** replace the last step in `cd.yml` (Render, Railway, your own server, etc.).

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Pipeline does not run at all | The `.github` folder was not uploaded | Upload the folder again |
| Lint (`ruff`) fails | Code style issue | Run `ruff check . --fix` |
| Coverage check fails | Less than 80% of the code is tested | Add more tests or lower the limit |
| Security scan (`bandit`) fails | Unsafe code pattern found | Fix the line it reports |
| Publish step fails | Missing package permission | Settings -> Actions -> General -> Workflow permissions -> "Read and write permissions" |

## Folder structure

```
app/                  Python source code
tests/                Automated tests
.github/workflows/    ci.yml (lint, test, security, Docker) and cd.yml (publish)
Dockerfile            Builds the container image
Makefile              Shortcut commands (make test, make lint)
```