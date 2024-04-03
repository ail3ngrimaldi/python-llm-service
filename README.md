## Python Service for Matrix LLM-Bot

This Python service handles communication with the Large Language Model (LLM) on behalf of the Matrix LLM-Bot. It receives messages from a Matrix user via a Rust client, processes them with the LLM, and sends the LLM-generated replies back to the user.

### How to initialize

Execute python app.py or python3 app.py to get your service up. It will immediately listen to every message the client sends and get a reply from the LLM.

### What do we use?

This service utilizes the following frameworks:

- Langchain: https://www.langchain.com/ for interacting with the LLM.
- Flask: https://flask.palletsprojects.com/en/3.0.x/ for providing the web service capabilities.

See the [Matrix LLM-Bot](https://github.com/ail3ngrimaldi/matrix-llm-bot) for more information on the overall project.
