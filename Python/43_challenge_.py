"""
I could not solve this problem can you help:

Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally.The rules of the game are as follows:

Initially there are n towers.
Each tower is of height m.
The players move in alternating turns.
In each turn, a player can choose a tower of height x and reduce its height to y , where 1<=y<x and y evenly divides x .
If the current player is unable to make a move, they lose the game.
Given the values of n and m, determine which player will win. If the first player wins, return 1 . Otherwise, return 2.

Example. 

There are  towers, each  units tall. Player  has a choice of two moves:
- remove  pieces from a tower to leave  as 
- remove  pieces to leave 

Let Player  remove . Now the towers are  and  units tall.

Player  matches the move. Now the towers are both  units tall.

Now Player  has only one move.

Player  removes  pieces leaving . Towers are  and  units tall.
Player  matches again. Towers are both  unit tall.

Player  has no move and loses. Return .

"""


def tower_breakers(n, m):
    # If the height of towers is 1, Player 2 wins automatically
    if m == 1:
        return 2
    # If the number of towers is odd, Player 1 wins
    elif n % 2 == 1:
        return 1
    # If the number of towers is even, Player 2 wins
    else:
        return 2