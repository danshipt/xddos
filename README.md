HTTP flood analyzer 
===================

```
Optional arguments:
  -h, --help            show this help message and exit
  -p pid-file           PID lock file (default: None)
  -f {nginx}, --format {nginx}
                        Log file format. (default: nginx)
  -b {iptables,apf}, --blocker {iptables,apf}
                        Use specific blocker. (default: iptables)
  --dry-run             Do not block, just notify

Parser parameters.:
  --stdin               Data from stdin (default: False)
  -l LOG_FILE, --log LOG_FILE
                        Log file to process. (default: None)
```

## Basic usage

```
# analyze nginx logs and block via apf firewall 
tail -n 1000 /var/log/nginx/access.log | ./http_protector.py -p /var/run/httpprot.pid -f nginx -b apf --stdin
```

## DDoS analyzers

By default HTTP protector uses Generic flood analyzer. It counts requests from the specific IP to some URL targets and
block, based on threshold parameter.

The following urls are treated as the different targets:
* (1) http://attacktarget.com/main
* (2) http://attacktarget.com/dfjslkdjf?query=fdksjf
* (3) http://attacktarget.com/dfjslkdjf?query=3847587

For example, if there is a more then 10 (default) requests from some IP to, say, url (2), then this IP is blocked.
