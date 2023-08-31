import time

class TimeLogger:
    def __init__(self):
        self.__time_logs = {}
        
    def get_time_logs(self):
        return self.__time_logs
    
    def add_time_log(self, name, time):
        self.__time_logs[name] = time
    
    def log_build_time(self, log_name, func, args=[], kwargs={}):
        time_taken = None
        
        start_time = time.time()
        response = func(*args, **kwargs) if args else func()
        end_time = time.time()
        
        time_taken = end_time - start_time
        self.__time_logs[log_name] = time_taken
        
        return response
