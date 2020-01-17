#!/bin/bash

TARGET="./mock/input"

inotifywait -m -e create -e moved_to --format "%f" $TARGET \
        | while read FILENAME
                do
                        echo Detected $FILENAME
                done