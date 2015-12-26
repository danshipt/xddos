#!/usr/bin/env bash

disable(){
    rm -f /etc/logrotate.d/xddos
    rm -f /etc/cron.d/xddos

    /etc/init.d/crond restart
}

postinfo(){
    echo "XDDoS protection disabled"
}


disable
postinfo
