import json
import base64
from urllib.request import urlopen


subs = [
        #"https://iwxf.netlify.app",
        #"https://raw.githubusercontent.com/freefq/free/master/v2",
        #"https://raw.githubusercontent.com/ssrsub/ssr/master/ss-sub"
        #"https://raw.githubusercontent.com/ssrsub/ssr/master/V2Ray"
        #"https://raw.githubusercontent.com/vveg26/GetNode/master/Eternity"
        #https://raw.githubusercontent.com/ripaojiedian/freenode/main/sub
        "https://raw.githubusercontent.com/zhangkaiitugithub/passcro/main/speednodes.yaml"
        ]

def str2Bas64(link):
    return base64.urlsafe_b64encode(link.encode('utf-8')).decode()

def main():
    nodeLinks = ''
    '''
    for subLink in subs:
        fetchContent = urlopen(subLink).read()
        fetchLinks = base64.b64decode(fetchContent).decode('utf-8')
        nodeLinks += fetchLinks
    '''
    for subLink in subs:
        content = urlopen(subLink).read()
    print(content)   
    #content = str2Bas64(nodeLinks)
    
    with open("index.html",'wb') as f:
        f.write(content)

    # Return node numbers
    print (len(nodeLinks.splitlines()))

if __name__ == "__main__":
    main()
