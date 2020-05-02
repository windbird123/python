import unittest

import my_program


class MyTestCase(unittest.TestCase):
    def test_add(self):
        add_result = my_program.add(1, 2)
        self.assertEqual(add_result, 3)


if __name__ == '__main__':
    unittest.main()
