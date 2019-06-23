import requests
# inp = input("Enter what you want to search ").split()
url = "https://www.google.com/search?q=bittoo"
# inp = '+'.join(inp)
# url = url1 + inp + url2
print(url)
r = requests.get(url)
print(r)
