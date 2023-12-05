#!/bin/bash
# Script that takes an URL and displays the body of the response
curl -sX GET "$1" -H "X-School-User-Id: 98" -L
