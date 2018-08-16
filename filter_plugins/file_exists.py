from ansible import errors
import os.path

def file_exists(file):
    return os.path.isfile(file)

class FilterModule(object):
    '''Returns tru eif the file exists'''
    def filters(self):
        return {
            'file_exists' : file_exists
        }