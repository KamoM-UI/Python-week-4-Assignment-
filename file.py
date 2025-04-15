

def read_file(file_path, new_file_path):

    try:
        with open(file_path, 'r') as file:
            data = file.read()
    
        modify_file = data.upper()

        with open(new_file_path, 'w') as new_file:
            new_file.write(modify_file)

            print(f"Modified content written to '{new_file_path}' successfully.")

    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    










