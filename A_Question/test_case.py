import unittest
import overlap

class QuestionATest(unittest.TestCase):

    """
    Test all the basics overlap cases.
    
    This unit test check for positive overlaps, negative overlaps and examples with no overlap.
    """

    def test_positive_overlap(self):
        line1 = (1,5)
        line2 = (2,6)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_positive_overlap_x3_in_x1x2(self):
        line1 = (5,10)
        line2 = (6,12)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_positive_overlap_x1x2_in_x3x4(self):
        line1 = (5,10)
        line2 = (2,15)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_positive_overlap_x2_in_x3x4(self):
        line1 = (5,10)
        line2 = (2,7)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_positive_overlap_x3x4_in_x1x2(self):
        line1 = (5,10)
        line2 = (6,9)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_positive_overlap_x1x2_equals_x3x4(self):
        line1 = (5,10)
        line2 = (5,10)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_positive_overlap_inverted(self):
        line1 = (10,5)
        line2 = (9,6)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_negative_overlap(self):
        line1 = (-5,-10)
        line2 = (-6,-9)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_float_overlap(self):
        line1 = (5.7,10.2)
        line2 = (6.4,9.8)
        self.assertTrue(overlap.check_overlap(line1,line2))

    def test_no_overlap(self):
        line1 = (1,5)
        line2 = (6,8)
        self.assertFalse(overlap.check_overlap(line1,line2))


if __name__ == '__main__':
    unittest.main()