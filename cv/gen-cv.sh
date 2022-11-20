#!/usr/bin/env bash

rm -f ./*.csv

gh repo list comp-physics --visibility public --source --json name,description,url > ./cpg.json
gh repo list mflowcode --visibility public --source --json name,description,url > ./mfc.json
gh repo list InertialMicrocavitationRheometry --visibility public --source --json name,description,url > ./imr.json

python3 parse.py

rm -f ./*.json

latexmk -c cv.tex
latexmk -pdf cv.tex

rm -f ./*.csv 
