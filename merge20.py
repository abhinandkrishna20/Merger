import os
import shutil

def move_files_to_single_folder_and_cleanup(source_folder, destination_folder, script_name):
    """
    Moves all files from subfolders of the source_folder into a single destination folder,
    skips the script file itself, and deletes empty folders after moving files.

    :param source_folder: Path to the folder containing subfolders
    :param destination_folder: Path to the destination folder where files will be moved
    :param script_name: Name of the script file to be skipped
    """
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Walk through the directory tree
    for root, _, files in os.walk(source_folder, topdown=False):  # Process subdirectories last
        for file in files:
            # Skip the script file itself
            if file == script_name:
                continue

            # Get the full path of the source file
            source_file_path = os.path.join(root, file)

            # Skip files already in the destination folder
            if os.path.abspath(root) == os.path.abspath(destination_folder):
                continue

            # Define the destination file path
            destination_file_path = os.path.join(destination_folder, file)

            # Check for duplicate file names
            if os.path.exists(destination_file_path):
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination_file_path):
                    destination_file_path = os.path.join(destination_folder, f"{base}_{counter}{ext}")
                    counter += 1

            # Move the file
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: {source_file_path} to {destination_file_path}")

        # Remove the folder if it is empty
        if root != source_folder and not os.listdir(root):
            os.rmdir(root)
            print(f"Deleted empty folder: {root}")

# Example usage
source_folder = os.getcwd()  # Current folder
destination_folder = os.path.join(source_folder, "merged_files")  # A subfolder named "merged_files"
script_name = "merge20.py"  # Name of the Python script file to skip

move_files_to_single_folder_and_cleanup(source_folder, destination_folder, script_name)
