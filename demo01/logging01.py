# _*_ coding = utf-8 _*_    设置文件中文编码
# @Time : 2022/10/26
# @Author King
# @File : logging01.py.py        当前文件名
# @Software  当前编译器

import logging
from logging import handlers


def create_log(name, level, filename, sh_level, fh_level):
    """
    :param name:  日志收集器名字
    :param level: 日志收集器的等级
    :param filename:  日志文件的名称
    :param sh_level:  控制台输出日志的等级
    :param fh_level:    文件输出日志的等级
    :return: 返回创建好的日志收集器
    """

    # 1、创建日志收集器
    log = logging.getLogger(name)

    # 2、创建日志收集器的等级
    log.setLevel(level=level)

    # 3、创建日志收集渠道和等级
    sh = logging.StreamHandler()
    sh.setLevel(level=sh_level)
    log.addHandler(sh)
    fh = logging.FileHandler(filename=filename, encoding="utf-8")
    # fh1 = handlers.TimedRotatingFileHandler(filename=filename,when="D",interval=1,backupCount=10,encoding="utf-8")
    fh.setLevel(level=fh_level)
    log.addHandler(fh)

    # 4、设置日志的输出格式
    formats = "%(asctime)s - [%(funcName)s-->line:%(lineno)d] - %(levelname)s:%(message)s"
    log_format = logging.Formatter(fmt=formats)
    sh.setFormatter(log_format)
    fh.setFormatter(log_format)
    return log


if __name__ == '__main__':
    log = create_log(name="rose_log", level=logging.DEBUG, filename="test_log.log", sh_level=logging.DEBUG,
                     fh_level=logging.DEBUG)
    log.info(msg="--------debug--------")
    log.info(msg="--------info--------")
    log.info(msg="--------warning--------")
    log.info(msg="--------error--------")
    log.info(msg="--------critical--------")
