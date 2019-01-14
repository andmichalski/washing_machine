import unittest
from wash_machine import callback

class WashMachineTests(unittest.TestCase):

    def test_write_callback(self):
        callback(17)
        callback(17)
        callback(17)

if __name__ == '__main__':
    unittest.main()

