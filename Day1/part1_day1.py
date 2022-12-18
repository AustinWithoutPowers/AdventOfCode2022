import base_code

INPUT_FILE_PATH = '.\\day1_text.txt'
# INPUT_FILE_PATH = '.\\day1_text_example.txt' # example answer is 24000

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
  print(max(elf_array))

# main chunk
def main():
  find_most_calorie_carrying_elf( \
    base_code.process_input_file(INPUT_FILE_PATH))

main()