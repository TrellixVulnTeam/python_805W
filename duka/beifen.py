#!/usr/bin/env python
# -*- coding: cp936 -*-  
import os  
import time 
import sys
import re
import datetime
import math
import string
#print (time.strftime('%Y-%m-%d',time.localtime(time.time())))
str_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
#print(str_time[5:])
b=str_time[5:]
lujing_name="G:\\ceshi\\CardLog\\2018\\"
#print(lujing_name)
a1=lujing_name+b
#print (type(a1))
b1_txt=r".txt"
#print (type(b1_txt))
c1=a1+b1_txt

#print(c1)
c2= '"'+c1+'"'
#print(c2)
# ���б���д����Ҫ���ݵ��ļ����ͻ�Ŀ¼  
source=[c2]
#source=[r'"c:\users\wangxiaozhen\desktop\lala.txt"']  
print(source)


# ���ݵ������Ŀ¼��  
target_dir='D:\\'  

# ����Ϊrar�ļ����ļ�����: ������ʱ����.rar  
target = target_dir + "lalala" + '.rar'  

# ��winrar����������ѹ���ļ���ǰ����winrar��windowsXP��path��  
zip_command="rar a %s %s"%(target, ' '.join(source) )   

#����������ݳ���������  
if os.system(zip_command) == 0:  
    print ('Successful backup to', target  )
else:  
    print ('Backup FAILED!'  )