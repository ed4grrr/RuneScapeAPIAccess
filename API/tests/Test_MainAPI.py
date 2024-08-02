import unittest
from unittest.mock import patch, MagicMock

import API.util.Runescape_HiScores_URL_Templates as URL_templates
from API.src._MainAPI import _API, Request


class _MainAPITestCase(unittest.TestCase):

    def setUp(self):
        self.mainAPItest = _API()
        self.userAgent = "DOING-IMPORTANT-TESTING"

    def test__clean_user_inputs(self):
        # entries to test
        args = ["player name", "skill/ID", "#dogg ", "_$@^edgar "]
        results = self.mainAPItest._clean_user_inputs(args)
        answer_key = ['player%20name', 'skill/ID', '%23dogg%20', '_%24%40%5Eedgar%20']
        self.assertListEqual(results, answer_key)  # add assertion here

    @patch('API.src._MainAPI.Request')
    def test__create_Request_from_URL_template(self, mock_request):
        # url and name to be used
        mock_request.return_value = "MockRequestObject"
        test_URL_template = "https://secure.runescape.com/m=hiscore/index_lite.ws?player=Zezima"
        user_entry_no_space = ["Zezima"]

        result_key = "MockRequestObject"
        result = self.mainAPItest._create_Request_from_URL_template(URL_templates.hiscores_lite_URL, self.userAgent,
                                                                    user_entry_no_space)
        mock_request.assert_called_once_with(test_URL_template, headers={'User-Agent': self.userAgent})
        self.assertEqual(result, result_key)

    @patch('API.src._MainAPI.urlopen')
    def test__call_API(self, mock_urlopen):
        mock_request = Request("https://secure.runescape.com/m=hiscore/index_lite.ws?player=Zezima")
        mock_urlopen.return_value = MagicMock(read=lambda: "API Response")
        result = self.mainAPItest._call_API(mock_request)
        self.assertEqual(result.read(), "API Response")

    @patch('API.src._MainAPI.Request')
    @patch('API.src._MainAPI.urlopen')
    def test_request_and_decode_API_response(self, mock_request, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"data": "value"}'
        mock_urlopen.return_value = mock_response
        mock_request.return_value = Request("https://secure.runescape.com/m=hiscore/index_lite.ws?player=Zezima")

        result = self.mainAPItest._request_and_decode_API_response(URL_templates.hiscores_lite_URL, self.userAgent,
                                                                   ['Zezima'])

if __name__ == '__main__':
    unittest.main()
