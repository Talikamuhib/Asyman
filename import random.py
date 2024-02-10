import random
import os
import msvcrt

class Asyman:
    def __init__(self):
        self.rows = 10
        self.columns = 20
        self.player_row = 5
        self.player_col = 10
        self.food_row = random.randint(0, self.rows - 1)
        self.food_col = random.randint(0, self.columns - 1)
        self.score = 0
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]

    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.rows):
            for j in range(self.columns):
                if i == self.player_row and j == self.player_col:
                    print('A', end=' ')
                elif i == self.food_row and j == self.food_col:
                    print('F', end=' ')
                else:
                    print(self.board[i][j], end=' ')
            print()

    def move_player(self, direction):
        if direction == 'w':
            self.player_row = max(0, self.player_row - 1)
        elif direction == 's':
            self.player_row = min(self.rows - 1, self.player_row + 1)
        elif direction == 'a':
            self.player_col = max(0, self.player_col - 1)
        elif direction == 'd':
            self.player_col = min(self.columns - 1, self.player_col + 1)

    def check_collision(self):
        if self.player_row == self.food_row and self.player_col == self.food_col:
            self.score += 1
            self.food_row = random.randint(0, self.rows - 1)
            self.food_col = random.randint(0, self.columns - 1)

    def run(self):
        print("Welcome to Asyman!")
        print("Use WASD to move. Press 'q' to quit.")
        while True:
            self.print_board()
            print("Score:", self.score)
            direction = msvcrt.getch().decode('utf-8')
            if direction == 'q':
                print("Game Over!")
                break
            self.move_player(direction)
            self.check_collision()

if __name__ == "__main__":
    game = Asyman()
    game.run()
