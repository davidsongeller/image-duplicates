## Duplicate File Detector

### Overview
The Duplicate File Detector is a Python program that scans a specified folder for duplicate files based on their hashes. It identifies duplicate files and moves them to a new folder named "duplicates". 

### Dependencies
The Following Python libraries:
- os
- sys
- shutil
- PIL (Python Imaging Library)
- imagehash
- filecmp

### Usage
To use the Duplicate File Detector:
1. Run the program in the command line using the command `python duplicate_file_detector.py [folder_path]`.
2. The program will scan the specified folder for duplicate files and move them to a new folder named "duplicates" within the specified folder.
3. If no duplicate files are found, the program will display a message indicating so.

### Notes
- If no folder path is specified in the command line, the program will prompt the user to enter a folder path.
- If a folder named "duplicates" already exists within the specified folder, the program will rename the duplicate files with a counter suffix and move them to the "duplicates" folder.
