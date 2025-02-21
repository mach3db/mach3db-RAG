### Run an LLM on your machine...
### But store its vector database on mach3db!
<br>
We use exaone3.5:32b as our default LLM:
<br><br>

[exaone3.5:32b](https://ollama.com/library/exaone3.5:32b) <br><br>

### 1. [Install](https://github.com/ollama/ollama?tab=readme-ov-file#macos) Ollama and run model

Install Ollama

```shell
curl -fsSL https://ollama.com/install.sh | sh
```

Run and pull manifest of your preferred LLM model

```shell
ollama run exaone3.5:32b 'Hey!'
```

You can find more LLM's [here](https://ollama.com/library), adjust app.py accordingly.

### 2. Create a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 3. Install libraries

```shell
pip install -r package.txt
```

### 4. edit assistant.py line 10 and add your mach3db username and password
Make sure to contact james@mach3db.com to have the pgvector extension enabled for your mach3db database.

### 5. Run RAG app

```shell
streamlit run app.py
```

- Open [localhost:8501](http://localhost:8501) to view your local RAG app.<br/>

![view.png](view.png)
