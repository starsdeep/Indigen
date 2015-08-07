__author__ = 'fucus'
from indigen.settings import MEDIA_URL
def get_file_path_from_url(url):
    len_media_url = len(MEDIA_URL)
    if url[:len_media_url] == MEDIA_URL:
        url = url[len_media_url:]

    return url