import requests
import math
from progress.bar import Bar

'''
    url -> file url to download
    savepath -> where you want to save the file
    progress -> want to see the download progress?
    chunk -> chunk
'''
def downloadFile(url, savepath, progress=False, chunk=1024):
    try:
        with requests.request('get',url, stream=True) as r:
            with Bar('Downloading', max=int(r.headers['Content-Length'])/chunk) as bar:
                with open(str(savepath), 'wb') as o:
                    for c in r.iter_content(chunk_size=chunk):
                        if progress:
                            bar.next()
                        o.write(c)
    except Exception as e:
        return e