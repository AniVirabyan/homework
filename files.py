#4
import os
import sys

def organize_files(source_dir):
    if not os.path.exists(source_dir):
        print(f"Error: Directory '{source_dir}' does not exist.")
        return

    file_types = {
        '.docs': 'docs',
        '.pdf': 'pdf',
        '.jpg': 'images',
        '.png': 'images',
        '.txt': 'texts',
        
    }

    create_directories(source_dir, file_types)
    move_files(source_dir, file_types)

def create_directories(source_dir, file_types):
    for folder in file_types.values():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def move_files(source_dir, file_types):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in file_types:
                dest_folder = file_types[file_ext]
                dest_path = os.path.join(source_dir, dest_folder, filename)
                os.rename(file_path, dest_path)
                print(f"Moved: {filename} to {dest_folder}")
def main():
    if len(sys.argv) != 2:
        print("Usage: python organize_files.py <source_directory>")
    else:
        source_dir = sys.argv[1]
        organize_files(source_dir)

if __name__ == "__main__":
    main()
