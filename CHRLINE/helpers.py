# -*- coding: utf-8 -*-
import json

class Helpers(object):

    def __init__(self):
        pass
    
    def squareMemberIdIsMe(self, squareMemberId):
        if self.can_use_square:
            if squareMemberId in self.squares.get(2, {}).keys():
                return True
            else:
                return False
        else:
            raise Exception('Not support Square')
    
    def sendLiff(self, to, messages, tryConsent=True):
        liff = self.issueLiffView(to)
        token = liff.get(3)
        if not token:
            error = liff.get('error', {})
            print(f"[sendLiff]{error}")
            if error.get('code') == 3 and tryConsent:
                self.tryConsentLiff(error['metadata'][3][1])
                return self.sendLiff(to, messages, tryConsent=False)
            return error
        liff_headers = {
            'Accept' : 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; G730-U00 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 Line/9.8.0',
            'Accept-Encoding': 'gzip, deflate',
            'content-Type': 'application/json',
            'X-Requested-With': 'jp.naver.line.android'
        }
        liff_headers["authorization"] = 'Bearer %s'%(token)
        if type(messages) == "list":
            messages = {"messages":messages}
        else:
            messages = {"messages":[messages]}
        resp = self.server.postContent("https://api.line.me/message/v3/share", headers=liff_headers, data=json.dumps(messages))
        return resp.text
    
    def tryConsentLiff(self, channelId):
        payload = {
            "on": [
                "P",
                "CM"
            ],
            "off": []
        }
        data = json.dumps(payload)
        hr = {
            'X-LINE-ChannelId': channelId,
            'X-LINE-Access': self.authToken,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.1; SAMSUNG Realise/DeachSword; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36',
            'Content-Type': 'application/json',
            'X-Line-Application': '',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'zh-TW,en-US;q=0.8'
        }
        r = self.server.postContent("https://access.line.me/dialog/api/permissions", data=data, headers=hr)