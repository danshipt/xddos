DDoS protection system 
======================

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

For example, if there is a more then 35 (default) requests from some IP to, say, url (2), then this IP is blocked.


Installation
============

Real world installation.

NOTE: Remove --dry-run flag while in production.

<pre>

pip install --upgrade pip
pip install xddos

# or to upgrade
# $ pip install xddos --upgrade

mkdir -p /usr/local/xddos/tmp

# using tlog from BFD utility
cp /usr/local/bfd/tlog /usr/local/xddos/

# update BASERUN in /usr/local/xddos/tlog
# BASERUN="/usr/local/xddos/tmp"

echo "" > /usr/local/xddos/xddos_run.sh
chmod +x /usr/local/xddos/xddos_run.sh

Put this in /usr/local/xddos/xddos_run.sh
-----------
#!/bin/bash

/usr/local/xddos/tlog /var/log/nginx/access.log nginxlog | /usr/bin/xddos.py -p /var/run/xddos.pid -f nginx -b apf --dry-run --stdin >/usr/local/xddos/stats.log 2>&1

exit 0
------------


echo "*/1 * * * * root /usr/local/xddos/xddos_run.sh" > /etc/cron.d/xddos
/etc/init.d/crond restart
</pre>


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
