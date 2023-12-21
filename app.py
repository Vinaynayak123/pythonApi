import os
import shutil

# Directories to be searched for temporary files
temp_directories = [
    '/private/var/folders',
    '~/Library/Caches',
    '~/Library/Logs',
    '~/Downloads',
    '~/Desktop'
]

# List of file extensions to be removed
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
            # Check if the file extension is in the list of extensions to be removed
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
                    
