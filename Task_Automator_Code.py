import os

# Define the directory path where the files are located
directory = "path/to/directory"

# Define the new file name format
new_name_format = "New_File_{index}.txt"

# Get a list of files in the directory
file_list = os.listdir(directory)

# Iterate over the files and rename them
for index, file_name in enumerate(file_list):
    # Create the new file name
    new_file_name = new_name_format.format(index=index)
    
    # Construct the full paths for the old and new file names
    old_file_path = os.path.join(directory, file_name)
    new_file_path = os.path.join(directory, new_file_name)
    
    # Rename the file
    os.rename(old_file_path, new_file_path)
    
    # Print the renaming status
    print(f"Renamed {file_name} to {new_file_name}")

print("Task completed!")
