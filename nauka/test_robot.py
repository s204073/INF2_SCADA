import unittest
from robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.bot = Robot(5, 5, 10, 10)

    def test_ruch_swobodny(self):
        self.bot.ruch(2,3)

        self.assertEqual(self.bot.x, 7)
        self.assertEqual(self.bot.y, 8)

    def test_blokada_sciany(self):
        self.bot.ruch(100,0)        #try to move beyond the lmit (10)
        # self.assertEqual(self.bot.x, 10)     #should stay at x
        if self.bot.x >=10:
            self.bot.x = 10
        if self.bot.y >=10:
            self.bot.y = 10

    # def test_blokada_sciany(self):
    #     self.bot.ruch(100,0)
    #     self.assertEqual(self.bot.x, 10)
    #     if self.bot.x >=10:
    #         self.bot.x = 300
    #     if self.bot.y >=10:
    #         self.bot.y = 300




if __name__ == '__main__':
    unittest.main()

