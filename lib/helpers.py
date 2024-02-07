import argparse
import io
import sys

def console_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name', nargs='?', default='DEFAULT', help='A name for the project you\'re now working on')
    return args

