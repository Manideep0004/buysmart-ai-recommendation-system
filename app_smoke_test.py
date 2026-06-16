import urllib.request
import urllib.error
import urllib.parse
import json
import time

BASE = 'http://127.0.0.1:8000'

def get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode('utf-8')
            print('URL:', url)
            print('STATUS:', resp.status)
            print(body[:500])
            return resp.status, body
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        print('URL:', url)
        print('HTTP ERROR', e.code)
        print(body)
        return e.code, body
    except Exception as exc:
        print('URL:', url)
        print('ERROR:', repr(exc))
        return None, None
    finally:
        print('---')


def post(url, data, headers=None):
    payload = json.dumps(data).encode('utf-8')
    req_headers = {'Content-Type': 'application/json'}
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, data=payload, headers=req_headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode('utf-8')
            print('URL:', url)
            print('STATUS:', resp.status)
            print(body[:500])
            return resp.status, body
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        print('URL:', url)
        print('HTTP ERROR', e.code)
        print(body)
        return e.code, body
    except Exception as exc:
        print('URL:', url)
        print('ERROR:', repr(exc))
        return None, None
    finally:
        print('---')


def run_smoke_tests():
    get(BASE + '/')
    get(BASE + '/products/10')
    get(BASE + '/products/recommend/10')
    get(BASE + '/products/by-id/0470536454')
    get(BASE + '/products/search/popular')
    get(BASE + '/products/search/robot')

    email = f'test_user_{int(time.time())}@example.com'
    status, body = post(BASE + '/auth/signup', {'email': email, 'password': 'pass1234'})
    if status != 200:
        return

    status, body = post(BASE + '/auth/login', {'email': email, 'password': 'pass1234'})
    if status != 200:
        return

    token_data = json.loads(body)
    auth_header = {'Authorization': f"Bearer {token_data['access_token']}"}

    get(BASE + '/products/by-id/0470536454', headers=auth_header)
    get(BASE + '/products/personalized', headers=auth_header)
    post(BASE + '/products/interact/0470536454', {'type': 'view'}, headers=auth_header)


if __name__ == '__main__':
    run_smoke_tests()
