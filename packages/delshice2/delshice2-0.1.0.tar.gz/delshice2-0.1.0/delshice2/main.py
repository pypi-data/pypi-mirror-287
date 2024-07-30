from .timer import create_timer, is_time_exceeded, uninstall_package

def main():
    if is_time_exceeded():
        uninstall_package()
        return None
    
    # 主逻辑
    result = 0.01
    
    create_timer()
    return result
