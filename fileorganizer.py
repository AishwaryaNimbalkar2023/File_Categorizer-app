import os
import shutil

def organize_files(path):
    # Define categories and their corresponding extensions
    categories = {
        "Images": ["jpg", "jpeg", "png", "gif", "avif"],
        "Videos": ["mp4", "avi", "mkv", "mov"],
        "Documents": ["pdf", "docx", "txt", "xlsx"],
        "Audio": ["mp3", "wav", "aac"],
        "Archives": ["zip", "rar", "xz"],
        "Programming": ["c", "java", "py", "cpp", "js", "html", "css"],
        "Others": []
    }

    if not os.path.exists(path):
        return "The specified path does not exist."

    # List all files in the directory
    files = os.listdir(path)
    if not files:
        return "No files found in the directory."

    result_log = []  # To store logs of moved files

    for file in files:
        # Skip directories
        if not os.path.isfile(os.path.join(path, file)):
            continue

        # Extract file extension
        _, extension = os.path.splitext(file)
        extension = extension[1:].lower()  # Remove the leading dot and convert to lowercase

        # Determine the category
        category = "Others"
        for cate, exts in categories.items():
            if extension in exts:
                category = cate
                break

        # Handle "Programming" category with subfolders for extensions
        if category == "Programming":
            category_path = os.path.join(path, category, extension)
        else:
            category_path = os.path.join(path, category)

        # Create the category folder (and subfolder for extensions if needed)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        # Move the file to the appropriate category folder
        source = os.path.join(path, file)
        destination = os.path.join(category_path, file)
        shutil.move(source, destination)
        result_log.append(f"Moved: {file} --> {category}/{extension}/{file}" if category == "Programming" else f"Moved: {file} --> {category}/{file}")

    return "\n".join(result_log)

