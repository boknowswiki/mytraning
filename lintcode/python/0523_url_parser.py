#!/usr/bin/python -t


import re

class HtmlParser:
    """
    @param: content: content source code
    @return: a list of links
    """
    def parseUrls(self, content):
        # write your code here
        links = re.findall("[Hh][Rr][Ee][Ff]\s*=\s*['\"](.*?)['\"]", content, re.I)
        links = [link for link in links if len(link) and not link.startswith('#')]
        return list(links)


import re

class HtmlParser:
    """
    @param: content: content source code
    @return: a list of links
    """
    def parseUrls(self, content):
        # write your code here
        pattern="(?:href|HREF)\s*=\s*(?:'|\")([^\s]*?)(?:'|\")"
        urls=re.findall(pattern,content)
        return [url for url in urls if len(url) and not url.startswith("#")]
