#!/bin/bash

jupyter nbconvert \
  --to html \
  --no-input 02-smap-hdf5-xarray.ipynb \
  --output html/$(date +%Y%m%d%H%M)-smap-hdf5-xarray.html
