# -*- coding: cp936 -*-  
import os  
import time  
# ���б���д����Ҫ���ݵ��ļ����ͻ�Ŀ¼  
source=[r'"G:\\ceshi\\CardLog\\2018\\03-26.txt"']  

# ���ݵ������Ŀ¼��  
target_dir='d:\\'  

# ����Ϊrar�ļ����ļ�����: ������ʱ����.rar  
target = target_dir + "lalala" + '.rar'  

# ��winrar����������ѹ���ļ���ǰ����winrar��windowsXP��path��  
zip_command="rar a %s %s"%(target, ' '.join(source) )   

#����������ݳ���������  
if os.system(zip_command) == 0:  
    print ('Successful backup to', target  )
else:  
    print ('Backup FAILED!'  )