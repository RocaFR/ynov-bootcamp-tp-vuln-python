#!/bin/bash
cd topsix
deactivate
source `pwd`/venv/bin/activate;

flask --debug run