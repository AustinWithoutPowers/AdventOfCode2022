import base_code

INPUT_FILE_PATH = '.\\day4_text.txt'
# INPUT_FILE_PATH = '.\\day4_text_example.txt' # example answer is X

def check_for_overlap(sorted_pair):
  if sorted_pair[0][0] <= sorted_pair[1][0]:
    if sorted_pair[0][1] >= sorted_pair[1][0]:
      return 1
  if sorted_pair[1][0] <= sorted_pair[0][0]:
    if sorted_pair[1][1] >= sorted_pair[0][0]:
      return 1
  return 0

def sort_pairs(pair):
  pair_array = pair.split(',')
  first_elf_dash_index = pair_array[0].find('-')
  second_elf_dash_index = pair_array[1].find('-')

  sorted_pair = [[int(pair_array[0][:first_elf_dash_index]), \
    int(pair_array[0][first_elf_dash_index + 1:])]]
  sorted_pair += [[int(pair_array[1][:second_elf_dash_index]), \
    int(pair_array[1][second_elf_dash_index + 1:])]]

  return check_for_overlap(sorted_pair)

def sort_into_pairs(input_array):
  overlap_pair_count = 0
  for pair in input_array:
    overlap_pair_count += sort_pairs(pair)
  print(overlap_pair_count)

# main chunk
def main():
  sort_into_pairs( \
    base_code.process_input_file(INPUT_FILE_PATH))

main()