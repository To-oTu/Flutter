import unittest
from health_check import check_communication

class TestHealthCheck(unittest.TestCase):

    def test_check_communication_returns_zero(self):
        self.assertEqual(check_communication(), 0, "check_communication should return 0")

if __name__ == '__main__':
    unittest.main()
