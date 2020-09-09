import requests

'''
    url -> file url to download
    step -> step
    savepath -> where you want to save the file
    progress -> want to see the download progress?
    chunk -> chunk
'''
def downloadFile(url, savepath,step=10, progress=False, chunk=1024):
    try:
        with requests.request('get',url, stream=True) as r:
            tcd = 0
            with open(str(savepath), 'wb') as o:
                for c in r.iter_content(chunk_size=chunk):
                    if progress:
                        tcd += len(c)
                        percent = round( ( int(tcd) / int(r.headers['Content-Length']) ) * 100,1)
                        if round(percent) % step == 0:
                            print(percent)
                    o.write(c)
    except Exception as e:
        return e