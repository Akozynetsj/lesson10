import logging #standartna biblioteka dlyz lgyvannya perebigy prigram
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(massage)s')
logging.debug('debug')
logging.info('info')
logging.error('error')
logging.warning('warning')
logging.critical('critical')
