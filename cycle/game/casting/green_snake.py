import constants
from game.casting.snake import Red_Snake
from game.casting.actor import Actor
from game.shared.point import Point

class Green_Snake(Red_Snake):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()


    def _prepare_body(self):
        x = int(3 * constants.MAX_X / 4)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0,-1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"
        
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(constants.GREEN)
            self._segments.append(segment)