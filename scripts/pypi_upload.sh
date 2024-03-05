#!/bin/bash

rm -rf build dist bananagotchi.egg-info &&
  python3 setup.py sdist bdist_wheel &&
  clear &&
  twine upload dist/*
