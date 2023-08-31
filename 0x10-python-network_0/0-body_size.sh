#!/bin/bash
# this shows the curl size
curl -i $1 | grep Content-Length | tail -c 4
