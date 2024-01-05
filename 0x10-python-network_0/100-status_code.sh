#!/bin/bash
# Script that sends a GET request to a given URL and dispaly response
curl -s -o /dev/null -w "%{http_code}" "$1"
