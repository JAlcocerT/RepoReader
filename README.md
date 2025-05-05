Wrote about reporeader [here](https://jalcocert.github.io/JAlcocerT/selfhosted-apps-may-2025/#automated-projects-docs).

1. Project Goal


    * It’s an interactive CLI tool that lets you point it at any public GitHub repo, automatically clones & indexes all the files in that repo, and then lets you ask natural-language
questions about the code.

    * Under the hood it uses:
            • a simple TF-IDF + BM25 text index to pull back the most relevant code snippets,
            • OpenAI’s GPT-3.5 (via LangChain) to generate human-readable answers,
            • NLTK for tokenization and some basic text cleaning.
2. Prerequisites
    • Python 3.6 or newer
    • git (to clone repositories)
    • An OpenAI API key

3. Installation & Setup

```sh
git clone https://github.com/JAlcocerT/RepoReader

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
#pip install python-dotenv
source .env

python3 app.py #The model `text-davinci-003` has been deprecated, learn more here: https://platform.openai.com/docs/deprecations
```

    1. Clone this project and cd into it:      git clone <this-repo-url>
                cd <this-repo-folder>

    2. (Optional but recommended) Create and activate a virtual environment:      python3 -m venv .venv
                source .venv/bin/activate      # macOS/Linux
                .venv\Scripts\activate         # Windows

    3. Install the Python dependencies:      pip install -r requirements.txt

    4. Provide your OpenAI key:
            • Either export it in your shell:      export OPENAI_API_KEY=sk-...

            • Or create a file named `.env` in the project root containing:      OPENAI_API_KEY=sk-...
4. Running the Explorer

        python app.py

    You’ll see a prompt:


    1. **Enter the GitHub URL** of the repo you want to explore.

    2. The tool will clone & index the repo (using a temporary directory).

    3. Once indexing is done, you’ll be in an interactive Q&A loop:

        * Type any question about the codebase (e.g. “How do I run the tests?”, “What does the `User` class do?”, “Where is the database configuration?”)


        * Type `exit()` to quit.
5. What’s Happening Under the Hood


    * **file_processing.py**
            • `clone_github_repo` → runs `git clone` for you
            • `load_and_index_files` → reads every text/code file, splits them into chunks, tokenizes, builds a BM25 index

    * **questions.py**
            • `ask_question` → for each user query, pulls top-N chunks via BM25 + TF-IDF/Cosine, then feeds those snippets + your question into the OpenAI chain to generate an answer

    * **main.py / app.py**
            • Glue-code: load your OpenAI key, prompt for the repo URL, spin up the loop
6. Tips & Troubleshooting


    * Make sure `git` is on your PATH

    * If NLTK complains about missing data, it will auto-download the “punkt” tokenizer on first run

    * If cloning large repos, indexing may take a minute—watch the console logs

    * You can adjust the LLM temperature or model in `config.py`


---

# Code Repository Explorer

Explore and ask questions about a GitHub code repository using OpenAI's GPT-3 language model.

## Prerequisites

- Python 3.6+
- OpenAI API key (set in the environment variable `OPENAI_API_KEY`)

## Usage
1. Set the OpenAI API key as an environment variable `OPENAI_API_KEY`.
2. Run the script: `reporeader.py`
3. Enter the GitHub URL of the repository to explore.
4. Ask questions about the repository. Type `exit()` to quit.

## Key Features
- Clones and indexes the contents of a GitHub repository.
- Supports various file types, including code, text, and Jupyter Notebook files.
- Generates detailed answers to user queries based on the repository's contents.
- Uses OpenAI's language model for generating responses.
- Supports interactive conversation with the language model.
- Presents top relevant documents for each question.
