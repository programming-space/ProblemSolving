import random
board = {
    2: -1, 4: -3, 9: -2, 21: -8, 28: -10, 51: -15, 80: -20,
    3: 7, 10: 12, 23: 15, 36: 15, 40: 10, 54: 22, 75: 10,
    5: 10, 11: 5, 14: 8, 25: 5, 38: 5, 45: 5, 70: 5,
}
def roll_dice():
    return random.randint(1, 6)
def move_player(player, position, dice_roll):
    new_position = position + dice_roll
    if new_position in board:
        effect = board[new_position]
        if effect > 0:
            print(f"{player} found a ladder and climbed to {new_position + effect}")
        else:
            print(f"{player} landed on a slide and moved down to {new_position + effect}")
        new_position += effect
    else:
        print(f"{player} moved to {new_position}")
    return new_position
def slide_and_ladder_game():
    player1 = input("Enter name of Player 1: ")
    player2 = input("Enter name of Player 2: ")
    player1_position = 0
    player2_position = 0
    while player1_position < 100 and player2_position < 100:
        input(f"{player1}, press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"{player1} rolled a {dice_roll}")
        player1_position = move_player(player1, player1_position, dice_roll)
        if player1_position >= 100:
            print(f"Congratulations! {player1} wins!")
            break
        input(f"{player2}, press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"{player2} rolled a {dice_roll}")
        player2_position = move_player(player2, player2_position, dice_roll)
        if player2_position >= 100:
            print(f"Congratulations! {player2} wins!")
            break

slide_and_ladder_game()