from flask import Flask, request, render_template
from expert_system import ExpertSystem

app = Flask(__name__)
system = ExpertSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    symptoms = {
        "demam": float(request.form.get("demam", 0)),
        "batuk": float(request.form.get("batuk", 0)),
        "ruam": float(request.form.get("ruam", 0)),
        "sesak napas": float(request.form.get("sesak_napas", 0))
    }
    diagnosis = system.diagnose(symptoms)
    return render_template('result.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
