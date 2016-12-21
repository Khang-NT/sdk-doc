import os
import sys
from bs4 import BeautifulSoup
import re

if len(sys.argv) > 1:
    htmlFile = sys.argv[1]
    with open(htmlFile) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, "html.parser")
    style_tag = soup.new_tag("style")
    style_tag.append(
        "ul.tab{list-style-type:none;margin:0;padding:0;overflow:hidden;border:0 solid #ccc;background-color:#f1f1f1}ul.tab li{float:left}ul.tab li a{display:inline-block;color:#000;text-align:center;padding:14px 16px;text-decoration:none;transition:.3s;font-size:17px}.tabcontent{display:none;margin:0;padding:0;border:0 solid #ccc;border:none}ul.tab li a:hover{background-color:#ddd}ul.tab li a:focus,.active{background-color:#ccc}.tabcontent{-webkit-animation:fadeEffect 1s;animation:fadeEffect 1s}@-webkit-keyframes fadeEffect{from{opacity:0}to{opacity:1}}@keyframes fadeEffect{from{opacity:0}to{opacity:1}}.s-content pre{background:#fbfbfb;padding:20px;margin:0}")
    soup.header.append(style_tag)

    script_tag = soup.new_tag("script")
    script_tag.append(
        "function openTab(evt,tab_content,active_id,tab_links){var i,tabcontent,tablinks;tabcontent=document.getElementsByClassName(tab_content);for(i=0;i<tabcontent.length;i++){tabcontent[i].style.display='none'}tablinks=document.getElementsByClassName(tab_links);for(i=0;i<tablinks.length;i++){tablinks[i].className=tablinks[i].className.replace(' active','')}document.getElementById(active_id).style.display='block';evt.currentTarget.className+=' active'}")
    soup.body.append(script_tag)

    html = str(soup)
    regex = r"(<pre><code class=\"language-([^\s\n\"]*).*?(?=\")\">.+?(?=<\/code>)<\/code><\/pre>)"

    matches = re.finditer(regex, html, re.DOTALL)

    count = 0
    blocks = []
    first_match = 0
    tabs = "<ul class='tab'>"
    last_end = -1
    insertCount = 0
    for matchNum, match in enumerate(matches):
        lang = match.group(2)

        if lang in blocks or (last_end != -1 and match.start() - last_end > 5):
            tabs += "</ul>"
            insertCount += len(tabs)
            html = html[:first_match] + tabs + html[first_match:]
            blocks = [lang]
            first_match = match.start() + insertCount
            count += 1
            tabs = "<ul class='tab'>"
            last_end = -1
        else:
            blocks.append(lang)
            last_end = match.end()

        print(matchNum)
        start = match.start() + insertCount
        end = match.end() + insertCount
        if len(blocks) == 1:
            first_match = start


        if lang == 'java':
            tabs += "\n<li><a href=\"javascript:void(0)\" class=\"tablinks tl%d\" onclick=\"openTab(event, 'tc%d', 'android%d', 'tl%d')\">Android</a></li>" % (
                count, count, count, count)
            html = html[:start] + "\n<div id='android%d' class='tabcontent tc%d'>\n" % (count, count) + html[start:end] + "\n</div>\n" + html[end:]
            insertCount += len("\n<div id='android%d' class='tabcontent tc%d'>\n" % (count, count) + "\n</div>\n")
        elif lang == 'swift':
            tabs += "\n<li><a href=\"javascript:void(0)\" class=\"tablinks tl%d\" onclick=\"openTab(event, 'tc%d', 'ios%d', 'tl%d')\">IOS</a></li>" % (
                count, count, count, count)
            html = html[:start] + "\n<div id='ios%d' class='tabcontent tc%d'>\n" % (count, count) + html[start:end] + "\n</div>\n" + html[end:]
            insertCount += len("\n<div id='ios%d' class='tabcontent tc%d'>\n" % (count, count) + "\n</div>\n")
        elif lang == 'javascript':
            tabs += "\n<li><a href=\"javascript:void(0)\" class=\"tablinks tl%d\" onclick=\"openTab(event, 'tc%d', 'web%d', 'tl%d')\">Web</a></li>" % (
                count, count, count, count)
            html = html[:start] + "\n<div id='web%d' class='tabcontent tc%d'>\n" % (count, count) + html[start:end] + "\n</div>\n" + html[end:]
            insertCount += len("\n<div id='web%d' class='tabcontent tc%d'>\n" % (count, count) + "\n</div>\n")

        print("Tab no:", count)
        print("Add lang:", lang)

    if blocks:
        tabs += "</ul>"
        html = html[:first_match] + tabs + html[first_match:]

    with open(htmlFile, 'w') as outFile:
        outFile.write(html)
