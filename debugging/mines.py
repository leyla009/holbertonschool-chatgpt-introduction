#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mine_indices = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.revealed_count = 0
        self.total_safe_cells = (width * height) - mines

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mine_indices:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mine_indices:
                        count += 1
        return count

    def reveal(self, x, y):
        # Boundary check and already revealed check
        if not (0 <= x < self.width and 0 <= y < self.height) or self.revealed[y][x]:
            return True
        
        # Hit a mine
        if (y * self.width + x) in self.mine_indices:
            return False
        
        self.revealed[y][x] = True
        self.revealed_count += 1
        
        # If the cell is empty, reveal neighbors recursively
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    self.reveal(x + dx, y + dy)
        return True

    def play(self):
        while True:
            self.print_board()
            
            # Win condition
            if self.revealed_count == self.total_safe_cells:
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break
                
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
