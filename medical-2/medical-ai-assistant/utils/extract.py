from .ollama_llm import generate_summary_with_llm

def extract_structured_data(text):
    structured_data = {
        "Patient Name": "",
        "Age": "",
        "Doctor Name": "",
        "Hospital": "",
    }

    # Optionally extract basic info using simple patterns (customize this as needed)
    if "Patient Name:" in text:
        structured_data["Patient Name"] = text.split("Patient Name:")[1].split("\n")[0].strip()
    if "Age:" in text:
        structured_data["Age"] = text.split("Age:")[1].split("\n")[0].strip()
    if "Doctor:" in text:
        structured_data["Doctor Name"] = text.split("Doctor:")[1].split("\n")[0].strip()
    if "Hospital:" in text:
        structured_data["Hospital"] = text.split("Hospital:")[1].split("\n")[0].strip()

    # AI Summary
    summary = generate_summary_with_llm(text)

    # Extract AI-provided details
    for line in summary.splitlines():
        line = line.strip()
        if line.lower().startswith("disease"):
            structured_data["Disease/Diagnosis"] = line.split(":", 1)[-1].strip()
        elif line.lower().startswith("treatment"):
            structured_data["Treatment/Advice"] = line.split(":", 1)[-1].strip()

    return [structured_data]
