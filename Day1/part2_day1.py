import base_code

INPUT_FILE_PATH = '.\\day1_text.txt'
# INPUT_FILE_PATH = '.\\day1_text_example.txt'

# takes all the elves and counts the largest x elves calories
def max_loop(elf_array, loop_count):
  sorted_elf_array = base_code.mergesort(elf_array)
  total_calorie_count = 0
  for _ in range(loop_count):
    total_calorie_count += sorted_elf_array.pop(len(sorted_elf_array) - 1)
  print(total_calorie_count)


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

# main chunk
def main():
  find_most_calorie_carrying_elf( \
    base_code.process_input_file(INPUT_FILE_PATH))

main()