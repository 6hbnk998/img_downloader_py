import requests
from bs4 import BeautifulSoup
import img2pdf
import os


headers={
    "User-Agent": "your user agent"
}

img_list =[]
dirname = "img_downloader.py"
for i in range(1,7):
    url = f"https://cdn.instantflipbook.com/assets2/examples/lm/inc/pages/mobile/page{i}.jpg"
    req = requests.get(url=url, headers=headers)
    response = req.content

    with open(f"imgdownloader/chasiki{i}.jpg", "wb") as file:
        img_list.append(f"{i}.jpg")
        file.write(response)
        
        print(f"picture {i} has been downloaded")

        for fname in os.listdir(dirname):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            img_list.append(path)
    

        
with open("result.pdf", "wb") as f:
    f.write(b'img2pdf.convert(img_list)')



def write():
    img_list = [f"media/{i}.jpg" for i in range(1,13)]

    with open("result.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))
write()
   
