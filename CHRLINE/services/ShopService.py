# -*- coding: utf-8 -*-
import time
import json

class ShopService(object):

    def __init__(self):
        pass
        
    def getProduct(self, shopId, productId, language="zh-TW", country="TW"):
        _headers = {
            'X-Line-Access': self.authToken, 
            'x-lpqs': "/TSHOP4"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 10, 103, 101, 116, 80, 114, 111, 100, 117, 99, 116, 0, 0, 0, 0]
        sqrd += [11, 0, 2, 0, 0, 0, len(shopId)] # e.g. stickershop
        for value in shopId:
            sqrd.append(ord(value))
        sqrd += [11, 0, 3, 0, 0, 0, len(productId)]
        for value in productId:
            sqrd.append(ord(value))
        sqrd += [12, 0, 4]
        sqrd += [11, 0, 1, 0, 0, 0, len(language)]
        for value in language:
            sqrd.append(ord(value))
        sqrd += [11, 0, 2, 0, 0, 0, len(country)]
        for value in country:
            sqrd.append(ord(value))
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent("https://gf.line.naver.jp/enc", data=data, headers=self.server.Headers)
        data = self.decData(res.content)
        return self.tryReadData(data)['getProduct']

    def getProductsByAuthor(self, authorId, productType=1):
        _headers = {
            'X-Line-Access': self.authToken, 
            'x-lpqs': "/TSHOP4"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('getProductsByAuthor') + [0, 0, 0, 0]
        sqrd += [12, 0, 2]
        sqrd += [8, 0, 1] + self.getIntBytes(productType)
        sqrd += [11, 0, 2] + self.getStringBytes(authorId)
        sqrd += [8, 0, 3] + self.getIntBytes(0)
        sqrd += [8, 0, 4] + self.getIntBytes(100)
        sqrd += [2, 0, 6, int(True)]
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent("https://gf.line.naver.jp/enc", data=data, headers=self.server.Headers)
        data = self.decData(res.content)
        return self.tryReadData(data)['getProductsByAuthor']
    
    def getStudentInformation(self):
        _headers = {
            'X-Line-Access': self.authToken, 
            'x-lpqs': "/TSHOP4"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('getStudentInformation') + [0, 0, 0, 0]
        sqrd += [12, 0, 2]
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent("https://gf.line.naver.jp/enc", data=data, headers=self.server.Headers)
        data = self.decData(res.content)
        return self.tryReadData(data)['getStudentInformation']
    
    def canReceivePresent(self, shopId, productId, recipientMid):
        _headers = {
            'X-Line-Access': self.authToken, 
            'x-lpqs': "/TSHOP4"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('canReceivePresent') + [0, 0, 0, 0]
        sqrd += [11, 0, 2] + self.getStringBytes(shopId)
        sqrd += [11, 0, 3] + self.getStringBytes(productId)
        sqrd += [12, 0, 4]
        sqrd += [11, 0, 1] + self.getStringBytes('zh_TW') #language
        sqrd += [11, 0, 2] + self.getStringBytes('TW') #country
        sqrd += [0]
        sqrd += [11, 0, 5] + self.getStringBytes(recipientMid)
        sqrd += [0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent("https://gf.line.naver.jp/enc", data=data, headers=self.server.Headers)
        data = self.decData(res.content)
        return self.tryReadData(data)['canReceivePresent']
    
    def getOwnedProductSummaries(self, shopId, offset=0, limit=200, language='zh_TW', country='TW'):
        _headers = {
            'X-Line-Access': self.authToken, 
            'x-lpqs': "/TSHOP4"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('getOwnedProductSummaries') + [0, 0, 0, 0]
        sqrd += [11, 0, 2] + self.getStringBytes(shopId)
        sqrd += [8, 0, 3] + self.getIntBytes(offset)
        sqrd += [8, 0, 4] + self.getIntBytes(limit)
        sqrd += [12, 0, 5]
        sqrd += [11, 0, 1] + self.getStringBytes(language)
        sqrd += [11, 0, 2] + self.getStringBytes(country)
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent("https://gf.line.naver.jp/enc", data=data, headers=self.server.Headers)
        data = self.decData(res.content)
        return self.tryReadData(data)['getOwnedProductSummaries']