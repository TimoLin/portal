import json
import base64
from urllib.request import urlopen
import yaml
import sys
import os

def readSubs():
    '''
    Read the links from the subs.list file
    '''
    with open('sub.list') as f:
        subs = f.read().splitlines()
    return subs[0]

def filterOutVless(content,orig_file):
    '''
    Filter out the VLESS nodes
    '''
    vlessNode = []
    for node in content['proxies']:
        if node['type'] == 'vless':
            content['proxies'].remove(node)
            vlessNode.append(node['name'])

    with open(orig_file) as f:
        lines = f.readlines()
        for line in lines:
            for node in vlessNode:
                if node in line:
                    lines.remove(line)
    with open('filtered.yml', 'w') as f:
        f.writelines(lines)

    return ( len(content['proxies'])-len(vlessNode) )

def main():
    nodeLinks = ''

    subLink = readSubs()
    
    # Use wget in python to download the yml and save it to a file
    #os.system(f'wget -O orig.yml {subLink}')
    
    # Use yaml to read the file
    with open('orig.yml') as stream:
        content = yaml.safe_load(stream)

    # Filter out the VLESS nodes
    n_nodes = filterOutVless(content, 'orig.yml')

    print("Original sub has {0} nodes", len(content['proxies'])
    print("Filter sub has {1} nodes",n_nodes)

if __name__ == "__main__":
    main()
