import unittest
from snake.snake_class import Snake
class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_initial_length(self):
        self.assertEqual(len(self.snake.body), 1)

    def test_initial_direction(self):
        self.assertEqual(self.snake.direction, "right")

    def test_move_right(self):
        self.snake.move()
        self.assertEqual(self.snake.head, (0, 1))

    def test_move_left(self):
        self.snake.direction = "left"
        self.snake.move()
        self.assertEqual(self.snake.head, (0, -1))

    def test_move_up(self):
        self.snake.direction = "up"
        self.snake.move()
        self.assertEqual(self.snake.head, (-1, 0))

    def test_move_down(self):
        self.snake.direction = "down"
        self.snake.move()
        self.assertEqual(self.snake.head, (1, 0))

    def test_eat_food(self):
        self.snake.eat_food()
        self.assertEqual(len(self.snake.body), 2)

    def test_collision_with_self(self):
        self.snake.body = [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0)]
        self.snake.direction = "right"
        self.assertFalse(self.snake.is_collision())

    def test_collision_with_wall(self):
        self.snake.head = (0, 0)
        self.snake.direction = "up"
        self.assertTrue(self.snake.is_collision())

if __name__ == "__main__":
    unittest.main()
