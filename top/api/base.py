# -*- coding: utf-8 -*-

try:
    import httplib
except ImportError:
    import http.client as httplib
import urllib.parse
import time
import hashlib
import json
import itertools
import mimetypes

'''
定义一些系统变量
'''

SYSTEM_GENERATE_VERSION = "taobao-sdk-python-20190726"

P_APPKEY = "app_key"
P_API = "method"
P_SESSION = "session"
P_ACCESS_TOKEN = "access_token"
P_VERSION = "v"
P_FORMAT = "format"
P_TIMESTAMP = "timestamp"
P_SIGN = "sign"
P_SIGN_METHOD = "sign_method"
P_PARTNER_ID = "partner_id"

P_CODE = 'code'
P_SUB_CODE = 'sub_code'
P_MSG = 'msg'
P_SUB_MSG = 'sub_msg'


N_REST = '/router/rest'


def sign(secret, parameters):
    # ===========================================================================
    # '''签名方法
    # @param secret: 签名需要的密钥
    # @param parameters: 支持字典和string两种
    # '''
    # ===========================================================================
    # 如果parameters 是字典类的话
    if hasattr(parameters, "items"):
        keys = list(parameters.keys())
        keys.sort()
        parameters = "%s%s%s" % (secret, ''.join('%s%s' % (key, parameters[key]) for key in keys), secret)
    sign_str = hashlib.md5(parameters.encode()).hexdigest().upper()
    return sign_str


def mix_str(pstr):
    return str(pstr).encode('utf-8')


class FileItem(object):
    def __init__(self, filename=None, content=None):
        self.filename = filename
        self.content = content


class MultiPartForm(object):
    """Accumulate the data to be used when posting a form."""

    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = "PYTHON_SDK_BOUNDARY"
        return
    
    def get_content_type(self):
        return 'multipart/form-data; boundary=%s' % self.boundary

    def add_field(self, name, value):
        """Add a simple field to the form data."""
        self.form_fields.append((name, str(value)))
        return

    def add_file(self, field_name, filename, file_handle, mime_type=None):
        """Add a file to be uploaded."""
        body = file_handle.read()
        if mime_type is None:
            mime_type = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
        self.files.append((mix_str(field_name), mix_str(filename), mix_str(mime_type), mix_str(body)))
        return
    
    def __str__(self):
        """Return a string representing the form data, including attached files."""
        # Build a list of lists, each containing "lines" of the
        # request.  Each part is separated by a boundary string.
        # Once the list is built, return a string where each
        # line is separated by '\r\n'.  
        parts = []
        part_boundary = '--' + self.boundary
        
        # Add the form fields
        parts.extend(
            [ part_boundary,
              'Content-Disposition: form-data; name="%s"' % name,
              'Content-Type: text/plain; charset=UTF-8',
              '',
              value,
            ]
            for name, value in self.form_fields
            )
        
        # Add the files to upload
        parts.extend(
            [ part_boundary,
              'Content-Disposition: file; name="%s"; filename="%s"' % \
                 (field_name, filename),
              'Content-Type: %s' % content_type,
              'Content-Transfer-Encoding: binary',
              '',
              body,
            ]
            for field_name, filename, content_type, body in self.files
            )
        
        # Flatten the list and add closing boundary marker,
        # then return CR+LF separated data
        flattened = list(itertools.chain(*parts))
        flattened.append('--' + self.boundary + '--')
        flattened.append('')
        return '\r\n'.join(flattened)


class TopException(Exception):
    # ===========================================================================
    # 业务异常类
    # ===========================================================================
    def __init__(self):
        self.errorcode = None
        self.message = None
        self.subcode = None
        self.submsg = None
        self.application_host = None
        self.service_host = None
    
    def __str__(self, *args, **kwargs):
        sb = "errorcode=" + mix_str(self.errorcode) +\
            " message=" + mix_str(self.message) +\
            " subcode=" + mix_str(self.subcode) +\
            " submsg=" + mix_str(self.submsg) +\
            " application_host=" + mix_str(self.application_host) +\
            " service_host=" + mix_str(self.service_host)
        return sb

  
class RequestException(Exception):
    # ===========================================================================
    # 请求连接异常类
    # ===========================================================================
    pass


