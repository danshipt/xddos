from __future__ import unicode_literals


class GenericDDoSAnalyzer(object):
    def __init__(self, data_provider, threshold=150):
        assert data_provider

        self.data_provider = data_provider
        self.threshold = threshold

    def attacker_ip_list(self):
        """
        Returns the list of IPs to block.
        """
        parsed_data_map = {}
        for log_record in self.data_provider:
            if log_record.request_uri not in parsed_data_map:
                parsed_data_map[log_record.request_uri] = {}

            if log_record.ip not in parsed_data_map[log_record.request_uri]:
                parsed_data_map[log_record.request_uri][log_record.ip] = 0

            parsed_data_map[log_record.request_uri][log_record.ip] += 1

        # find top request IPs
        filtered_ips = {}
        for ip_count_map in parsed_data_map.values():
            for ip in ip_count_map:
                if ip_count_map[ip] < self.threshold:
                    continue

                if ip not in filtered_ips:
                    filtered_ips[ip] = ip_count_map[ip]
                elif filtered_ips[ip] < ip_count_map[ip]:
                    filtered_ips[ip] = ip_count_map[ip]

        return filtered_ips.keys()
