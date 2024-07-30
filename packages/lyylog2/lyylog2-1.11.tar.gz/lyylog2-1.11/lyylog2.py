import logging
import os
import sys
import inspect
from datetime import datetime
from colorama import init, Fore, Style

# 初始化 colorama
init(autoreset=True)

# 创建并配置日志记录器
lyy_logger = logging.getLogger("lyylog")

if not os.path.isdir(r"lyylog2"):
    os.mkdir(r"lyylog2")
# 自定义格式化函数
def format_log_message(level, msg):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    frame = inspect.currentframe().f_back.f_back
    filename = frame.f_code.co_filename
    line_number = frame.f_lineno
    log_msg = f"[{current_time}] [{level}] [{filename}:{line_number}] {msg}"
    return log_msg

def get_caller_module_name():
    frame = inspect.currentframe().f_back.f_back
    module = inspect.getmodule(frame)
    if module:
        module_filename = os.path.basename(module.__file__)
        module_name, _ = os.path.splitext(module_filename)
        return module_name
    else:
        print("Caller module name: unknown")
def write_log(text, directory=".",if_print=False):
    """
    简单写文件。

    Args:
    text (str): The text to append to the file.
    directory (str): The directory where the file will be saved. Default is the current directory.

    Returns:
    None
    """
    # Get the current date
    current = datetime.now()
    current_time = current.strftime("%Y-%m-%d %H:%M:%S")
    current_date = current.strftime("%Y-%m-%d")
    
    # Create the filename with the current date
    filename = f"lyylog2/write_log_{current_date}.txt"
    
    # Create the full file path
    file_path = os.path.join(directory, filename)
    
    text = "["+current_time + "] " + str(text)
    # Open the file in append mode and write the text
    with open(file_path, "a",encoding="utf-8") as file:
        file.write(text + "\n")
    if os.isatty(sys.stdout.fileno()) and if_print:
        print(f"日志已写入到 {file_path}, text = "+text)

def logg(msg,caller_module_name, level="info",  console=True, **kwargs):
    # 将所有参数拼接成一个字符串

    
    # 根据日志等级设置日志级别和文件名
    log_levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }
    
    level = level.lower()
    log_level = log_levels.get(level, logging.INFO)
    lyy_logger.setLevel(log_level)
    
    # 生成包含日期的日志文件名
    date_str = datetime.now().strftime("%Y%m%d")
    log_file = f"lyylog2/{caller_module_name}_lyylog2_{level}_{date_str}.log"
    
    # 创建文件处理器以写入日志文件
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(message)s")
    file_handler.setFormatter(formatter)
    lyy_logger.addHandler(file_handler)

    # 记录日志
    lyy_logger.log(log_level, msg)
    
    # 关闭文件处理器
    for handler in lyy_logger.handlers:
        handler.flush()
        handler.close()

    # 移除处理器以防止重复记录
    lyy_logger.handlers = []
    
    # 打印到终端，根据日志等级使用不同颜色
    if console:
        console_msg = msg
        color_map = {
            "debug": Fore.BLUE,
            "info": Fore.GREEN,
            "warning": Fore.YELLOW,
            "error": Fore.RED,
            "critical": Fore.MAGENTA
        }
        color = color_map.get(level, Fore.WHITE)
        print(f"{color}{console_msg}{Style.RESET_ALL}")

def log(*args, **kwargs):
    msg = ' '.join(map(str, args))
    if kwargs:
        msg += ' ' + ' '.join(f"{k}={v}" for k, v in kwargs.items())
    msg = format_log_message("info", msg)
    caller_module_name = get_caller_module_name()
    logg(msg, caller_module_name=caller_module_name, level="info", **kwargs)

def logerr(*args, **kwargs):
    msg = ' '.join(map(str, args))
    if kwargs:
        msg += ' ' + ' '.join(f"{k}={v}" for k, v in kwargs.items())
    msg = format_log_message("error", msg)
    caller_module_name = get_caller_module_name()
    logg(msg, caller_module_name=caller_module_name, level="error", **kwargs)

def logwarn(*args, **kwargs):
    msg = ' '.join(map(str, args))
    if kwargs:
        msg += ' ' + ' '.join(f"{k}={v}" for k, v in kwargs.items())
    msg = format_log_message("warn", msg)
    caller_module_name = get_caller_module_name()
    logg(msg, caller_module_name=caller_module_name, level="warn", **kwargs)

logerror = logerr
logdebug = log

if __name__ == "__main__":
    list1 = [1, 2, 3]
    log("这是一条info级别的日志信息。", "太好了", list1)
    logerr("这是一条error级别的日志信息。")
    write_log("这是写的日志")