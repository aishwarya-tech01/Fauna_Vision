import os
import shutil

# 1. Define where the images are and what folders to create
source_dir = 'data'
categories = ['jaguar', 'macaw', 'capybara']

# 2. Create folders if they don't exist
for category in categories:
    path = os.path.join(source_dir, category)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {category}")

# 3. Move files based on their names
for filename in os.listdir(source_dir):
    # We only want to move files (not folders)
    if os.path.isfile(os.path.join(source_dir, filename)):
        lower_name = filename.lower()
        
        for category in categories:
            if category in lower_name:
                shutil.move(os.path.join(source_dir, filename), 
                            os.path.join(source_dir, category, filename))
                print(f"Moved {filename} to {category}/")
                break

print("All done! Your dataset is organized.")
