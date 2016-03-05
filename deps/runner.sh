#!/usr/bin/env bash

TLOG=/usr/share/xddos/tlog.sh
NGINX_LOG=/var/log/nginx/access.log
XDDOS_LOG=/var/log/xddos.log

if [ ! -f ${NGINX_LOG} ]; then
    echo "Nginx access log is not found: ${NGINX_LOG}. Nginx is installed?"
    exit 1
fi

${TLOG} ${NGINX_LOG} nginxlog | xddos -p /var/run/xddos.pid -f nginx --threshold 45 -b iptables --stdin >>${XDDOS_LOG} 2>&1
