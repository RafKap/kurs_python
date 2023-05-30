import webbrowser
from urllib.error import URLError

def ensure_correct_start(url):
    return url.startswith("https://") or url.startswith("http://")

def ensure_correct_end(url):
    return url.endswith(".pl") or url.endswith(".com")


def get_url():
    #url = input("Podaj strone internetowa ")
    url = "google.com/"
    if ensure_correct_start(url) or ensure_correct_end(url):
        return url
    elif url.startswith("www."):
        return "http://" + url
    else:
        raise URLError("zly format")






def main():

    try:
        url = get_url()
        webbrowser.open(url)
    except URLError as err:
        print(err)




if __name__ == "__main__":
    main()