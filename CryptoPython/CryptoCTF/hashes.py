import requests
import re
import os
import concurrent.futures


def isHash(string):
    # TODO return True if looks like hash, else False
    return True

def decodeHash(hashStr):
    def beta(hashvalue, hashtype):
        response = requests.get('https://hashtoolkit.com/reverse-hash/?hash=' + hashvalue).text
        match = re.search(r'/generate-hash/?text=.*?"', response)
        if match:
            return match.group(1)
        else:
            return False
    
    def gamma(hashvalue, hashtype):
        response = requests.get('https://www.nitrxgen.net/md5db/' + hashvalue, verify=False).text
        if response:
            return response
        else:
            return False
    
    def theta(hashvalue, hashtype):
        response = requests.get('https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=deanna_abshire@proxymail.eu&code=1152464b80a61728' % (hashvalue, hashtype)).text
        if len(response) != 0:
            return response
        else:
            return False
    
    md5 = [gamma, alpha, beta, theta, delta]
    sha1 = [alpha, beta, theta, delta]
    sha256 = [alpha, beta, theta]
    sha384 = [alpha, beta, theta]
    sha512 = [alpha, beta, theta]
    
    
    result = False
    if len(hashvalue) == 32:
        for api in md5:
            r = api(hashvalue, 'md5')
            if r:
                return r
    elif len(hashvalue) == 40:
        for api in sha1:
            r = api(hashvalue, 'sha1')
            if r:
                return r
    elif len(hashvalue) == 64:
        for api in sha256:
            r = api(hashvalue, 'sha256')
            if r:
                return r
    elif len(hashvalue) == 96:
        for api in sha384:
            r = api(hashvalue, 'sha384')
            if r:
                return r
    elif len(hashvalue) == 128:
        for api in sha512:
            r = api(hashvalue, 'sha512')
            if r:
                return r
    else:
        if not file:
            quit()
        else:
            return False