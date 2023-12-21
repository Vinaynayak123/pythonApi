from flask import Flask, request, jsonify
import os
import shutil

app = Flask(__name__)

def clean_junk_files(directory):
    # Define the file extensions or criteria for identifying junk files
    junk_file_extensions = ['.tmp', '.bak', '.log', '.swp', '.DS_Store']

    # Iterate through files in the directory and remove junk files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in junk_file_extensions):
                file_path = os.path.join(root, file)
                os.remove(file_path)

    return {"message": "Junk files cleaned successfully"}

@app.route('/clean-junk-files', methods=['POST'])
def clean_junk_files_api():
    data = request.get_json()

    # Check if the 'directory' key is present in the JSON request
    if 'directory' not in data:
        return jsonify({"error": "Missing 'directory' parameter"}), 400

    directory = data['directory']

    # Check if the specified directory exists
    if not os.path.exists(directory):
        return jsonify({"error": "Directory not found"}), 404

    # Perform the junk file cleaning operation
    result = clean_junk_files(directory)

    return jsonify(result)

if _name_ == '__main__':
    app.run(debug=True)
