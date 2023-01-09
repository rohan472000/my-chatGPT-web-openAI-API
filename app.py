import openai
from flask import Flask, render_template, request

app = Flask(__name__)

openai.api_key = "openAI-API-key"


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(generate_response(user_text))


if __name__ == "__main__":
    app.run(port=8090)
