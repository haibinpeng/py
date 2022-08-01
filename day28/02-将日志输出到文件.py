# 作者: Michael(phb)
# 2022年06月30日20时53分36秒
import logging

logging.basicConfig(level=logging.INFO,
                    filename='log.txt',
                    filemode='w',
                    encoding='utf8',
                    format = '%(asctime)s - %(process)d - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s')
logging.debug('这是 logging debug message')
logging.info('这是 logging info message')
logging.warning('这是 logging warning message')
logging.error('这是 logging error message')
logging.critical('这是 logging critical message')
