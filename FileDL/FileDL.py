#!python3

"""
Downloads a file from a URL in the Web
"""

import requests

res = requests.get('https://en.wikipedia.org/wiki/Ros%C3%A9_(singer)#Life_and_career')

try:
  res.raise_for_status()
  
  playFile = open('Rosie.html', 'wb')
  
  for chunk in res.iter_content(100000):
    playFile.write(chunk)
  
  playFile.close()
except Exception as exc:
  print('There was a problem: %s ' % (exc))