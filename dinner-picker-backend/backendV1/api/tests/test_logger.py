from django.test import TestCase
from api.third_party_libraries.logger.singleton_logger import Logger

class TestLogger(TestCase):

    def test_logger(self):
        log1 = Logger()
        log2 = Logger()
        log3 = Logger()
        log4 = Logger()
        log5 = Logger()
        log1.info("test1")
        log2.info("test2")
        log3.debug("test3")
        log4.warning("test4")
        log5.error("test5")
        log1.critical("test6")
        self.assertEquals(log1 == log2, True)
        self.assertEquals(log1 is log2, True)
        self.assertEquals(log1._singleton_logger_instance, log2._singleton_logger_instance)