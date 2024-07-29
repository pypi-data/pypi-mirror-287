import datetime
import json


import lief
import pefile
import lief.logging

# 将日志级别设置为 ERROR，避免异常抛出
lief.logging.set_level(lief.logging.LOGGING_LEVEL.ERROR)


class FileInfo:
    def __init__(self, filepath):
        self.filepath = filepath
        self.cert_num = self.get_cert_num()
        self.cert_info = self.get_certificate_info()

    def get_cert_num(self):
        try:
            pe = pefile.PE(self.filepath)
            size = pe.OPTIONAL_HEADER.DATA_DIRECTORY[4].Size
            if size // 1000 < 12:
                cert_num = 1
            else:
                cert_num = 2
            return cert_num
        except:
            return 0

    def get_certificate_info(self):
        try:
            binary = lief.parse(open(self.filepath, 'rb'))
            d = json.loads(lief.to_json(binary))
            issuer = d["signatures"][0]['signer_info'][0]["issuer"]
            lst = d["signatures"][0]['certificates']
            for item in lst:
                if item['issuer'] == issuer:
                    name = item['subject'].split("=")[-1]
                    valid = item['valid_to']
                    if name:
                        return name, datetime.datetime(*valid)
                    return None, f"WARNING: {self.filepath} 签名解析失败---请手动查看"
        except KeyError:
            return None, f"WARNING: {self.filepath} 签名检查失败---未签名"
        except TypeError:
            return None, f"WARNING: {self.filepath} 签名解析失败---请手动查看"
