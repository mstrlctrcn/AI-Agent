import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if not full_path.startswith(working_directory):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    try:
        directory_list = os.listdir(full_path)
        files_info = []
        for file in directory_list:
            filepath = os.path.join(full_path, file)
            file_size = os.path.getsize(filepath)
            is_dir = os.path.isdir(filepath)
            info = f"{file}: file_size={file_size} bytes, is_dir={is_dir}"
            files_info.append(info)
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"