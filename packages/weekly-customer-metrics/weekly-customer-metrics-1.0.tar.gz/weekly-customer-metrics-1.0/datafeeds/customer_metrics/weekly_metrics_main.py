import logging
import traceback
import sys
sys.path.insert(0, r'C:\Users\nmdeshi\weekly_customer_metrics\datafeeds\customer_metrics')
from weekly_metrics_data import *

LOG = logging.getLogger(__name__)
PARAMS_LIST = ['config']


def get_command_line_arguments():
    """
    Method to read command line arguments passed to the main script
    Returns:
        args(dict): Dict of key value pairs passed as argument
    """
    LOG.info('>> get_command_line_arguments()')
    try:
        from awsglue.utils import getResolvedOptions
        args = getResolvedOptions(sys.argv, PARAMS_LIST)
    except ImportError:
        import argparse
        parser = argparse.ArgumentParser()
        for param in PARAMS_LIST:
            parser.add_argument('--{}'.format(param))
        args = vars(parser.parse_args())
    LOG.info('<< get_command_line_arguments()')
    return args


if __name__ == '__main__':
    try:
        import time
        start_time = time.time()
        weekly_metrics = WeeklyMetrics()
        message = weekly_metrics.run()
        end_time = time.time()
        execution_time = (end_time - start_time)
        print(f"Script executed in {execution_time} seconds.")

    except Exception as e:
        LOG.error('Error executing Customer Metrics \n {}'.format(
            traceback.format_exc()))
        raise e
