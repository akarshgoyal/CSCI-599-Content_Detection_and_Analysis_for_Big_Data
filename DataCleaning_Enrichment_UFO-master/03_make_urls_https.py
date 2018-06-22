# http -> https
urls = []
with open('imageurls.txt') as f:
    for url in f.readlines():
        urls.append('https' + url[4:])

with open('https_urls.txt', 'w') as f:
    f.writelines(urls)
