"# Copy_Folders" 
This code is written to copy folders that meet certain criteria from one location to another

from Copy_Folders.Copy_Folder_To_Another import down_folder

    output = r'\\path_to\output_images'
    base_path = r'R:\path_to\current_images'
    folder_criteria = lambda i: i.find('RTSTRUCT') != -1 # If the folder has the title 'RTSTRUCT' in it, copy
    down_folder(base_path, output=output, base_path=base_path, folder_criteria=folder_criteria)
