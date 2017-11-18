from pyexpat import ParserCreate
from xml.dom import minidom

xml = r'''
<head>
    <meta charset="utf-8" />
    <title>淘宝网 - 淘！我喜欢</title>
    <meta name="spm-id" content="a21bo" />
</head>
'''

# class MySaxHandler(object):
#     def start_element(self, name, attrs):
#         print('start element:%s,attr:%s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax:end element:%s' % name)
#
#     def char_data(self, content):
#         print('sax:content:%s' % content)
#
#
# handler = MySaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

dom = minidom.parse('test.xml')
rootElement = dom.documentElement
print('名称：%s,值：%s,类型：%s' % (rootElement.nodeName, rootElement.nodeValue, rootElement.nodeType))
print(rootElement.childNodes[0].nodeName)
list_ = rootElement.getElementsByTagName('list')
for li in list_:
    print('------')
    print(li.getAttribute('id'))
    for node in li.childNodes:
        if node.nodeType == 1:
            print(node.nodeName + ":" + node.childNodes[0].data)
