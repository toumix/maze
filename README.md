Example:

```
>>> from maze import Maze, N, S, E, W
>>> m = Maze(size=(15, 15))
>>> print(m)
+   +-------------------+---------------+-----------+-------+
| v |                   |               |           |       |
|   +---+-----------+   +---+---+   +   |   +---+---+   +---+
|   |   |           |       |       |   |       |       |   |
|   |   +---+   +---+---+   +---+   +---+   +---+   +---+   |
|   |                               |                       |
|   +-------+-------+---+   +   +   +---+   +   +   +   +---+
|   |       |       |       |   |           |   |   |       |
|   +---+   +---+   +---+   |   +-------+   +---+---+---+---+
|           |       |       |   |                       |   |
+-------+   +---+   +-------+   |   +   +   +-----------+   |
|                   |       |   |   |   |                   |
|   +-----------+   +   +---+---+   |   +---+---+   +---+   |
|   |                               |       |   |       |   |
|   |   +   +   +   +   +   +---+   |   +---+   |   +---+---+
|   |   |   |   |   |   |   |       |       |   |           |
|   +---+---+   |   +---+---+   +---+   +   +   |   +   +---+
|   |           |   |   |   |   |       |       |   |   |   |
+---+   +---+   |   |   +   +---+   +   |   +   +---+---+   |
|       |   |   |   |               |   |   |               |
+---+   |   +   +---+-------+-------+   +---+   +---+   +   |
|       |       |           |               |       |   |   |
+-------+-------+-------+   +-------+   +---+---+   +---+   |
|                                               |   |       |
|   +   +   +---+   +   +---+   +---+   +-------+   |   +   |
|   |   |   |       |   |       |       |           |   |   |
+---+   |   +-------+---+   +   +---+   +---+   +---+   +---+
|       |   |               |       |   |       |           |
|   +---+---+   +-----------+   +---+   +---+   |   +   +   |
|           |   |                   |   |       |   |   |   |
+-----------+---+-------------------+---+-------+---+---+   |

>>> for d in [S, S, S, S, E, E, N, W]:
...     m.move(d)
>>> print(m)
+   +-------------------+---------------+-----------+-------+
| x |                   |               |           |       |
|   +---+-----------+   +---+---+   +   |   +---+---+   +---+
| x |   |           |       |       |   |       |       |   |
|   |   +---+   +---+---+   +---+   +---+   +---+   +---+   |
| x |                               |                       |
|   +-------+-------+---+   +   +   +---+   +   +   +   +---+
| x | <   x |       |       |   |           |   |   |       |
|   +---+   +---+   +---+   |   +-------+   +---+---+---+---+
| x   x   x |       |       |   |                       |   |
+-------+   +---+   +-------+   |   +   +   +-----------+   |
|                   |       |   |   |   |                   |
|   +-----------+   +   +---+---+   |   +---+---+   +---+   |
|   |                               |       |   |       |   |
|   |   +   +   +   +   +   +---+   |   +---+   |   +---+---+
|   |   |   |   |   |   |   |       |       |   |           |
|   +---+---+   |   +---+---+   +---+   +   +   |   +   +---+
|   |           |   |   |   |   |       |       |   |   |   |
+---+   +---+   |   |   +   +---+   +   |   +   +---+---+   |
|       |   |   |   |               |   |   |               |
+---+   |   +   +---+-------+-------+   +---+   +---+   +   |
|       |       |           |               |       |   |   |
+-------+-------+-------+   +-------+   +---+---+   +---+   |
|                                               |   |       |
|   +   +   +---+   +   +---+   +---+   +-------+   |   +   |
|   |   |   |       |   |       |       |           |   |   |
+---+   |   +-------+---+   +   +---+   +---+   +---+   +---+
|       |   |               |       |   |       |           |
|   +---+---+   +-----------+   +---+   +---+   |   +   +   |
|           |   |                   |   |       |   |   |   |
+-----------+---+-------------------+---+-------+---+---+   |
```
