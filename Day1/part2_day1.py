INPUT_FILE_PATH = '.\\day1_text.txt'
# INPUT_FILE_PATH = '.\\day1_text_example.txt'

# takes all the elves and counts the largest x elves calories
def max_loop(elf_array, total_count):
  pass

# best function name ever
def find_most_calorie_carrying_elf(line_array):
  elf_array = [0]
  elf_count = 0
  for line in line_array:
    if len(line) < 1:
      elf_count += 1
      elf_array += [0]
    else:
      try:
        elf_array[elf_count] += int(line)
      except Exception:
        print('Probably the int/str conversion...\n')
  max_loop(elf_array, 3)

# iterates over array and "trims" all the entries
def remove_newlines(line_array):
  newlineless_array = []
  for line in line_array:
    newlineless_array += [line.strip()]
  find_most_calorie_carrying_elf(newlineless_array)

# reads input file and returns array of lines
def get_file_data():
  input_file = open(INPUT_FILE_PATH, 'r')
  remove_newlines(input_file.readlines())

# main chunk
def main():
  get_file_data()

main()