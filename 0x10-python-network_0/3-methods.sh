#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
CURL -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev