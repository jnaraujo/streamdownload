import requests

def downloadFile(url, local, progress=False, chunk=1024):
    try:
        with requests.request('get',url, stream=True) as r:
            tcd = 0
            with open(str(local), 'wb') as o:
                for c in r.iter_content(chunk_size=chunk):
                    if progress:
                        tcd += len(c)
                        print(round( ( int(tcd) / int(r.headers['Content-Length']) ) * 100, 2))
                    o.write(c)
    except Exception as e:
        return e