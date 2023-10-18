import requests
import os


# 224 ERROR

def chapter_int_str(chapt):
    chapter_string = '0001'
    if chapt < 10:
        chapter_string = '000' + str(chapt)
    elif chapt < 100:
        chapter_string = '00' + str(chapt)
    elif chapt < 328:
        chapter_string = '0' + str(chapt)

    return chapter_string


def max_page(chapter_str):
    op = True
    maxn = 1
    linknum = '00' + str(maxn)
    while op:
        if maxn > 10:
            linknum = '0' + str(maxn)
        if chapter < 165:
            url = f"https://temp.compsci88.com/manga/Vagabond/{chapter_str}-{linknum}.png"
        else:
            url = f"https://scans-hot.leanbox.us/manga/Vagabond/{chapter_str}-{linknum}.png"
        r = requests.get(url)
        content = str(r.content[150:164])
        if content == "b'Page Not Found'":
            op = False
        else:
            maxn = maxn + 1

    return maxn


def generate_images(chapter_str):
    if chapter < 165:
        url = f"https://temp.compsci88.com/manga/Vagabond/{chapter_str}-001.png"
        image_url = 47
        url_min = 43
        url_max = 46
    else:
        url = f"https://scans-hot.leanbox.us/manga/Vagabond/{chapter_str}-001.png"
        image_url = 49
        url_min = 45
        url_max = 48

    directory_path = f'Gallery/Chapter {url[url_min:url_max]}/'
    os.makedirs(directory_path, exist_ok=True)
    n = max_page(chapter_str)

    for i in range(1, n):
        if i < 10:
            ui = '0' + str(i)
            # = f"https://temp.compsci88.com/manga/Vagabond/{chapter_str}-0{ui}.png"
            url = url[:image_url] + f"0{ui}" + ".png"
            image_name = url[image_url:]
            r = requests.get(url)
            with open(directory_path + image_name, 'wb') as f:
                f.write(r.content)
        else:
            # url = f"https://temp.compsci88.com/manga/Vagabond/{chapter_str}-0{i}.png"
            url = url[:image_url] + f"0{i}" + ".png"
            image_name = url[image_url:]
            r = requests.get(url)
            with open(directory_path + image_name, 'wb') as f:
                f.write(r.content)


chapter = int(input("Enter Chapter From which to start: "))

while True:
    # chapter = int(input("Enter Chapter number you want to download: "))

    chapter_limit = False

    if chapter > 327 or chapter_limit < 0:
        chapter_limit = True

    chapter_str = chapter_int_str(chapter)

    if not chapter_limit:
        generate_images(chapter_str)
        print(f"Chapter {chapter} Downloaded")
    else:
        print("CHAPTER LIMIT!!!")
        break

    chapter += 1
