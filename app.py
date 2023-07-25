from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"
model_engine = "text-davinci-003"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.9,
            )
            response = completion.choices[0].text
            return render_template("index.html", response=response)
        except Exception as e:
            return render_template("index.html", error=f"Error: {e}")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
