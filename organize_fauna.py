import os
import shutil

# 1. Configuration
source_folder = 'data'
# Add any animals you are tracking here
categories = ['jaguar', 'macaw', 'capybara']

def organize_images():
    # Create the categories folders if they don't exist
    for category in categories:
        folder_path = os.path.join(source_folder, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

    # Loop through the files in the 'data' folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        # Skip directories, we only want files
        if os.path.isdir(file_path):
            continue

        # Check filename for keywords and move the file
        moved = False
        for category in categories:
            if category in filename.lower():
                dest_path = os.path.join(source_folder, category, filename)
                shutil.move(file_path, dest_path)
                print(f"Moved {filename} -> {category}/")
                moved = True
                break
        
        if not moved:
            print(f"Skipped {filename} (No category match)")

if __name__ == "__main__":
    organize_images()
    print("\nOrganization complete!")