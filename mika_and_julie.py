def replace_all(input_file, output_file, search, replace):
    with open(input_file, 'r') as file_name:
        for line in file_name:
            file_name.write(line.replace(search, replace))
        open(output_file, 'w')
        output_file.write(file_name)
    return


