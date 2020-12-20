# TicTacToe

This TicTacToe allows you to play against the program that analyzes the board to find the best way to deafeat you.

# Algorythm 
After every round, the programm will analyze the board using the following method

## Look at every row, column and diagonal
- If he finds 2 of these  points and an empty case, then he will got a winnable play.
- Otherwise he find 2 of your points and an empty case, he will get a vital counter play 
- Otherwise he find 1 of these point and 2 empty cases, he will got a good play.
- Otherwise will choose a random case

If he has no chance to win or counter-play, he will check if he can play middle or corner cases.

![tictactoe](https://user-images.githubusercontent.com/72104477/102715659-451f1980-42d7-11eb-91db-ecaf83d9a92c.jpg)
