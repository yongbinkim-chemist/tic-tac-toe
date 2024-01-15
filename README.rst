TIC-TAC-TOE GAME
=================
`Tic-tac-toe <https://en.wikipedia.org/wiki/Tic-tac-toe>`__ is a game for two players who take turns making the spaces in a 3X3 grid with X or O.
The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.
It is a solved game, with a forced draw assuming best play from both players.

In order to create game AI that attemps to beat human being, `Minimax <https://en.wikipedia.org/wiki/Minimax>`__ with `Alpha-beta pruning <https://en.wikipedia.org/wiki/Alpha–beta_pruning#:~:text=Alpha–beta%20pruning%20is%20a,Connect%204%2C%20etc.).>`__ is implemented.

Requirements
------------
- Python 3+

How to play
------------
.. code-block:: bash

  git clone https://github.com/yongbinkim-chemist/tic-tac-toe.git
  cd tic-tac-toe
  python play_tic-tac-toe.py

- Select difficulty of the game:
  1.Easy: random
  2.Medium: 50% random / 50% minimax
  3.Hard: 100% minimax
- Select who will play the fist
  1.Human
  2.CPU
- Try to beat AI CPU

Authors
-------
`Yongbin Kim <https://github.com/yongbinkim-chemist>`__ (University of Southern California),
