#!/usr/bin/env bash

INSPATH="/usr/share/xddos"

enable(){
    chmod +x ${INSPATH}/*.sh

    cp ${INSPATH}/logrotate.d.xddos /etc/logrotate.d/xddos

    cp ${INSPATH}/cron /etc/cron.d/xddos
    chmod 644 /etc/cron.d/xddos

    /etc/init.d/crond restart
}

postinfo(){
    echo "XDDoS protection enabled"
}


enable
postinfo
