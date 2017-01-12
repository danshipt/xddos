#!/usr/bin/env bash

#
# Installer for XDDoS
#
# Basic usage:
#   bash <(curl https://raw.githubusercontent.com/servancho/xddos/master/install.sh)
#
# If you want to check script contents:
#   wget https://raw.githubusercontent.com/servancho/xddos/master/install.sh
#   bash install.sh
#


echo "Install PIP"
wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm -f get-pip.py

echo "Installing XDDoS"
pip install pip --upgrade --no-cache-dir
pip install xddos --no-cache-dir

if [ ! -f /usr/share/xddos ]; then
    cp -r /usr/lib/python2.6/site-packages/usr/share/xddos /usr/share/xddos
    chmod +x /usr/share/xddos/*.sh
fi

echo ""
echo "==========================================================="
echo "XDDoS installed"

echo "Edit the parameters of protection:"
echo "$ vi /usr/share/xddos/runner.sh"

echo "Enable protection:"
echo "$ /usr/share/xddos/enable.sh"

echo "Disable protection:"
echo "$ /usr/share/xddos/disable.sh"
echo "==========================================================="

exit 0
