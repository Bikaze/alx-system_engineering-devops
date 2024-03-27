#!/bin/bash
# This script takes in a URL and displays the size of the body the response
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
