INPUT_FILE_PATH = '.\\day1_text.txt'

# reads input file and returns array of lines
def get_file_data():
  input_file = open(INPUT_FILE_PATH, 'r')
  return input_file.readlines()

# iterates over array and "trims" all the entries
def remove_newlines(input_array):
  temp_array = []
  for line in input_array:
    temp_array += [line.strip()]
  return temp_array

# main chunk
def main():
  input_array = get_file_data()
  input_array = remove_newlines(input_array)
  print(input_array)

main()