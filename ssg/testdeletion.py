import re
from yaml import load
from yaml import FullLoader
from collections.abc import Mapping


__delimiter = r"^(?:-|\+){3}\s*$"
__regex = re.compile(__delimiter, re.MULTILINE)


with open('content/index.md','r') as file:
    for line in file.readlines():
        _, fm, content = __regex.split(line, 2) 
        metadata = load(fm, Loader=FullLoader)


print(metadata)