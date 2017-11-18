import base64

# print(base64.b64encode(b'abc'))
# print(base64.b64decode(b'YWJj'))
#
# print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # 普通编码，会出现+和/
# print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # url safe编码，把+和/变成了-_
# print(base64.urlsafe_b64decode(b'abcd--__'))
# print(base64.urlsafe_b64decode(b'abcd++//'))

print(base64.b64encode(b'abcd'))
print(base64.b64decode(b'YWJjZA=='))


def safe_base64_decode(c):
    clength = 0
    if isinstance(c, bytes):
        c = str(c, encoding='utf-8')
        clength = len(c) % 4
    return base64.b64decode(c + '=' * clength)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
