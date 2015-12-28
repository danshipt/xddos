from __future__ import unicode_literals

import re


class AccessLogRecord(object):
    def __init__(self):
        self.date = ''
        self.domain = ''
        self.ip = ''
        self.http_code = ''
        self.request_uri = ''


class NginxLogParser(object):
    pattern = re.compile(r''
                         '(\d+.\d+.\d+.\d+)\s-\s-\s'  # IP address
                         '\[(.+)\]\s'  # datetime
                         '"(.+)\s\w+/.+"(\s)["]*(\d+)["]*\s'  # request and HTTP code
                         '\d+\s"(.+)"\s'  # referrer
                         '"(.+)"\s+".+"\s+'  # user agent
                         '(.+)'  # domain
                         )

    def __init__(self, data_provider):
        assert data_provider

        self.data_provider = data_provider

    def __iter__(self):
        for log_line in self.data_provider:
            rec = self._parse_request(log_line)
            if rec:
                yield rec

    def _parse_request(self, log_line):
        record = None
        log_line = log_line.strip()

        mt = re.match(self.pattern, log_line)
        if mt:
            record = AccessLogRecord()
            record.date = mt.group(2)
            record.request_uri = mt.group(3)
            record.ip = mt.group(1)
            record.http_code = int(mt.group(5))
            record.domain = mt.group(8).lower()

        return record
