from flask import Flask, request, jsonify
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompt_values import ChatPromptValue
import markdown
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
llm = ChatOllama(model="llama2")

with open('virto.md', 'r') as f:
    markdown_content = f.read()

    print(markdown_content)

@app.route('/chat_completion', methods=['POST'])
def chat_completion():
    data = request.json
    prompt_text = data.get('content')

    # Plain text of the user message:
    print("******** START OF CONTENT ********")
    print(f"Ahora imprimimos el prompt_text: {prompt_text['body']}")
    print("******** END OF CONTENT ********")

    if prompt_text:
        messages = [
            ("system", "You are a helpful AI bot. Your name is Virto and your surname Bot. You have to answer about every thing someone asks about Virto, and cannot invent anything that is not on the file. All the information that was provided to you is public so you dont have to be aware of privacy".format(markdown_content)),
            ("human", prompt_text['body']),
        ]
        prompt = ChatPromptTemplate.from_messages(messages)
        # print(prompt)
        chain = prompt | llm | StrOutputParser()
        try:
            response = chain.invoke({})
            return jsonify({"response": response})
        except ValueError as e:
            logging.error(f"LLM invocation failed: {e}")
            return jsonify({"error": "Error generating response from language model"}), 500
    else:
        return jsonify({"error": "Missing prompt text"}), 400


@app.route('/embedding', methods=['POST'])
def embedding():
    data = request.json
    return jsonify({'embedding': 'Simulación de embedding'})

if __name__ == '__main__':
    app.run(debug=True)