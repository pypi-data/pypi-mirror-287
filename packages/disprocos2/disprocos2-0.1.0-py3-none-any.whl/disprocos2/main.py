import time
from .timer import create_timer, is_time_exceeded, uninstall_package

def main(pklfile):
    if is_time_exceeded():
        uninstall_package()
        return
    
    # 你的主逻辑
    time.sleep(5 * 60)
    result = 0.01
    
    create_timer()
    return result

