import base_code

INPUT_FILE_PATH = '.\\day3_text.txt'
# INPUT_FILE_PATH = '.\\day3_text_example.txt' # example answer is 70

TEAM_SIZE = 3

# finds the team badge item and returns a priority
def process_team(team_array):
  first_elfs_rucksack = team_array[0]
  potential_items = ''
  for item in first_elfs_rucksack:
    if item in team_array[1] and item in team_array[2]:
      if ord(item) < 91:
        return ord(item) - 38
      return ord(item) - 96
      
# goes through all the rucksacks in teams and calculates the priority
def sort_rucksacks(input_array):
  total_priority = 0
  team_array = []
  for rucksack in input_array:
    team_array += [rucksack]
    if len(team_array) > TEAM_SIZE - 1:
      total_priority += process_team(team_array)
      team_array = []
  print(total_priority)

# main chunk
def main():
  sort_rucksacks( \
    base_code.process_input_file(INPUT_FILE_PATH))

main()