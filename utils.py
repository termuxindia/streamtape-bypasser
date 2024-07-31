#!/usr/bin/env python
import re
import requests


PREFIX='https:/'

def get_streamtape_url(url: str) -> str:
    html = requests.get(url).content.decode()
    token = re.match(r".*document.getElementById.*\('norobotlink'\).innerHTML =.*?token=(.*?)'.*?;", html, re.M|re.S).group(1)
    infix=re.match(r'.*<div id="ideoooolink" style="display:none;">(.*?token=).*?<[/]div>', html, re.M|re.S).group(1)
    final_URL=f'{PREFIX}{infix}{token}'
   
    return f"{final_URL}"