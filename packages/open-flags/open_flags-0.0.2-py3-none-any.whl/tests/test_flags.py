import unittest
from open_flags import get_flag_svg, get_all_flags, get_flags_by_country

class TestFlagFunctions(unittest.TestCase):
    def test_get_flag_svg(self):
        svg = get_flag_svg('usa', 'colorado')
        self.assertIn('<svg', svg)

    def test_get_all_flags(self):
        flags = get_all_flags()
        self.assertGreater(len(flags), 0)

    def test_get_flags_by_country(self):
        flags = get_flags_by_country('usa')
        self.assertGreater(len(flags), 0)

if __name__ == '__main__':
    unittest.main()
