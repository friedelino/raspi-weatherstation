#!/bin/env/bash

# fetch_weather_data.sh
#
# solely fetches weatherdata from raspi and saves it in WEATHERDIR.

OLD_PWD=$PWD
WEATHERDIR=~/Projects/weatherstation
REMOTE_WEATHERDIR=$WEATHERDIR

cd $WEATHERDIR
scp frido@pido:$REMOTE_WEATHERDIR/data.log .

cd $OLD_PWD
