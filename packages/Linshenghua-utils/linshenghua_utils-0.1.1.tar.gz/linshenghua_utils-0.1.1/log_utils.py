# 日志操作
import logging


class LoggerUtils(object):
    def __init__(self, log_name='log'):
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(f'{log_name}.log')
        fh.setLevel(logging.ERROR)

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
    logger = LoggerUtils('order').get_logger()
    logger.error('这是一条信息')