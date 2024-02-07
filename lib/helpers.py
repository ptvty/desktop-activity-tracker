import argparse
import io
import sys

def console_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name', nargs='?', default='DEFAULT', help='A name for the project you\'re now working on')
    parser.add_argument('-stderr', dest = 'enable_stderr', action='store_true', default = False, help='Enable printing stderr output to console')
    args = parser.parse_args()
    return args

def null_stderr():
    class NullIO(io.StringIO):
        def write(self, txt):
            pass
    sys.stderr = NullIO()