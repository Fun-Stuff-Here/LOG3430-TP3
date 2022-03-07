#!/bin/bash
python3 -m unittest test_crud.py
coverage run -m unittest test_crud.py
coverage report
cmd.exe