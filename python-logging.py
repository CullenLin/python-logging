import logging


def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)


def log_main():
    setup_logger('log1', '/tmp/log1.log')
    setup_logger('log2', '/tmp/log2.log')
    log1 = logging.getLogger('log1')
    log2 = logging.getLogger('log2')

    log1.info('Info for log 1!')
    log2.info('Info for log 2!')
    log1.error('Oh, no! Something went wrong!')


if __name__ == '__main__':
    log_main()