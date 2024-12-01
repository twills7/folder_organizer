import os
import shutil
from pathlib import Path

# Define categories and their associated file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []  # Catch-all for unrecognized file types
}

def organize_folder(folder_path):
    """Organizes files in the given folder into subfolders based on file type."""
    folder_path = Path(folder_path)
    if not folder_path.exists():
        print(f"Folder {folder_path} does not exist.")
        return

    for file in folder_path.iterdir():
        # Skip directories
        if file.is_dir():
            continue

        # Determine file type
        file_type = file.suffix.lower()

        # Find the category or assign to "Others"
        destination_folder = "Others"
        for category, extensions in FILE_CATEGORIES.items():
            if file_type in extensions:
                destination_folder = category
                break

        # Create destination folder if it doesn't exist
        category_path = folder_path / destination_folder
        category_path.mkdir(exist_ok=True)

        # Move file to the destination folder
        try:
            shutil.move(str(file), str(category_path / file.name))
            print(f"Moved: {file.name} -> {category_path}")
        except Exception as e:
            print(f"Error moving {file.name}: {e}")

if __name__ == "__main__":
    # Set your folder path here
    target_folder = input("Enter the path to the folder you want to organize: ").strip()
    organize_folder(target_folder)