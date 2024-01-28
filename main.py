# the main file where you run all the codes and 
# will import all functions from the second file

import functions as f

def main():
    grid = f.initialize_grid()
    print("Welcome to 2048!")
    f.print_grid(grid)

    while True:
        try:
            move = input("Enter move (w: up, s: down, a: left, d: right, q: quit): ").strip().lower()
            
            if move == 'q':
                break

            valid_moves = {'w': f.move_up, 's': f.move_down, 'a': f.move_left, 'd': f.move_right}
            # invalid move since pressed other keys
            if move not in valid_moves:
                raise ValueError("Invalid move, you can only move (w: up, s: down, a: left, d: right, q: quit): ")

            new_grid = valid_moves[move](grid)

        except ValueError as e:
            print(e)
        
        else:
            if new_grid != grid:
                grid = new_grid
                f.add_new_tile(grid)
                f.print_grid(grid)
                # reached 2048
                if f.find_max_tile(grid) == 2048:
                    print("Congratulations, you've reached 2048!")
                    break
                # can not move since can not merge after compress
                if not f.can_move(grid):
                    print("No more moves available. Game over!")
                    # add try again logic
                    while True:
                        move = input("Try again? Yes - Y, No - N: ").strip().lower()
                        if move == 'y':
                            grid = f.initialize_grid()  
                            f.print_grid(grid)          
                            break                       
                        elif move == 'n':
                            print("Thank you for playing!")  
                            exit()                           
                        else:
                            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
            else:
                print("Move not possible. Try again.")
        
        finally:
            pass


if __name__ == "__main__":
    main()
