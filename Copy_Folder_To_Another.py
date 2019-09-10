import shutil, os


def down_copy(input_path,output_path):
    dirs = []
    files = []
    for _, dirs, files in os.walk(input_path):
        break
    for file in files:
        shutil.copy(os.path.join(input_path,file),os.path.join(output_path,file))
    for dir_val in dirs:
        new_out = os.path.join(output_path,dir_val)
        if not os.path.exists(new_out):
            os.makedirs(new_out)
        down_copy(os.path.join(input_path,dir_val),new_out)


def down_folder(input_path,output=r'\\mymdafiles\di_data1\Morfeus\Andrea\Copy_Logs',base_path=r'G:\Cat',folder_criteria=None):
    dirs = []
    for _, dirs, _ in os.walk(input_path):
        break
    for dir_val in dirs:
        if folder_criteria(dir_val):
            new_output = os.path.join(input_path.replace(base_path,output),dir_val)
            if not os.path.exists(new_output):
                os.makedirs(new_output)
            print(new_output)
            down_copy(os.path.join(input_path,dir_val), new_output)
        else:
            down_folder(os.path.join(input_path,dir_val),output=output,base_path=base_path, folder_criteria=folder_criteria)
    return None


if __name__ == '__main__':
    xxx = 1
    # output = r'\\mymdafiles\di_data1\Morfeus\bmanderson\Copy_Of_Sanne_Patients'
    # base_path = r'R:\Team Share\Sam_Mulder\P_F_X\MATLAB_Practice\OutputNEWEST\DIXON'
    # folder_criteria = lambda i: i.find('RTSTRUCT') != -1
    # down_folder(base_path, output=output, base_path=base_path, folder_criteria=folder_criteria)