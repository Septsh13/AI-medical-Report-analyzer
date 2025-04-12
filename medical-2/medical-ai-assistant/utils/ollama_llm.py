import subprocess

def generate_summary_with_llm(text):
    try:
        prompt = f"""
        Extract a concise summary from the following medical text. Include:
        - Disease or Diagnosis
        - Suggested Treatment, Medication, or Advice

        Text:
        {text}

        Respond in this format:
        Disease: ...
        Treatment: ...
        """

        # Run Ollama using subprocess and pass the prompt via stdin
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("Ollama error:", result.stderr)
            return "LLM failed to generate summary."

        return result.stdout.strip()

    except Exception as e:
        return f"LLM exception: {str(e)}"
