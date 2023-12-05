import os
import subprocess
import shutil

current_folder = "D:\\My Programming\\Python\\wifi_scanner\\"
def new_file(file: str, type: str) -> int:
    file = file + "." + type

    try:
        with open(file, 'x') as f:  # 'x' mode raises FileExistsError if file already exists
            return 1 # File created successfully
    except FileExistsError:
        return 0  # File already exists
    except Exception as e:
        return -1  # An exception occurred

def list_files() -> list[str]:
    cmd = ["cmd", "/c", "dir", "/b", current_folder + "*.csv"]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print("Error listing files")
    else:
        # Split the result by lines
        lines = result.stdout.splitlines()
    
        # Filter and extract the filenames
        files = [line for line in lines if line.endswith('.csv')]
        return files

def file_exists(filename: str) -> int:
    # Returns 1 if the file exists, otherwise 0.

    if not filename:
        return 0
    return 1 if os.path.exists(current_folder + filename) else 0

def create_backup(orig_file: str) -> int:
    """
        Create a backup of the given file with a .bak extension.
    """

    try:
        bak_file = orig_file + ".bak"
        shutil.copy(orig_file, bak_file)
        return 1
    except Exception as e:
        return 0

def del_file(file_name: str) -> int:
    try:
        if file_exists(file_name):
            os.remove(file_name)
        else:
            return 0
        return 1
    except Exception as e:
        return -1

def append_file():
    pass



