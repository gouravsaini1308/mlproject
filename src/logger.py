'''
## Logging means:
“Recording important events, messages, errors, and program activity 
while a program is running.”

## It helps developers:
-track program execution
-debug errors
-monitor applications

## Without Logging
If a project crashes: Something went wrong
You may not know:
-where
-why
-when
'''


import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
