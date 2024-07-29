# 日志操作
import logging
from datetime import datetime


class LoggerUtils(object):
    '''日志工具类'''
    current_date = datetime.now().strftime('%Y-%m-%d')
    def __init__(self, log_name=f'log'):
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(f'{self.current_date}_{log_name}.log', encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger


if __name__ == '__main__':
    # 使用示例
    logger = LoggerUtils('demo').get_logger()
    logger.error('这是一条error信息')
    logger.info('这是一条Info信息')
    logger.warning('这是一条warning信息')
    logger.debug('这是一条debug信息')
    logger.critical('这是一条critical信息')