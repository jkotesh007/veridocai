import os
from datetime import datetime
#Directory to save uploaded notes
UPLOAD_DIR="app/temp_uploads"
#Make sure UPLOAD_DIR exists
os.makedirs(UPLOAD_DIR,exist_ok=True)

def save_project_notes(notes_text):
    try:
        timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
        filename=f"project_notes_{timestamp}.txt"
        file_path=os.path.join(UPLOAD_DIR,filename)
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(notes_text)
        return True
    except Exception as e:
        print(f"Error saving project notes: {e}")
        return False


def list_saved_notes():
    try:
        files=[f for f in os.listdir(UPLOAD_DIR) if f.endswith('.txt')]
        return files
    except Exception as e:
        print(f"Error listing files:{e}")
        return[]

def read_project_notes(filename):
    try:
        file_path=os.path.join(UPLOAD_DIR,filename)
        with open(file_path,"r",encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading project notes:{e}")
        return None

def save_generated_memo(memo_text):
    try:
        output_dir="app/generated_memos"
        os.makedirs(output_dir,exist_ok=True)
        filename="generated_memo.txt"
        file_path=os.path.join(output_dir,filename)
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(memo_text)
        return file_path
    except Exception as e:
        print(f"Error saving generated memo:{e}")
        return None
