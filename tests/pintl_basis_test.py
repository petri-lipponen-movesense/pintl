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
        result = self.PIntl.get_string("notification_text")
        self.assertEqual(result, "Movesense ECG: Recording in background...")
    
    def test_fi_translation(self):
        
        self.PIntl.set_locale('fi')
        result = self.PIntl.get_string("notification_text")
        self.assertEqual(result, "Movesense ECG: tallentaa taustalla...")

    def test_en_parameter(self):
        
        self.PIntl.set_locale('en')
        result = self.PIntl.get_string("share_format", {'format': 'CSV'})
        self.assertEqual(result, "Share CSV file?")

        result = self.PIntl.get_string("duration", {'days': 25})
        self.assertEqual(result, "Duration is 25 days.")
        
    
    def test_fi_parameter(self):
        
        self.PIntl.set_locale('fi')
        result = self.PIntl.get_string("share_format", {'format': 'CSV'})
        self.assertEqual(result, "Jaa CSV tiedosto?")

        result = self.PIntl.get_string("duration", {'days': 23})
        self.assertEqual(result, "Kesto on 23 päivää.")

    def test_default_lang(self):
        
        self.PIntl.set_locale('fr')
        result = self.PIntl.get_string("notification_text")
        self.assertEqual(result, "Movesense ECG: Recording in background...")
    
    def test_default_string(self):
        
        self.PIntl.set_locale('fr')
        result = _("non_existing_text")
        self.assertEqual(result, "##non_existing_text##")

    def test_sublang(self):
        
        self.PIntl.set_locale('fi-SV')
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: tallentaa taustalla...")

        # Reset setting
        self.PIntl.set_locale('fr')
        result = _("non_existing_text")
        self.assertEqual(result, "##non_existing_text##")

        # Make sure that one with underscore is works as well (Android/flutter sends these)
        self.PIntl.set_locale('fi_SV')
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: tallentaa taustalla...")


    def test_bad_setlocale(self):
        
        self.PIntl.set_locale("fi")

        self.PIntl.set_locale(None)
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: Recording in background...")


        self.PIntl.set_locale("")
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: Recording in background...")

        self.PIntl.set_locale("fiFI")
        result = _("notification_text")
        self.assertEqual(result, "Movesense ECG: Recording in background...")

        self.PIntl.set_locale("fyfantasy")
        result = _("duration", {'days': 25})
        self.assertEqual(result, "Duration is 25 days.")

if __name__ == '__main__':
    unittest.main()
