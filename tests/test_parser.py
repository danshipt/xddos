from __future__ import unicode_literals

import os
import unittest

from lib.analyzers import GenericDDoSAnalyzer
from lib.data_providers import FileDataProvider
from lib.nginx_log_parser import NginxLogParser


class TestDDoSAnalizer(unittest.TestCase):
    TESTLOG_PATH = os.path.join(os.path.dirname(__file__), 'access.log-mini')

    def test_dict_test(self):
        dict = {
            'dom1': {
                'ip1': 5,
                'ip2': 7,
                'ip3': 10,
            },
            'dom2': {
                'ip4': 5,
                'ip2': 70,
                'ip7': 10,
            },
            'dom3': {
                'ip3': 5,
                'ip2': 3,
                'ip9': 10,
            }
        }

        print dict.values()

    def test_analyze_minilog(self):
        minilog = self.TESTLOG_PATH

        log_parser = NginxLogParser(FileDataProvider(minilog))

        analyzer = GenericDDoSAnalyzer(log_parser, threshold=100)
        block_ips = analyzer.attacker_ip_list()

        self.assertEqual(5, len(block_ips))
        self.assertEqual('77.106.228.178', block_ips[0])
        self.assertEqual('190.195.160.2', block_ips[1])
        self.assertEqual('89.21.79.68', block_ips[2])
        self.assertEqual('46.118.121.72', block_ips[3])
        self.assertEqual('201.254.106.234', block_ips[4])

    def test_parse_minilog(self):
        minilog = self.TESTLOG_PATH

        log_parser = NginxLogParser(FileDataProvider(minilog))

        records_list = list(log_parser)

        self.assertEqual('46.118.121.72', records_list[0].ip)
        self.assertEqual(302, records_list[0].http_code)
        self.assertEqual('razdacha-akkauntov.ru', records_list[0].domain)

        self.assertEqual('201.254.106.234', records_list[261].ip)
        self.assertEqual(200, records_list[261].http_code)
        self.assertEqual('provoloka34.ru', records_list[261].domain)


if __name__ == '__main__':
    unittest.main()
