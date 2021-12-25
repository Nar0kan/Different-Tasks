import urllib.request

def dl_img(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input('Enter image URL to download: ')
file_name = input('Enter file name to save as: ')

if file_name:
    dl_img(url, '', file_name)
else:
    dl_img(url, '', 'Image')
