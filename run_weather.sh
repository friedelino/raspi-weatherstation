#!/usr/bin/env bash

OLD_PWD=$PWD
WEATHERDIR=~/Projects/weatherstation
REMOTE_WEATHERDIR=$WEATHERDIR

cd $WEATHERDIR
scp frido@pido:$REMOTE_WEATHERDIR/data.log .

# Wayland needs QT_QPA_PLATFORM=xcb for matplotlib
# Default: display weatherdata for last 3 days
QT_QPA_PLATFORM=xcb python3 ./raspi-weatherstation.py -d 3

cd $OLD_PWD
