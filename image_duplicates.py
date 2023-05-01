import os
import sys
import shutil
from PIL import Image
import imagehash
import filecmp

def get_file_hash(file_path):
    """Calculate the hash of a file."""
    with open(file_path, 'rb') as f:
        return hash(f.read())

def identify_duplicates(folder_path):
    """Identify duplicate files in a folder based on their hashes."""
    print("Scanning for duplicate files...")
    file_hashes = {}
    duplicates = []
    processed_files = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                file_hash = get_file_hash(file_path)
                if file_hash in file_hashes:
                    duplicates.append(file_path)
                else:
                    file_hashes[file_hash] = file_path
                processed_files += 1
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    print(f"Processed {processed_files} files.")
    return duplicates

def move_duplicates_to_folder(duplicates, dest_folder):
    """Move duplicate files to a new folder."""
    print("Moving duplicate files to duplicates folder...")
    for file_path in duplicates:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(dest_folder, filename)
        if not os.path.exists(dest_path):
            shutil.move(file_path, dest_path)
            print(f"Moved duplicate file: {file_path} to {dest_path}")
        else:
            duplicate_filename = os.path.splitext(filename)[0]
            duplicate_ext = os.path.splitext(filename)[1]
            counter = 1
            while os.path.exists(dest_path):
                duplicate_filename = f"{os.path.splitext(filename)[0]}_{counter}"
                filename = f"{duplicate_filename}{duplicate_ext}"
                dest_path = os.path.join(dest_folder, filename)
                counter += 1
            shutil.move(file_path, dest_path)
            print(f"Moved duplicate file: {file_path} to {dest_path}")

def run_duplicate_file_detector(folder_path):
    """Run the duplicate file detector on a specified folder."""
    # Specify the destination folder for moving duplicate files
    dest_folder = os.path.join(folder_path, 'duplicates')

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Identify duplicate files
    duplicates = identify_duplicates(folder_path)

    if duplicates:
        print(f"Found {len(duplicates)} duplicate files:")
        for file_path in duplicates:
            print(file_path)
        # Move duplicate files to the destination folder
        move_duplicates_to_folder(duplicates, dest_folder)
    else:
        print("No duplicate files found.")

if __name__ == '__main__':
    # Check if a directory argument is provided
    if len(sys.argv) == 2:
        folder_path = sys.argv[1]
        if os.path.isdir(folder_path):
            run_duplicate_file_detector(folder_path)
        else:
            print("Error: Invalid directory path.")
    else:
        # Request user input for the directory path
        folder_path = input("Enter the folder path to scan for duplicate files: ")
        if os.path.isdir(folder_path):
            run_duplicate_file_detector(folder_path)
        else:
            print("Error: Invalid directory path.")
