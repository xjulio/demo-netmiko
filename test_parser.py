from unittest import TestCase
import my_parser

json_file = "files/myfile.json"
json_file2 = "files/myfile2.json"

class TestParser(TestCase):
    def test_parser_json(self):
        r = my_parser.parse_json(json_file)
        self.assertIsNot(r, None)

    def test_parser_json2(self):
        r = my_parser.parse_json(json_file2)
        self.assertEqual(r, {})
        
