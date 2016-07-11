#coding=utf-8

"""
filename : JDAPI
author : Quincy
date written : 07/11/2016
date modify : 07/11/2016
program purpose : 根据京东云宙斯提供的API,调用不同的方法method,获取相应的数据
description : 创建JdAPI类, api_dict为方法对应的参数,主要的参数是access_token, app_key, app_secret
"""

import urllib
import chardet


class JdAPI:

    api_dict = {'360buy.warecats.get': '{"fields":""}', #获取商家已开通的标准商品类目
                'jingdong.pop.vender.cener.venderBrand.query': '{"name":""}', #查询商家已授权的品牌
                'jingdong.dsp.kc.usertag.get': '{}', #获取类目结构树
                'jingdong.dsp.kc.orderdetail.list': '', #
                }

    def __init__(self, access_token=None, app_key=None, app_secret=None):
        self.access_token = access_token
        self.app_key = app_key
        self.app_secret = app_secret
        self.server_url = 'https://api.jd.com/routerjson'
        self.version = 'v=2.0'

    def create_url(self, method, _360buy_param_json=None):

        """
        :param method : (方法名)
        :param _360buy_param_json: (方法对应的参数列表)
        :return: url网址链接
        """

        api_method = 'method=' + method
        api_app_key = 'app_key=' + self.app_key
        api_access_token = 'access_token=' + self.access_token
        api_360buy_param_json = '360buy_param_json=' + _360buy_param_json
        url = self.server_url + '?' + self.version + '&' + api_method + '&' + api_app_key + '&' + api_access_token + '&' + api_360buy_param_json
        return url

    @staticmethod
    def request_data(url):

        """
        :param url: 网址链接
        :return: json格式的text文本
        """

        data = (urllib.urlopen(url)).read()
        charset = chardet.detect(data)
        code = charset['encoding']
        json_text = str(data).decode(code, 'ignore').encode("utf-8")
        return json_text

    def call_api(self, method):

        """
        :param method: 方法名
        :return: json格式的text文本
        """

        _360buy_param_json = JdAPI.api_dict[method]
        url = self.create_url(method, _360buy_param_json)
        json_data = self.request_data(url)
        print '---------- the result data by using method: ' + method + ' ------------'
        print json_data
        print '-----------------------------------------------------------------------'
        return json_data




if __name__ == '__main__':

    access_token = 'c7070849-84fa-4b62-ad02-cbe4c1e29867'
    app_key = '79AF7352BBAD29F3DC9D2CEA57FC27E4'
    app_secret = '5a62810a103b48249806983674dc043d'
    my_jd_dpi = JdAPI(access_token, app_key, app_secret)
    for method in my_jd_dpi.api_dict:
        print method
        my_jd_dpi.call_api(method)
        print '\n'