import re


def summary(s):
    return re.sub(r'дождь', replacer, s)
   # return re.sub(r'(\d+)%', lambda m: str(int(m.group(1)) / 100), s)

def replacer(match):
    return 'снег'