#!/bin/bash
# POST a json file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
