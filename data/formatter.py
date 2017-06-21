#-*-coding: utf-8-*-
from __future__ import unicode_literals
import json
import glob
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

files = glob.glob("*.json")

for f in files:
    content = {}
    with open(f, 'r') as input:
        content = json.load(input)
        if f == 'System.json':
            content['versionId'] = 12345678
    with open(f, "w") as output:
        formatted = json.dumps(content, indent=2, ensure_ascii=False, sort_keys=True).encode('utf-8')
        output.write(formatted)
