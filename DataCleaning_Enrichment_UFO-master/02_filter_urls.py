# discard unsupported extensions
urls = []
exts = ['jpg','jpeg', 'png', 'mp4', 'gif']
with open('https_urls.txt') as f:
    for url in f.readlines():
        url = url.rstrip('\n')
        if url[-3:] in exts or url[-4:] in exts:
            urls.append(url+'\n')

with open('filtered.txt', 'w') as f:
    f.writelines(urls)
