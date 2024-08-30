import os,sys
from pathlib import Path


class Custom_Exception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()


        self.error_file_name=exc_tb.tb_frame.f_code.co_filename
        self.error_line_num=exc_tb.tb_lineno

    def __str__(self):
        return "the file name is : [{0}] \n  line number is :[{1}] \n error message is :[{2}]".format(self.error_file_name,self.error_line_num,str(self.error_message))
    