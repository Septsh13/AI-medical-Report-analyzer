import json
import csv
import os

EXPORT_FOLDER = "exports"
os.makedirs(EXPORT_FOLDER, exist_ok=True)

# Export to JSON
def export_to_json(data, output_path="structured.json"):
    path = os.path.join(EXPORT_FOLDER, output_path)
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    return path

# Export to CSV
def export_to_csv(data, output_path="structured.csv"):
    path = os.path.join(EXPORT_FOLDER, output_path)

    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)

        # Case 1: single dictionary (e.g., {"Name": "John", "Age": 30})
        if isinstance(data, dict):
            writer.writerow(data.keys())
            writer.writerow(data.values())

        # Case 2: list of dictionaries (e.g., [{"Name": "John"}, {"Name": "Jane"}])
        elif isinstance(data, list) and data and isinstance(data[0], dict):
            keys = data[0].keys()
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

        # Unsupported format
        else:
            writer.writerow(["Error: Unsupported data format"])
    
    return path
