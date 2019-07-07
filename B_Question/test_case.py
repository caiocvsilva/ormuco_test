import unittest
import version

class QuestionBTest(unittest.TestCase):

    """
    Test all the basics version cases.
    
    This unit test check for equal, greater and less version strings. 
    
    Cases where the string was not a version were not tested since it can be in the Legacy format.
    """

    def test_version_equal(self):
        version1 = '1.9.a.dev'
        version2 = '1.9.a.dev'
        expected = version1+' is equal to '+version2
        self.assertEqual(expected, version.compare_version(version1, version2))

    def test_version_equal_no_point(self):
        version1 = '1.0.0.0'
        version2 = '1'
        expected = version1+' is equal to '+version2
        self.assertEqual(expected, version.compare_version(version1, version2))

    def test_version1_greater(self):
        version1 = '2.9.a.dev'
        version2 = '1.9.a.dev'
        expected = version1+' is greater than '+version2
        self.assertEqual(expected, version.compare_version(version1, version2))

    def test_version1_less(self):
        version1 = '0.9.a.dev'
        version2 = '1.9.a.dev'
        expected = version1+' is less than '+version2
        self.assertEqual(expected, version.compare_version(version1, version2))

    
if __name__ == '__main__':
    unittest.main()