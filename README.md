Game of Sticks!

In the Game of Sticks there is a heap of sticks on a board. On their turn, each player picks up 1 to 3 sticks. The one who has to pick the final stick will be the loser.

The player may choose to play against another person or against the AI. In either case, the starting number of sticks on the board is chosen when the game begins. The count can be between 10 and 100 (inclusive).

When playing against the AI, the computer will learn after each round's win or loss. It does so by creating a dictionary for each possible number of sticks on the board with a list of [1, 2, 3] for each. Every round it selects randomly from the list corresponding to the number of sticks on the board and picks up that number. It tracks the choice each time and at the end of the round will either add or remove the choices from the corresponding dictionary entry. That is, if the computer lost and had selected to pick up 2 sticks when there were 7 on the board, the next round it will only choose 1 or 3 sticks when 7 are on the board. Conversely, it would have a choice of [1, 2, 2, 3] if it had won with that choice.
