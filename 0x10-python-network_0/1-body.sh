#!/bin/bash
# Bash script that takes in a URL, sends a GET request and displays only the  body of a 200 status code response
curl -sX GET "$1" -L
