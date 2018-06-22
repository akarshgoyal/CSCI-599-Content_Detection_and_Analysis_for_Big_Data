video_urls = []
image_urls = []
exts = ['jpg','jpeg', 'png', 'gif']
with open('filtered.txt') as f:
    for url in f.readlines():
        url = url.rstrip('\n')
        if url[-3:] in exts or url[-4:] in exts:
            image_urls.append(url+'\n')    
        else:
            video_urls.append(url+'\n')      

with open('image_urls.txt', 'w') as f:
    f.writelines(image_urls)

with open('video_urls.txt', 'w') as f:
    f.writelines(video_urls)
