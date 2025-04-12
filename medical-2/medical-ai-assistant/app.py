from flask import Flask, request, render_template
from utils.ocr import extract_text_from_image, extract_text_from_pdf
from utils.extract import extract_structured_data, generate_summary_with_llm
from utils.export import export_to_json, export_to_csv
from utils.ollama_llm import generate_summary_with_llm
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload and export folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs("exports", exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ""
    summary = ""
    data = {}
    json_path = ""
    csv_path = ""

    if request.method == 'POST':
        file = request.files['file']
        model = request.form.get('model')  # "spacy" or "ollama"

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Extract text
        if file.filename.lower().endswith('.pdf'):
            extracted_text = extract_text_from_pdf(filepath)
        else:
            extracted_text = extract_text_from_image(filepath)

        # Extract structured data
        data = extract_structured_data(extracted_text)

        # Generate AI Summary
        if model == 'ollama':
            summary = generate_summary_with_llm(extracted_text)
        else:
            summary = generate_summary(data)

        # Export to JSON and CSV
        json_path = export_to_json(data)
        csv_path = export_to_csv(data)

    return render_template("index.html", 
        extracted_text=extracted_text, 
        summary=summary, 
        json_file=json_path, 
        csv_file=csv_path
    )

# 🟢 Flask App Runner
if __name__ == '__main__':
    app.run(debug=True)
