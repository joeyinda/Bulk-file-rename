import os

# Function to rename files in a directory
def rename_files(directory, prefix, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            new_filename = prefix + filename
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")

# Main program
def main():
    directory = input("Enter the directory path: ")
    prefix = input("Enter the new filename prefix: ")
    extension = input("Enter the file extension (e.g., .txt): ")

    rename_files(directory, prefix, extension)

# Start the program
main()
