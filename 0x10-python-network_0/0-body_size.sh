#!/bin/bash
# Sends a request and displays the size of the body of the response in bytes
curl -s "$1" | wc -c
