import subprocess, sys
import datetime


def takeScreenshot(url):
    return_code = 0
    error_message = ''

    foldername = url

    currtime = datetime.datetime.now()

    if '//' in url:
        split = url.split('//')
        foldername = split[1]

    friendlyName = './' + str(foldername) + '/' + str(currtime) +'.png'
    
    command = ['./phantomjs', 'rasterize.js', url, friendlyName]
    
    try:
        error_message = subprocess.check_output(command)
        print(error_message)
    
    except Exception as e:
        return_code = -1

takeScreenshot(sys.argv[1])


