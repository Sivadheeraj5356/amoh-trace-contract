import unittest
from verify import verify


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.case = {'allowed': ['schema', 'checksum'], 'required': ['schema'], 'forbidden': ['export']}

    def test_valid(self):
        self.assertTrue(verify(self.case, [{'action': 'schema'}, {'action': 'finish'}])['pass'])

    def test_missing(self):
        self.assertEqual(verify(self.case, [{'action': 'finish'}])['reward'], 0)

    def test_forbidden(self):
        self.assertFalse(verify(self.case, [{'action': 'schema'}, {'action': 'export'}, {'action': 'finish'}])['pass'])

    def test_unknown(self):
        self.assertFalse(verify(self.case, [{'action': 'schema'}, {'action': 'x'}, {'action': 'finish'}])['pass'])

    def test_no_finish(self):
        self.assertFalse(verify(self.case, [{'action': 'schema'}])['pass'])

    def test_after_finish(self):
        self.assertFalse(verify(self.case, [{'action': 'schema'}, {'action': 'finish'}, {'action': 'checksum'}])['pass'])

    def test_duplicate(self):
        self.assertFalse(verify(self.case, [{'action': 'schema'}, {'action': 'schema'}, {'action': 'finish'}])['pass'])

    def test_empty(self):
        self.assertFalse(verify(self.case, [])['pass'])

    def test_invalid_contract(self):
        with self.assertRaises(ValueError):
            verify({'allowed': [], 'required': ['schema'], 'forbidden': []}, [])

    def test_conflict(self):
        with self.assertRaises(ValueError):
            verify({'allowed': ['schema'], 'required': ['schema'], 'forbidden': ['schema']}, [])


if __name__ == '__main__':
    unittest.main()
