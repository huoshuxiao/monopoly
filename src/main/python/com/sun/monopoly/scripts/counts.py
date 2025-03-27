import sys

from com.sun.monopoly.features import counts
from com.sun.monopoly.features.parallel import counts as p_counts

if __name__ == '__main__':
    if len(sys.argv) > 1:
        __years__ = sys.argv[1].split(',')
        p_counts.run_ssq_count(__years__)
    else:
        counts.run_ssq_count()