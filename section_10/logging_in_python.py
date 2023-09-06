import logging;
#An argument for .basicConfig that displays date-time-seconds of when a log is created 
#format='%(asctime)s %(levelname)-8s:%(message)s' -8s indents each piece of data in a line
#You can add a parameter to basicConfig called datafmt='' and add arguments like '%d-%m-%Y %H:%M:%S'
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s:%(message)s', 
    level=logging.DEBUG,
    filename='logs.txt'
);

logger = logging.getLogger('test_logger');

logger.info('This will not show up');
logging.warning('This will....');
logger.debug("Debug message");
logger.critical("You did not find the bug fast enough and someone penetrated our system.")

'''
Levels of logging
-Debug,
-Info,
-Warning,
-Error,
-Critical
'''