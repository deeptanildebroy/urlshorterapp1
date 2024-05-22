import hashlib

def generate_short_url(original_url, length=6):
    hash_object = hashlib.md5(original_url.encode())
    short_url = hash_object.hexdigest()[:length]
    return short_url