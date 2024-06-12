#Cron use: Pan India Billing Process
#File Description: Running City based multi-threading (each thread will get N no of data chunks to process)
#Main Function: start_proccess
#Database: None
#Database-Tables: None

import sys
import os
import time
import json
from concurrent.futures import ThreadPoolExecutor,wait,as_completed
import logging
import datetime
from pathlib import Path


def log(msg):
    path     = '/'
    filename = 'log_'
    dateTime = datetime.datetime.now()
    logpath = "logs/"+str(dateTime.year)+"/"+str(dateTime.month)+"/"
    if not os.path.exists(logpath):os.makedirs(logpath)
    fileObj = open(str(logpath)+filename+str(dateTime.strftime("%d")) + ".log", "a")
    logging.basicConfig(filename= fileObj.name, encoding='utf-8', level=logging.INFO)
    logging.info(f"[{dateTime.strftime('%Y-%m-%d %H:%M:%S')}][{msg}]")
    
def errorHandling(err):
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    errormsg = (f"Error:{err} File:{filename}, LineNo:{line_number}")
    log(errormsg)
    print(json.dumps({'errorcode':1,'status':'fail','message':errormsg}))

def start_proccess(data):
    try:
        start = time.perf_counter()
        time.sleep(3)
        end = time.perf_counter()
        # return {'errorcode':0, 'status':'success', 'execution-time':{end - start}}
    except Exception as err:
        errorHandling(err)
        
def create_thread():
    try:
        # log(params['id'])  
        cities = ['mumbai','delhi','pune']
        for city in cities:
            result=["Ford", "Volvo", "BMW", "Tata", "Mahindra"]
            divide = 2
            finalData = [result[i:i + divide] for i in range(0, len(result), divide)]
            
            # print(finalData)
            log(f"#----------------START------------------#")
            log(f"City: {city}, Threads Count:-{len(finalData)}")
            #Create Thread Pool with chunk data
            with ThreadPoolExecutor(max_workers=len(finalData)) as executor:
                threads = [executor.submit(start_proccess, finalData[chunkData]) for chunkData in range(len(finalData))]
                wait(threads)
                i = 0
                for thread in as_completed(threads):
                    # retrieve the result            
                    result = thread.result()
                    i += 1

                    log(f"Thread ({city})-{i}, result-{result}")
                log(f"#----------------END------------------#")
        print(json.dumps({'errorcode':0,'status':'success', 'message':'All cities thread are completed successfully.'}))
    except Exception as err:
            errorHandling(err)

####----start on PHP execution----####
create_thread()

            

