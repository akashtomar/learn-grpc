import os
import time


def create_file(file_name, content):
    '''
    simple function to create file 
    '''
    fn = os.path.join(os.path.dirname(__file__), 'output', file_name)
    content_lines = ''
    for i in range(100):
        content_lines += content + "\n"

    with open(fn, 'w') as f:
        f.write(content_lines)
        f.close()
    
    time.sleep(300)#to emulate an operation that takes 5 mins

    return "file created"