class RestApi(object):
    # ===========================================================================
    # Rest api的基类
    # ===========================================================================
    
    def __init__(self, domain='gw.api.taobao.com', port=80, appkey='27722846',
                 secret='0bd75d91b3cd38bd1e3fe3b77112fc0e'):
        # =======================================================================
        # 初始化基类
        # Args @param domain: 请求的域名或者ip
        #      @param port: 请求的端口
        # =======================================================================
        self.__domain = domain
        self.__port = port
        self.__httpmethod = "POST"
        self.__app_key = appkey
        self.__secret = secret

    def get_request_header(self):
        return {
                 'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                 "Cache-Control": "no-cache",
                 "Connection": "Keep-Alive",
        }
        
    def set_app_info(self, appinfo):
        # =======================================================================
        # 设置请求的app信息
        # @param appinfo: import top
        #                 appinfo top.appinfo(appkey,secret)
        # =======================================================================
        self.__app_key = appinfo.appkey
        self.__secret = appinfo.secret
        
    def getapiname(self):
        return ""
    
    def getMultipartParas(self):
        return []

    def getTranslateParas(self):
        return {}
    
    def _check_requst(self):
        pass
    
    def getResponse(self, authrize=None, timeout=30):
        # =======================================================================
        # 获取response结果
        # =======================================================================
        if self.__port == 443:
            connection = httplib.HTTPSConnection(self.__domain, self.__port, None, None, False, timeout)
        else:
            connection = httplib.HTTPConnection(self.__domain, self.__port, timeout)
        sys_parameters = {
            P_FORMAT: 'json',
            P_APPKEY: self.__app_key,
            P_SIGN_METHOD: "md5",
            P_VERSION: '2.0',
            P_TIMESTAMP: str(int(time.time() * 1000)),
            P_PARTNER_ID: SYSTEM_GENERATE_VERSION,
            P_API: self.getapiname(),
        }
        if authrize is not None:
            sys_parameters[P_SESSION] = authrize
        application_parameter = self.get_application_parameters()
        sign_parameter = sys_parameters.copy()
        sign_parameter.update(application_parameter)
        sys_parameters[P_SIGN] = sign(self.__secret, sign_parameter)
        connection.connect()
        
        header = self.get_request_header()
        if self.getMultipartParas():
            form = MultiPartForm()
            for key, value in application_parameter.items():
                form.add_field(key, value)
            for key in self.getMultipartParas():
                fileitem = getattr(self,key)
                if fileitem and isinstance(fileitem, FileItem):
                    form.add_file(key, fileitem.filename, fileitem.content)
            body = str(form)
            header['Content-type'] = form.get_content_type()
        else:
            body = urllib.parse.urlencode(application_parameter)
            
        url = N_REST + "?" + urllib.parse.urlencode(sys_parameters)
        connection.request(self.__httpmethod, url, body=body, headers=header)
        response = connection.getresponse()
        if response.status is not 200:
            raise RequestException('invalid http status ' + str(response.status) + ',detail body:' + response.read())
        result = response.read()
        jsonobj = json.loads(result)
        if "error_response" in dict(jsonobj).keys():
            error = TopException()
            if P_CODE in dict(jsonobj["error_response"]).keys():
                error.errorcode = jsonobj["error_response"][P_CODE]
            if P_MSG in dict(jsonobj["error_response"]).keys():
                error.message = jsonobj["error_response"][P_MSG]
            if P_SUB_CODE in dict(jsonobj["error_response"]).keys():
                error.subcode = jsonobj["error_response"][P_SUB_CODE]
            if P_SUB_MSG in dict(jsonobj["error_response"]).keys():
                error.submsg = jsonobj["error_response"][P_SUB_MSG]
            error.application_host = response.getheader("Application-Host", "")
            error.service_host = response.getheader("Location-Host", "")
            raise error
        return jsonobj
    
    def get_application_parameters(self):
        application_parameter = {}
        for key, value in self.__dict__.items():
            if not key.startswith("__") and key not in self.getMultipartParas() \
                    and not key.startswith("_RestApi__") and value is not None:
                if key.startswith("_"):
                    application_parameter[key[1:]] = value
                else:
                    application_parameter[key] = value
        # 查询翻译字典来规避一些关键字属性
        translate_parameter = self.getTranslateParas()
        for key, value in application_parameter.items():
            if key in translate_parameter:
                application_parameter[translate_parameter[key]] = application_parameter[key]
                del application_parameter[key]
        return application_parameter
