import requests

""" r = requests.get("https://httpbin.org/get")
print(r.status_code)   # 200 = 成功，404 = 找不到
print(r.text[:100])    # 网页内容（前 100 字符）
print(r.json())        # 如果是 JSON，直接转成字典 """ 


""" # 查天气 API（模拟）
r = requests.get("https://httpbin.org/get", params={"city": "beijing"})
print(r.url)   # https://httpbin.org/get?city=beijing """


try:
    r = requests.get("https://http111.org/get", timeout=5)
    r.raise_for_status()       # 不是 200 就抛异常
    print(r.json())
except requests.ConnectionError:
    print("网络连不上")
except requests.Timeout:
    print("请求超时")
except requests.HTTPError:
    print(f"服务器返回 {r.status_code}")


""" 
r = requests.get("https://api.github.com/repos/torvalds/linux")
d = r.json()
print(f"Linux 仓库：{d['stargazers_count']} ⭐")
print(f"描述：{d['description']}") """

