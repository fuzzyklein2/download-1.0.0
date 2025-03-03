from .startup import *
from .download import Download

if __name__ == '__main__':
    print(PROGRAM)
    log.info(f'Executing {PROGRAM} ...')
    
    p = Download().process_files()
    
    log.info(f'Execution complete.')
