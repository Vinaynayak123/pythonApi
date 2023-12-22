from flask import Flask, jsonify
import os
import shutil 
app = Flask(__name__)

# Your code for cleaning temporary files
def clean_temp_files():
    temp_directories = [
        '/private/var/folders',
        '~/Library/Caches',
        '~/Library/Logs',
        '~/Downloads',
        '~/Desktop'
    ]

    extensions = [
        '.log',
        '.cache',
        '.tmp',
        '.dmg',
        '.pkg'
    ]

    for directory in temp_directories:
        for dirpath, dirnames, filenames in os.walk(os.path.expanduser(directory)):
            for filename in filenames:
                if os.path.splitext(filename)[1].lower() in extensions:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        if os.path.isfile(filepath):
                            os.remove(filepath)
                        elif os.path.isdir(filepath):
                            shutil.rmtree(filepath)
                        print(f"Removed {filepath}")
                    except Exception as e:
                        print(f"Error deleting {filepath}: {e}")

# Define a route for cleaning temporary files
@app.route('/clean_temp_files', methods=['GET'])
def route_clean_temp_files():
    clean_temp_files()
    return jsonify({'message': 'Temporary files cleaned successfully.'})

if _name_ == '__main__':
    app.run(debug=True)
