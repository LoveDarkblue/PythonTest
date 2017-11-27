import chardet

print(chardet.detect(b'abc'))

print(chardet.detect('中国中国中国'.encode('gbk')))

print(chardet.detect('の主要ニュース'.encode('euc-jp')))
