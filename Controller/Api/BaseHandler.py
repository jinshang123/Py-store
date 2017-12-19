# -*- coding: utf-8 -*-
"""
__author__ = 'sunny'
__mtime__ = '2017/2/14'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
                   ┏┓      ┏┓
                ┏┛┻━━━┛┻┓
               ┃      ☃      ┃
              ┃  ┳┛  ┗┳  ┃
             ┃      ┻      ┃
            ┗━┓      ┏━┛
               ┃      ┗━━━┓
              ┃              ┣┓
             ┃　            ┏┛
            ┗┓┓┏━┳┓┏┛
             ┃┫┫  ┃┫┫
            ┗┻┛  ┗┻┛
"""
import time
import json

import tornado
from tornado import web, gen, ioloop
from Controller.DbHandler import DB_Handler
from Common.MyExecption import ApiException
from Common.StaticFunc import ErrorCode, Set_return_dicts
import Common.config as config
from Common.Common import GetStoreId
# 这个并发库在python3自带在python2需要安装sudo pip install futures
from concurrent.futures import ThreadPoolExecutor


class Base_Handler(web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(Base_Handler, self).__init__(application, request, **kwargs)
        self.executor = ThreadPoolExecutor(10)
        self.__keyWord = None
        self.func = None
        self.dbhelp = DB_Handler()
        # 请求ip
        self.spbill_create_ip = self.request.remote_ip
        self.deviceName = self.request.headers.get("Devicename", "")
        self.connect = config.connect
        try:
            self.storeId = GetStoreId()
        except:
            self.storeId = None

    # 设置头部
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

    # 获取表单内容
    def get_all_argument(self):
        argument = self.request.arguments
        result = dict()
        for name, value in argument.items():
            if len(value) == 1:
                result[name] = value[0].decode()
            else:
                for data in value:
                    data = data.decode()
                result[name] = value

        return result

    @web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        try:
            # 异步
            yield tornado.gen.Task(ioloop.IOLoop.instance().add_timeout, time.time())
            if args != ():
                self.__keyWord = args[0]

            get_Data = self.get_all_argument()
            # print ('get:',get_Data)
            if len(args) > 1:
                get_Data['args'] = list(args)
                get_Data['args'].remove(self.__keyWord)

            checkSheBei = self.dbhelp.CheckSheBei(self.spbill_create_ip, self.deviceName)
            if checkSheBei == False:
                raise ApiException(ErrorCode.UserStateError)
            elif checkSheBei == 2:
                raise ApiException(ErrorCode.UserStateWaitError)

            if self.__keyWord:
                # result = self.func(self.__keyWord,get_Data)
                result = yield self.func(self.__keyWord, get_Data)
            else:
                result = yield self.func(get_Data)
                #  result = self.func(get_Data)

            TransmissionResult = json.dumps(result)
            # print ('get_send:{}'.format(TransmissionResult))

            self.write(TransmissionResult)
            self.finish()

        except ApiException as e:
            self.write(json.dumps(Set_return_dicts(forWorker=e.error_result['forWorker'],
                                                   code=e.error_result['errorCode'],
                                                   forUser=e.error_result['forUser'])))
            self.finish()

        except:
            self.write(json.dumps(Set_return_dicts(forWorker='不合法的参数',
                                                   code=ErrorCode.ParameterError,
                                                   forUser='请求超时')))

            self.finish()

    @web.asynchronous
    @gen.coroutine
    def post(self, *args, **kwargs):
        try:
            # 异步
            yield tornado.gen.Task(ioloop.IOLoop.instance().add_timeout, time.time())
            if args != ():
                self.__keyWord = args[0]

            # json传输
            try:
                get_Data = json.loads(self.request.body.decode())
            except:
                try:
                    get_Data = self.get_all_argument()
                except:
                    raise ApiException(ErrorCode.JsonError)
            # print ('post:',get_Data)

            checkSheBei = self.dbhelp.CheckSheBei(self.spbill_create_ip, self.deviceName)
            if checkSheBei == False:
                raise ApiException(ErrorCode.UserStateError)
            elif checkSheBei == 2:
                raise ApiException(ErrorCode.UserStateWaitError)

            if self.__keyWord:
                result = yield self.func(self.__keyWord, get_Data)
                # result = self.func(self.__keyWord,get_Data)
            else:
                result = yield self.func(get_Data)
                # result = self.func(get_Data)

            TransmissionResult = json.dumps(result)
            # print ('post_send{}'.format(TransmissionResult))
            self.write(TransmissionResult.encode('utf-8'))
            self.finish()

        except ApiException as e:
            self.write(json.dumps(Set_return_dicts(forWorker=e.error_result['forWorker'],
                                                   code=e.error_result['errorCode'],
                                                   forUser=e.error_result['forUser'])))

            self.finish()
