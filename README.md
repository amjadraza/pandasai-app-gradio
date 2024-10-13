# 📖 PANDASAI APP

An App to interact with Pandas Dataframes using Generative AI (LLMs). This app is built using `gradio` as the front end and [`pandasai`](https://github.com/gventuri/pandas-ai) as a higher-level Python wrapper to make dataframes conversational.

`pandasai` makes available `openai`, `HuggingFace`, and `Azure` APIs for Generative AI capabilities. 
Users can configure their choice of platform for the backend.  

## 🔧 Features

- Upload csv 📁(csv) and ask questions about the uploaded Data.
- Ask Questions about the data
- Interact with your data like a Human

## 💻 Running Locally

1. Clone the repository📂

```bash
git clone https://github.com/amjadraza/pandasai-app-gradio.git
```

2. Install dependencies with [uv](https://github.com/astral-sh/uv) and activate virtual environment🔨

```bash
# Install uv if you haven't already
pip install uv

# Create a virtual environment and install dependencies using `uv` with `pyproject.toml` file

```bash
# Create a virtual environment
uv venv
source .venv/bin/activate

# Install dependencies from pyproject.toml
uv pip install -r pyproject.toml
```

3. Run the Gradio server🚀

```bash
python src/main.py
```


## 🚀 Upcoming Features

- [ ] Add support for more models (e.g., HuggingFace, Azure).
- [ ] Adding Functionality of Plotting.
- [ ] Some Generic insights on Uploaded Data (e.g., Shape, head, etc.)
- [x] Adding Docker Support to run the App in Docker
- [ ] Push Docker Image to DockerHub for Public use
- [ ] Deploying App on Google App Engine

## Report Feedbacks

As `pandasai` is in active development, as well as LLMs sometimes go south. 
Please report your feedbacks for improvements. 

## DISCLAIMER

The Pandasai app (hereinafter referred to as "the App") is provided for informational purposes only. 
The creators and authors of the App make no representations or warranties of any kind, 
express or implied, about the completeness, accuracy, reliability, suitability, 
or availability of the App or the information, products, services, 
or related graphics contained in the App.

We do not store any data or API keys. Users can refresh Keys as part of Best Practices.

This disclaimer is subject to change without notice. It is your responsibility to review this disclaimer periodically 
for any updates or changes.
