# 作者: Michael(phb)
# 2022年06月30日20时56分49秒
import logging

# 创建一个logger
logger = logging.getLogger()

# log等级总开关
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
log_file = 'log.txt'
fh = logging.FileHandler(log_file, mode='a')
fh.setLevel(logging.DEBUG)

# 创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(process)d - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 将logger添加到handler中
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')
