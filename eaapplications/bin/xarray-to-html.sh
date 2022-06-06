#!/bin/bash

jupyter nbconvert \
  --to html \
  --no-input $1.ipynb \
  --output html/$(date +%Y%m%d%H%M)-$1.html
