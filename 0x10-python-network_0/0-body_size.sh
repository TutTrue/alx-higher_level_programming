#!/bin/bash
# takes a url sends a request and display the content-length
curl -sI "$1" | grep content-length | grep -o '[0-9]\+'
