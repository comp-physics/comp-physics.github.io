#!/usr/bin/env python
import pandas as pd
import json

groups = ["cpg","mfc","imr"]
for grp in groups:
    # Load json from gh
    fn = grp + ".json"
    obj  = json.load(open(fn))

    # Ignore these repositories
    ignore_names = [".github", "comp-physics.github.io", "MFlowCode.github.io", "benchmark", "stats", "qce23-qpde-tutorial", "IMR_simple", "IMR-simple"]
    for ig in ignore_names:
        for i in range(len(obj)):
            if obj[i]["name"] == ig:
                obj.pop(i)
                break

    myinp = json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
    df = pd.read_json(myinp)

    # Get rid of stuf that TeX won't like
    df = df.replace('_','-',regex=True)
    df = df.replace('@','at',regex=True)

    # CSV file to read from github
    df.to_csv("github-" + grp + ".csv", encoding='utf-8', index=False)
