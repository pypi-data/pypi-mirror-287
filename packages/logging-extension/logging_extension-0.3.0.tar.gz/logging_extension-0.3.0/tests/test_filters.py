import logging.config
import operator
from unittest import TestCase

from src.logging_extension.filters import BelowLevelFilter, LevelFilter


class TestLevelFilter(TestCase):
    def tearDown(self):
        logger = logging.getLogger()
        for ftr in logger.filters:
            logger.removeFilter(ftr)

    def test_filter(self):
        ftr = LevelFilter(level='INFO', compare='le')
        logging.getLogger().addFilter(ftr)

        with self.assertLogs():
            logging.getLogger().info('info message')
        with self.assertNoLogs():
            logging.getLogger().warning('error message')

    def test_filter_config(self):
        config = {
            'version': 1,
            'disable_existing_handlers': False,
            'filters': {
                'exclude_warnings': {
                    '()': LevelFilter,
                    'level': 'WARNING',
                    'compare': 'ne',
                },
            },
            'loggers': {
                'root': {
                    'level': 'DEBUG',
                    'filters': [
                        'exclude_warnings'
                    ]
                }
            }
        }

        logging.config.dictConfig(config)

        with self.assertLogs():
            logging.getLogger().info('info message')
            logging.getLogger().error('error message')
        with self.assertNoLogs():
            logging.getLogger().warning('error message')

    def test_set_level_int_valid(self):
        ftr = LevelFilter(level=0, compare='ge')
        ftr.set_level(logging.DEBUG)

        self.assertEqual(ftr.level, 10)

    def test_set_level_str_valid(self):
        ftr = LevelFilter(level=0, compare='ge')
        ftr.set_level('ERROR')
        self.assertEqual(ftr.level, 40)

    def test_set_level_invalid_raises(self):
        ftr = LevelFilter(level=0, compare='ge')
        with self.assertRaises(ValueError):
            ftr.set_level('INVALID_LEVEL')

    def test_set_compare_str(self):
        ftr = LevelFilter(level=0, compare='ge')
        ftr.set_compare('ne')
        self.assertEqual(ftr.compare, operator.ne)

    def test_set_compare_callable(self):
        ftr = LevelFilter(level=0, compare='ge')
        ftr.set_compare(max)
        self.assertEqual(ftr.compare, max)

    def test_set_compare_str_invalid_raises(self):
        ftr = LevelFilter(level=0, compare='ge')
        with self.assertRaises(ValueError):
            ftr.set_compare('not_valid')


class TestBelowLevelFilter(TestCase):
    def test_filter(self):
        level_filter = BelowLevelFilter(level=logging.ERROR)
        logging.getLogger().addFilter(level_filter)

        with self.assertLogs():
            logging.getLogger().warning('warning_msg')
        with self.assertNoLogs():
            logging.getLogger().error('error_msg')
