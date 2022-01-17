from urllib.request import urlretrieve as retrieve_url
from urllib.error import HTTPError



def download_image(url: str, file_path: str, file_name: str) -> None:
    """Saving image by its URL which are taken as arguments (url, file_path - where to save, file_name - naming saved image)."""
    full_path = file_path + file_name + '.jpg'
    retrieve_url(url, full_path)


def main():
    """Main function for operating with whole saving proccess and exceptions."""

    # Data input
    try:
        url = str(input('Enter image URL to download: '))
        file_name = str(input('Enter file name to save as: '))
        file_path = str(input('Enter file path: '))
    except TypeError:
        print("Wrong type were retrieved! Please try again.")
    else:
        print("Downloading image...")

    # Downloading image
    try:
        if file_name:
            download_image(url, file_path, file_name)
        else:
            download_image(url, file_path, 'Image')
    except HTTPError:
        print("Unexpected HTTP error! Please try another url.")
    else:
        print(f"Image saved as {file_path}/{file_name}")

if __name__=="__main__":
    main()