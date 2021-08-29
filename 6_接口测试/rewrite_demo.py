# -*- coding:utf-8 -*-


from mitmproxy import ctx,http
import json

class RewriteMitm:
    def __init__(self):
        self.num = 0

    def request(self,flow):
        #编写匹配的规则
        #flow  mitmproxy.http
        if 'quote.json' in flow.request.pretty_url and 'x=' in flow.request.pretty_url:
            ctx.log.info(f'{flow.request.text}')
            data = json.loads(flow.response.text)
            data['data']['items'] += data['data']['items']
            flow.reponse.text = json.dumps(data)






addons = [
RewriteMitm()
]


if __name__=='__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p','8080','-s',__file__])

