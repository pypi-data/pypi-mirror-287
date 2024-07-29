# coding=utf-8
"""
众测API
"""
import requests
import hashlib
import json
import time


class CrowdtestApi(object):
    """
    众测API
    """

    def __init__(self, offline, template_id):
        """
            初始化MarketingApi类的实例，用于发送营销活动短信。
        
        Args:
            offline (bool): True表示是DEBUG模式，False表示是线上模式。默认为False。
            template_id (str): 短信模板ID，必须与对应产品线的模板ID一致。
        
        Returns:
            None.
        
        Raises:
            无异常抛出。
        """
        # DEBUG ENVIRONMENT
        self.offline = offline

        if self.offline:
            self.productline_name = 'AIR'
            self.secret = 'AIR'
            self.host = "https://zhongbao.baidu.com"
            self.request_prefix = '/mark/apiOut/'
            self.template_id = template_id

        else:
            # self.productline_name = 'ADU'
            # self.secret = 'ADU_2017'
            self.productline_name = 'AIR'
            self.secret = 'AIR'
            self.host = "https://zhongbao.baidu.com"
            self.request_prefix = '/mark/apiOut/'
            self.template_id = template_id

    def __sign(self, params):
        """
            为请求参数添加签名信息，包括时间戳、用户名和token。
        其中token是对用户名和时间戳进行MD5加密的结果。
        
        Args:
            params (dict): 请求参数字典，需要添加签名信息，必须包含以下键值对：
                - user_name (str): 产品线名称，默认为空字符串
                - timestamp (int, optional): 时间戳，默认为当前时间的整形毫秒数
                - token (str, optional): token信息，默认为空字符串
        
        Returns:
            dict: 返回添加了签名信息后的请求参数字典，包括以下键值对：
                - user_name (str): 产品线名称
                - timestamp (int): 时间戳
                - token (str): token信息，由用户名、时间戳和密钥（self.secret）进行MD5加密得到
        """
        params['timestamp'] = int(time.time())
        params['user_name'] = self.productline_name
        params['token'] = hashlib.md5(('user_name=' + params['user_name'] + '&timestamp=' +
                                      str(params['timestamp']) + '&' + self.secret).encode('utf-8')).hexdigest()

        return params

    def __get(self, request_resource, params=None):
        """
        get方式调用
        :param request_resource: 调用url
        :param params: 调用参数
        :return: json 格式返回
        """
        if not params:
            params = {}

        if self.offline:
            params["x_offline_debug"] = 1

        params = self.__sign(params)
        try:
            response = requests.get(self.host + self.request_prefix +
                                    request_resource, params=params)
            return response.text
        except Exception as e:
            error_msg = str(e)
            raise Exception(error_msg)

    def __post(self, request_resource, params=None):
        """
        post方式调用
        :param request_resource: 调用url
        :param params: 调用参数
        :return: json 格式返回
        """
        if not params:
            params = {}

        if self.offline:
            params["x_offline_debug"] = 1

        params = self.__sign(params)
        try:
            response = requests.post(self.host + self.request_prefix +
                                     request_resource, data=params)
            return response.text
        except Exception as e:
            error_msg = str(e)
            raise Exception(error_msg)

    def data_project_fill(self, url):
        """
        投放数据到标注项目
        :param file: 本地文件
        :return: 结果array
        """
        param = {
            'template_id': self.template_id,
            'url': str(url)
        }
        zhongce_result = self.__post('dataProjectFill', param)
        # print zhongce_result
        return json.loads(zhongce_result)

    def get_converted_file(self, data_id):
        """
        拉取数据投放结果
        :param data_id: 批次id
        :return: 结果array
        """
        param = {
            'id': data_id,
            'type': 'project_data'
        }
        zhongce_result = self.__get('getConvertedFile', param)
        # print zhongce_result
        return json.loads(zhongce_result)

    def get_reconciliation_list(self, template_id, status, date, page, limit):
        """
        获取对账列表
        :param template_id: 项目id
        :return: 结果array
        """
        param = {
            'template_id': template_id,
            'status': status,
            'date': date,
            'page': page,
            'limit': limit
        }
        zhongce_result = self.__get('getReconciliationList', param)
        return json.loads(zhongce_result)

    def get_reconciliation_detail(self, batch_id):
        """
        获取对账详情
        :param id: 批次id
        :return: 结果array
        """
        param = {
            'id': batch_id
        }
        zhongce_result = self.__get('getReconciliationDetail', param)
        return json.loads(zhongce_result)

    def confirm_converted_file(self, data_id, data_type, info):
        """
        确认对账结果
        :param data_id: 批次id
        :param data_type: 数据类型，目前使用project_data表示批次数据
        :param info: 纯字符串、json，{"is_reconciliation":1, "status":"success | fail"}
        :return: 结果array
        """
        param = {
            'id': data_id,
            'type': data_type,
            'info': info
        }

        zhongce_result = self.__post('confirmConvertedFile', param)
        return json.loads(zhongce_result)
