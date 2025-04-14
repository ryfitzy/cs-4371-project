# cs-4371-project
Prompt injection attack against LLM-integrated applications

## Members
Colin Crippen,
Joseph Dippel,
Ryan Fitzgerald,
Will Jefts and
Sabrina Khan



## Building
*This project may be large. LLMs take up several GBs each. Ensure you have proper storage free.*

### Prerequisites:
* [Python](https://www.python.org/downloads)
* [Ollama](https://ollama.com/download)


### Setup:
1. Clone the repo into a directory on your machine.

2. Create a python [virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments):  
    * On Linux/MacOS:
        * `python -m venv .venv`
        * `source .venv/bin/activate`
    * On Windows:
        * `python -m venv .venv`
        * `.venv\Scripts\activate.bat` *(command prompt)* **OR**
        * `.venv\Scripts\Activate.ps1` *(powershell)*

3. Install the dependencies:
    * `pip install -r requirements.txt`

4. Ensure Ollama is running (you can run `ollama` to start)

5. Download the following models:
    * [Mistral](https://ollama.com/library/mistral): 4.1 GB - `ollama pull mistral`
    * [Gemma 3](https://ollama.com/library/gemma3): 3.3 GB - `ollama pull gemma3`
    * [Llama 3.2](https://ollama.com/library/llama3.2): 2.0 GB - `ollama pull llama3.2`

### Running

Navigate to the root directory of the repo, then type `flask run`. It should start on http://127.0.0.1:5000 by default. Navigate to the link in your browser to view the app.
