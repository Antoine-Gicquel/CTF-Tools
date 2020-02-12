import requests
import sys
import os
import libs.git_dumper


# Uses the git-dumper.py script from Maxime Arthaud and python-dirbuster.py from rek7

## main part
if __name__ == '__main__':
    if len(sys.argv) < 2 or (len(sys.argv) == 2 and '-v' in sys.argv):
        print("Things are missing. Usage: "+str(sys.argv[0])+" <url> (-v)")
        exit(-1)
    
    url = sys.argv[1]
    if url[-1] != '/':
        url += '/'
    
    verbosity = ('-v' in sys.argv)
    
    print("AutoCheckWeb by blueshit, 2019")
    print("Checking url : "+url)
    
    r = requests.get(url)
    if r.status_code == 404:
        print("There is an error with the URL, we got 404. Exiting")
        exit(-1)
    
    # check robots.txt
    r = requests.get(url+"robots.txt")
    if r.status_code != 404:
        print("** robots.txt found ! Here it is :")
        print(r.text)
    else:
        if verbosity:
            print("robots.txt file not found")
    
    # checks sitemap.xml
    r = requests.get(url+"sitemap.xml")
    if r.status_code != 404:
        print("** sitemap.xml found ! Here it is :")
        print(r.text)
    else:
        if verbosity:
            print("sitemap.xml file not found")
        
    # checks .git
    r = requests.get(url+".git/HEAD")
    if r.status_code != 404 and r.status_code != 403:
        print("** Git repository found ! Dumping it to ./gitdump")
        try:
            git_dumper.fetch_git(url, "./gitdump", 1, 2, 2)
            print("Git repo dumped !\nDo not forget to run \"git checkout .\" or \"git log\" to investigate the repo")
        except:
            print("Error while dumping git repo")
    else:
        if verbosity:
            print("Git repo not found")
    
    # manual checks !
    print("---------------")
    print("Analysis is over. Check above for the results")
    print("Don't forget to check for :")
    print("- Null byte (in GET params, POST params and cookies)")
    print("- Double encoding")
    print("- GBK")
    print("- LFI")
    print("- Directory traversal")
    print("- Path truncation")
    print("- SQL injections")
    print("- XSS of all types")
    print("- HTML comments / JS code")
    print("")
    
    
    # dirbusteeeer
    print("Now proceeding to dirbuster...")

    useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    extensions = (".php", ".txt", "", ".js")
    with open("res/dir-wordlist.txt", "r") as check_list:
        for line in check_list:
            for ext in extensions:
                site_to_test = url + line.replace('\n', "") + ext
                site_request = requests.get(site_to_test, headers=useragent)
                if site_request.status_code == requests.codes.ok:
                    print("Page found : "+site_to_test)