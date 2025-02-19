import sys
import unittest
from pintl import PIntl, _

class TestPintl(unittest.TestCase):
    def setUp(self):
        self.PIntl = PIntl.load("tests/l10n")
    
    def test_initialization(self):
        self.assertIsNotNone(self.PIntl)
    
    def test_en_translation(self):
        
        self.PIntl.set_locale('en')
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: Recording in background...")
    
    def test_fi_translation(self):
        
        self.PIntl.set_locale('fi')
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: tallentaa taustalla...")

    def test_default_lang(self):
        
        self.PIntl.set_locale('fr')
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: Recording in background...")
    
    def test_sublang(self):
        
        self.PIntl.set_locale('fi-SV')
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: tallentaa taustalla...")

if __name__ == '__main__':
    unittest.main()
