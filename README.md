# small-tic-tac-toe-engine

This is a small Tic-Tac-Toe engine a build for learning purpose

## How this works?

### To start the board in initial position, you can simply do:

```python main.py computer=1 "board=[0,0,0, 0,0,0, 0,0,0]"```


or if you'd like to initialize computer as "O" instead of "X"

```python main.py computer=2 "board=[0,0,0, 0,0,0, 0,0,0]"```

---

### The piece are:
0 = Empty<br />
1 = X<br />
2 = O<br />

The board is represented as an array of size 9

![File:Tic-tac-toe-game-1.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tic-tac-toe-game-1.svg/479px-Tic-tac-toe-game-1.svg.png)

Image from: [Wikipedia](https://en.wikipedia.org/wiki/File:Tic-tac-toe-game-1.svg)

The image above can be represented as the following:

1. [0, 0, 1,  0, 0, 0,  0, 0, 0]

```python main.py computer=2 board=[0,0,1, 0,0,0, 0,0,0]```

2. [2, 0, 1,  0, 0, 0,  0, 0, 0]

```python main.py computer=2 board=[2,0,1, 0,0,0, 0,0,0]```

3. [2, 0, 1,  0, 0, 0,  1, 0, 0]

```python main.py computer=2 board=[2,0,1, 0,0,0, 1,0,0]```

4. [2, 0, 1,  0, 2, 0,  1, 0, 0]

```python main.py computer=2 board=[2,0,1, 0,2,0, 1,0,0]```

5. [2, 0, 1,  0, 2, 0,  1, 0, 1]

```python main.py computer=2 board=[2,0,1, 0,2,0, 1,0,1]```

6. [2, 0, 1,  0, 2, 2,  1, 0, 1]

```python main.py computer=2 board=[2,0,1, 0,2,2, 1,0,1]```

7. [2, 0, 1,  0, 2, 2,  1, 1, 1]

```python main.py computer=2 board=[2,0,1, 0,2,2, 1,1,1]```

### ```result=YOU WIN! board=[2, 0, 1, 0, 2, 2, 1, 1, 1]```