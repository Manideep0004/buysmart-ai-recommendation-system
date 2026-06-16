import urllib.request

urls = [
    'http://127.0.0.1:8000/',
    'http://127.0.0.1:8000/products/recommend/1'
]

for url in urls:
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            print('URL:', url)
            print('STATUS:', resp.status)
            print(resp.read().decode('utf-8'))
    except Exception as exc:
        print('URL:', url)
        print('ERROR:', repr(exc))
