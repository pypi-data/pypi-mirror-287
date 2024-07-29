# yaml 文件操作
import os
import yaml
import configparser
import json
from config import Config
import pandas as pd

config = Config()


# 定义一个文件操作类
class FileOperateUtils:
    def __init__(self, file_name):
        self.file_path = os.path.join(config.File_DIR, file_name)

    # yaml文件操作
    def read_yaml(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    def write_yaml(self, data):
        with open(self.file_path, 'a+', encoding='utf-8') as f:
            yaml.dump(data, f)

    # excel 文件操作
    def read_excel(self):
        # 创建工作簿对象
        workbook = pd.ExcelFile(self.file_path)
        # 读取第一个工作表
        data = pd.read_excel(workbook, sheet_name=0)

        return data

    def write_excel(self, data):
        pass

    # ini文件操作
    def read_ini(self):
        conf = configparser.ConfigParser()
        conf.read(self.file_path)
        data = {}
        for section in conf.sections():
            data[section] = {}
            for option in conf.options(section):
                data[section][option] = conf.get(section, option)

        return data

    def write_ini(self, data):
        config = configparser.ConfigParser()
        for section, section_data in data.items():
            config.add_section(section)
            for option, value in section_data.items():
                config.set(section, option, value)

        with open(self.file_path, 'w') as f:
            config.write(f)

    # json文件操作
    def read_json(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return data

    def write_json(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


# 示例用法
if __name__ == '__main__':
    # 读取yaml文件
    # file_path = 'test.yaml'
    # file_utils = FileOperateUtils(file_path)
    # data = file_utils.read_yaml()
    # print(data)

    # 写入yaml文件
    # data = {'name': 'John', 'age': 30}
    # data = {'num': [1, 2, 3, 4, 5, 6, 7]}
    # file_utils.write_yaml(data)

    # 读取ini文件
    file_path = 'test.ini'
    file_utils = FileOperateUtils(file_path)
    data = file_utils.read_ini()
    print(data)

    # 写入ini文件
    # data = {
    #     'section1': {'key1': 'value1', 'key2': 'value2'},
    #     'section2': {'key3': 'value3', 'key4': 'value4'}
    # }
    # file_utils.write_ini(data)

    # # 读取json文件
    # file_path = 'example.json'
    # file_utils = FileOperateUtils(file_path)
    # data = file_utils.read_json()
    # print(data)
    #
    # # 写入json文件
    # data = {'name': 'John', 'age': 30}
    # file_utils.write_json(data)

    # 读取excel文件
    # file_path = 'example.xlsx'
    # file_utils = FileOperateUtils(file_path)
    # data = file_utils.read_excel()
    # print(data["A"])
    # # 转成列表输出
    # lst = data.values.tolist()
    # print(lst)
