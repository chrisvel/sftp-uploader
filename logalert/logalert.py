import tkinter
import logging
from tkinter import messagebox

#construct a tkinter class for alerts
rootalert = tkinter.Tk()
rootalert.withdraw()

class LogAlert(object):
    """ Uploads files from Locally to the Remote site """

    def __init__(self):
        # create logger
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(logging.INFO)

        # create console handler and set level to debug
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.INFO)
        self.formatter = str('%(asctime)s - %(levelname)s - %(message)s')

    def lognalertaction(self, text, status):
        """ logs all shit """
        # create formatter
        formatter = logging.Formatter(self.formatter, datefmt='%m/%d/%Y %H:%M:%S')

        # write log to file
        logging.basicConfig(format=self.formatter,
                            datefmt='%m/%d/%Y %H:%M:%S',
                            filename='logs/sendlog.txt',
                            level=logging.INFO)

        # add formatter to ch
        self.ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(self.ch)

        if status == 'info':
            self.logger.info(str(text))
        elif status == 'warn':
            self.logger.warn(str(text))
            messagebox.showwarning("Error", str(text))
            quit()
        elif status == 'error':
            self.logger.error(str(text))
        elif status == 'critical':
            self.logger.critical(str(text))
        elif status == 'debug':
            self.logger.debug(str(text))
        else:
            pass

