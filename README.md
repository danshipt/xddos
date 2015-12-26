XDDoS - DDoS protection system
==============================

```
usage: xddos [-h] -p pid-file -f {nginx} -b {iptables,apf}
                [--threshold THRESHOLD] [--dry-run] [--stdin | -l LOG_FILE]

DDoS protection system

optional arguments:
  -h, --help            show this help message and exit
  -p pid-file           PID lock file (default: None)
  -f {nginx}, --format {nginx}
                        Log file format. (default: nginx)
  -b {iptables,apf}, --blocker {iptables,apf}
                        Use specific blocker. (default: iptables)
  --threshold THRESHOLD
                        Analyzer threshold. (default: 35)
  --dry-run             Do not block, just notify (default: False)

Parser parameters.:
  --stdin               Data from stdin (default: False)
  -l LOG_FILE, --log LOG_FILE
                        Log file to process. (default: None)

```

## Basic usage

```
# analyze nginx logs and block via apf firewall 
tail -n 1000 /var/log/nginx/access.log | xddos --dry-run -p /var/run/httpprot.pid -f nginx -b apf --stdin

# analyze nginx logs and block via iptables firewall 
tail -n 1000 /var/log/nginx/access.log | xddos --dry-run -p /var/run/httpprot.pid -f nginx -b iptables --stdin
```

NOTE: Remove --dry-run flag while in production.


## DDoS analyzers

By default HTTP protector uses Generic flood analyzer. It counts requests from the specific IP to some URL on the
server and block this IP based on threshold parameter.

The following urls are treated as the different targets:
* (1) http://attacktarget.com/main
* (2) http://attacktarget.com/dfjslkdjf?query=fdksjf
* (3) http://attacktarget.com/dfjslkdjf?query=3847587

For example, if there is a more then 35 (default) requests from some IP to, say, url (2), then this IP is blocked.


Installation
============

Install pip:
```
cd
wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

Installing app using pip
```
pip install pip --upgrade --no-cache-dir
pip install xddos

# or upgrade
# pip install xddos --upgrade --no-cache-dir

# test installed script
xddos -h
```

XDDoS can protect your server automatically. To do this, perform the following steps: 
```
cd /usr/share/xddos
./enable.sh

# to disable xddos
cd /usr/share/xddos
./disable.sh
```

Running tests
=============

Use nosetest to run tests. Install nosetests by running:
<code>
$ pip install nose
</code>

To run the project tests:
<code>
$ nosetests -w ./tests/
</code>
