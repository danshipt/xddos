#!/usr/bin/env bash

# Nginx access log
NGINX_LOG=/var/log/nginx/access.log

# XDDoS protection log
XDDOS_LOG=/var/log/xddos.log

# Number of requests on the specific URL per minute
THRESHOLD=45

# Block source IPs using this firewall
FIREWALL=iptables


TLOG=/usr/share/xddos/tlog.sh
if [ ! -f ${NGINX_LOG} ]; then
    echo "Nginx access log is not found: ${NGINX_LOG}. Nginx is installed?"
    exit 1
fi

${TLOG} ${NGINX_LOG} nginxlog | xddos -p /var/run/xddos.pid -f nginx --threshold ${THRESHOLD} -b ${FIREWALL} --stdin >>${XDDOS_LOG} 2>&1
