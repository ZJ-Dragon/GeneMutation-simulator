from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dna_utils import complement, transcribe, translate, mutate  # ensure dna_utils.py has these functions

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # enable CORS for local JS fetch()

@app.route("/")
def index():
    """Serve the main HTML page."""
    return render_template("index.html")

@app.route("/mutate", methods=["POST"])
def mutate_api():
    """
    Accept JSON payload:
      {
        "template": "<DNA template strand>",
        "type": "sub" | "ins" | "del",
        "pos": "7" or "3-5",
        "base": "A" | "T" | "G" | "C"   # optional for deletion
      }
    Return JSON with updated sequences.
    """
    data = request.get_json(force=True)
    tpl = data["template"].strip().upper()
    mtype = data["type"]
    pos = data["pos"]
    base = data.get("base", "").upper() if data.get("base") else None

    new_tpl = mutate(tpl, mtype, pos, base)
    coding = complement(new_tpl)
    mrna = transcribe(coding)
    amino = translate(mrna)

    return jsonify({
        "template": new_tpl,
        "coding": coding,
        "mrna": mrna,
        "amino": amino
    })

if __name__ == "__main__":
    # Debug mode ON for hot‑reload during development
    app.run(host="0.0.0.0", port=7777, debug=True)