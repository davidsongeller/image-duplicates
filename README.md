# image-duplicates
### utilize imagehash to compare images and move duplicates into a separate folder for review

- Libraries: `os`, `sys`, `shutil`, `Image`, `imagehash`, and `filecmp`

  - `get_file_hash` takes a file path and calculates the hash of that file.
  - `identify_duplicates` takes a folder path and identifies duplicate files in that folder based on their hashes. It creates a dictionary of file hashes and file paths and checks if the hash already exists in the dictionary. If it does, it adds the file path to a list of duplicates.
  - `move_duplicates_to_folder` takes a list of duplicate file paths and moves them to a new folder called "duplicates". If the file already exists in the "duplicates" folder, it appends a number to the end of the file name and tries again.
  - `run_duplicate_file_detector` takes a folder path, creates the "duplicates" folder, identifies duplicate files using `identify_duplicates`, and moves the duplicate files to the "duplicates" folder using `move_duplicates_to_folder`.
  - The `if __name__ == '__main__':` statements at the end of scripts are to check if the script is being run directly (as opposed to being imported as a module). 
   - If it is being run directly, it checks if a directory argument is provided. If it is, it runs the `run_duplicate_file_detector` function on that directory. If not, it asks the user to input a directory path and runs the `run_duplicate_file_detector` function on that path.
