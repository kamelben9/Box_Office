from code_to_text.code_to_text import read_and_combine_files

read_and_combine_files(input_directory='/home/apprenant/Bureau/Box-Office/',
output_file='/home/apprenant/Bureau/Box-Office/boxoffice/boxoffice.txt',
ignore_file_path='/home/apprenant/Bureau/Box-Office/boxoffice/.codeToTextIgnore')


# import os
# from code_to_text.code_to_text import read_and_combine_files


# input_directory = os.path.dirname(os.path.dirname(__file__))
# output_directory = os.path.dirname(__file__)
# output_file = os.path.join(output_directory, "ctt_output_project.txt")
# ignore_file_path = os.path.join(output_directory, "ctt_ignore")

# print(input_directory, '\n', output_file, '\n', ignore_file_path)

# read_and_combine_files(input_directory, output_file, ignore_file_path)