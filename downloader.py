import urlgenerator
import repeatfileremover
import urllib.request
import os
from datetime import datetime
from datetime import timedelta

if not os.path.exists("./data/"):
    os.makedirs("./data/")
    
    
def download(configure):
    print ("downloader : start download task !")
    now = datetime.now()
    timelable = now.strftime('_%Y-%m-%d-%H-%M')
    for target in configure.namelist:
        if configure.switch[target] == 1 :
            print ("downloader : downloading",target)
            savedir = "./data/"+target+"/"
            if not os.path.exists(savedir):
                os.makedirs(savedir)
            [base_url, filenamelist, extension] = urlgenerator.geturl(configure,target)
            
            add = 0
            for filename in filenamelist:
                if (target == "JMA_Weather_Chart_1") or (target == "CWB_Skew"):
                    savepath = savedir+filename+timelable+extension
                else:
                    savepath = savedir+filename+extension
                if not os.path.exists(savepath):
                    try:
                        urllib.request.urlretrieve(base_url+filename+extension, savepath)
                    except:
                        pass
                    else:
                        add += 1
            print ("downloader : downloaded",add,"files")
            if (target == "JMA_Weather_Chart_1") or (target == "CWB_Skew"):
                repeatfileremover.removerepeatedfiles(savedir)
        else :
            print ("downloader :",target,"is cancelled")
    return