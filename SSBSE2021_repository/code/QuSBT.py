import sys

from search_method import Search

if __name__ == '__main__':
    dec2bin_param = int(sys.argv[1])
    group_name = sys.argv[2]
    program_name = sys.argv[3]
    algorithm = sys.argv[4]
    Search.search(dec2bin_param, group_name, program_name, algorithm)
