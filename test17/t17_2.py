def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 如果端口后面有值就取([1:]是字符串切分，从第1位开始到结尾，目的是去年第一个斜线)，否则返回'web'，
    body = '<h1>sss , %s' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
