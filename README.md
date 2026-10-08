# Release Notes and Changelog Drafter

## Overview

This Streamlit application generates release notes and a changelog from commits in a GitHub repository. It fetches the latest commits from a selected branch, uses OpenAI to categorize their messages, and formats the results as Markdown.

## Features

- Fetch up to 30 commits from a GitHub repository branch
- Categorize commit messages with OpenAI
- Generate release notes and a changelog
- Preview the generated documents and commit details in the app
- Download release notes and changelog as Markdown files

Commit categories include new features, bug fixes, improvements, documentation, and breaking changes.

## Technologies

- Python
- Streamlit
- GitHub REST API
- OpenAI API
- Markdown

## Project Structure

```text
release note drafter/
├── app.py
├── github_service.py
├── ai_service.py
├── release_notes.py
├── output/
│   └── screenshotnode.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.9 or later
- An OpenAI API key
- A GitHub repository and branch to read
- A GitHub token is optional for public repositories and can be configured for authenticated API access

## Installation

Open a terminal in the project folder and create a virtual environment:

```powershell
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, use Command Prompt instead:

```bat
venv\Scripts\activate.bat
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Setup

Copy `.env.example` to `.env` in the project folder, then add your own credentials:

```dotenv
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4o-mini
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.3-70b-versatile
GITHUB_TOKEN=your_github_token
```

`OPENAI_API_KEY` is required for the Streamlit app. You can also enter it in the app's masked **OpenAI API Key** sidebar field; the field value is used for that app session and is not written to `.env`. The command-line workflow requires `GROQ_API_KEY`; `OPENAI_MODEL` and `GROQ_MODEL` are optional model settings. `GITHUB_TOKEN` is optional for public repositories. Keep `.env` and your API keys private; do not commit credentials to source control.

Replace each example value with a newly issued credential before use. If a key was ever placed in a shared or tracked file, revoke it and create a new one.

The separate `output/screenshotnode.py` workflow uses `GROQ_API_KEY` and the Groq OpenAI-compatible API. Set `GROQ_MODEL` to choose a model; it defaults to `llama-3.3-70b-versatile`. This workflow sends commit messages and metadata to Groq for analysis.

## Run the Application

Start the Streamlit app from the project folder:

```bash
streamlit run app.py
```

In the app's sidebar, enter the GitHub owner, repository name, branch, release version, and release date. Select **Generate Release Notes** to fetch and analyze the commits.

To run the command-line workflow represented in the screenshots instead, use:

```powershell
python .\output\screenshotnode.py --owner your-github-username --repo your-repository --branch main --version 2.0
```

It writes a combined release-notes and changelog Markdown file to `output/`. The command-line workflow requires `GROQ_API_KEY` in `.env`.

## How It Works

1. The app fetches up to 30 commits from the selected GitHub branch.
2. OpenAI analyzes the commit messages and assigns them to categories.
3. The app creates release notes and a changelog in Markdown.
4. Review the release notes, changelog, and commit details in the app, then download either document.

## Generated Output

The release notes include the selected version and release date, with sections for features, bug fixes, improvements, documentation, and breaking changes. The changelog uses the corresponding `Added`, `Fixed`, `Changed`, `Documentation`, and `Breaking Changes` sections when there are categorized commits.

## Troubleshooting

- **`OPENAI_API_KEY is missing`**: Add `OPENAI_API_KEY` to the `.env` file in the project folder.
- **GitHub API error**: Check the owner, repository, and branch names. For private repositories, configure a valid `GITHUB_TOKEN`.
- **No commits found**: Confirm that the selected branch exists and has commits.   README.md