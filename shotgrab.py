from urllib import request
import requests
from bs4 import BeautifulSoup

def PathHandler(letters, img_code, end_code):
    path_array = []
    
    while(img_code <= end_code):
        path = f"https://prnt.sc/{letters}{img_code}"
        img_code += 1
        path_array.append(path)

    return path_array
    
def GetImgSrc(url):
    r = requests.get(url, headers={'User-Agent': 'Chrome'})
    f = r.text
    doc = BeautifulSoup(f, "html.parser")
    img = doc.find("img")
    src = img["src"]
    print(f"SRC CONVERTING : {src}")

    return src 

def WriteImage(src):
    if (src[:2] != "//"):
        full_code = src.rsplit('/', 1)[-1]

        try:
            with request.urlopen(src) as response:
                data = response.read()

            with open(f"output/{full_code}", 'wb') as f:
                f.write(data)

        except:
            print('BAD RESPONSE')
        
    else: 
        print("File deleted")


if __name__ == "__main__":

    code = input("Enter start code ex: aa1111 (2numbers4letters)")

    letters = code[:2]
    start = int(code[-4:])

    number = int(input("Enter the amount of images (Max 9999)"))
    end = start + number

    if(end > 9999):
        end = 9999

    path_array = PathHandler(letters, start, end)
    src_array = []
    
    counter = 1
    size = len(path_array)

    for i in range(len(path_array)):
        print(f"Sourcing image {counter}/{size}")
        src_array.append(GetImgSrc(path_array[i]))
        counter += 1

    counter = 1
    size = len(src_array)

    for i in range(len(src_array)):
        print(f"Writing image {counter}/{size}")
        WriteImage(src_array[i])
        counter += 1