import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t')
        self.g1.guess('s')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t')

    def testDisplayGuessed(self):
        self.g1.guess('e')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayGuessed(), 'e n')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), 'a e n')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t u')
        self.g1.guess('s')
        self.assertEqual(self.g1.displayGuessed(), 'a e n s t u')
        self.g1.guess('s')
        self.assertEqual(self.g1.displayGuessed(), 'a e n s t u')

    def testguess(self):
        self.assertTrue(self.g1.guess('t'))
        self.assertEqual(self.g1.displayGuessed(), 't')
        self.assertEqual(self.g1.currentStatus, '______t')
        self.assertTrue(self.g1.guess('f'))
        self.assertEqual(self.g1.displayGuessed(), 'f t')
        self.assertEqual(self.g1.currentStatus, '__f___t')
        self.assertFalse(self.g1.guess('s'))
        self.assertEqual(self.g1.displayGuessed(), 'f s t')
        self.assertEqual(self.g1.currentStatus, '__f___t')
        self.assertTrue(self.g1.guess('d'))
        self.assertEqual(self.g1.displayGuessed(), 'd f s t')
        self.assertEqual(self.g1.currentStatus, 'd_f___t')
        self.assertTrue(self.g1.guess('u'))
        self.assertEqual(self.g1.displayGuessed(), 'd f s t u')
        self.assertEqual(self.g1.currentStatus, 'd_f_u_t')
        self.assertFalse(self.g1.guess('n'))
        self.assertEqual(self.g1.displayGuessed(), 'd f n s t u')
        self.assertEqual(self.g1.currentStatus, 'd_f_u_t')
        self.assertTrue(self.g1.guess('a'))
        self.assertEqual(self.g1.displayGuessed(), 'a d f n s t u')
        self.assertEqual(self.g1.currentStatus, 'd_fau_t')
        self.assertTrue(self.g1.guess('e'))
        self.assertEqual(self.g1.displayGuessed(), 'a d e f n s t u')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.assertFalse(self.g1.guess('p'))
        self.assertEqual(self.g1.displayGuessed(), 'a d e f n p s t u')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.assertTrue(self.g1.guess('l'))
        self.assertEqual(self.g1.displayGuessed(), 'a d e f l n p s t u')
        self.assertEqual(self.g1.currentStatus, 'default')
        
if __name__ == '__main__':
    unittest.main()