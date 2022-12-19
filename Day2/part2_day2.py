import base_code

INPUT_FILE_PATH = '.\\day2_text.txt'
# INPUT_FILE_PATH = '.\\day2_text_example.txt' # example answer is 12

ROCK = 1
PAPER = 2
SCISSORS = 3

PLAY_DICT = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}

# takes an integer and a letter and calculates the points
def get_result(opponent_move, outcome):
  if outcome == 'X':
    if opponent_move == 1:
      return 2
    return 0 + opponent_move - 1
  elif outcome == 'Y':
    return 3 + opponent_move
  else:
    if opponent_move == 3:
      return 7
    return 6 + opponent_move + 1

def get_score(input_array):
  total_points = 0
  for game in input_array:
    total_points += get_result(PLAY_DICT[game[0]], game[2])
  print(total_points)

# main chunk
def main():
  get_score( \
    base_code.process_input_file(INPUT_FILE_PATH))

main()