import base_code

INPUT_FILE_PATH = '.\\day2_text.txt'
# INPUT_FILE_PATH = '.\\day2_text_example.txt' # example answer is 15

ROCK = 1
PAPER = 2
SCISSORS = 3

PLAY_DICT = {'A': ROCK, 'B': PAPER, 'C': SCISSORS, 'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}

# takes two integers and calculates the win
def get_result(opponent_move, player_move):
  # draw
  if opponent_move - player_move == 0: return 3 + player_move

  # win
  if opponent_move - player_move == -1: return 6 + player_move
  if opponent_move - player_move == 2: return 6 + player_move

  return 0 + player_move

def get_score(input_array):
  total_points = 0
  for game in input_array:
    total_points += get_result(PLAY_DICT[game[0]], PLAY_DICT[game[2]])
  print(total_points)

# main chunk
def main():
  get_score( \
    base_code.process_input_file(INPUT_FILE_PATH))

main()