import base_code

INPUT_FILE_PATH = '.\\day3_text.txt'
# INPUT_FILE_PATH = '.\\day3_text_example.txt' # example answer is 157

# finds the wrong item and returns the priority (int)
def get_wrong_item(rucksack):
  first_compartment = rucksack[:len(rucksack) // 2]
  second_compartment = rucksack[len(rucksack) // 2:]

  for first_item in first_compartment:
    for second_item in second_compartment:
      if first_item == second_item:
        if ord(first_item) < 91:
          return ord(first_item) - 38
        return ord(first_item) - 96

# goes through all the rucksacks and adds the priority to a total
def sort_rucksacks(input_array):
  total_priority = 0
  for rucksack in input_array:
    total_priority += get_wrong_item(rucksack)
  print(total_priority)

# main chunk
def main():
  sort_rucksacks( \
    base_code.process_input_file(INPUT_FILE_PATH))

main()