#!/usr/bin/env python
# Version = 3.5.2
# __auth__ = 'kevin'
import os
import time
import sendmail
import psutil
import collections
 
disk_used = collections.OrderedDict()
cur_time = time.time()
# current_day = cur_time - cur_time % 86400
root_dir = ["D:\\SYSLOG", "F:\\log"]
log_name = 'result.log'
 
 
def get_disk_info():
    """
    查看磁盘属性信息
    :return: 磁盘使用率和剩余空间
    """
    for id in psutil.disk_partitions():
        if 'cdrom' in id.opts or id.fstype == '':
            continue
        disk_name = id.device.split(':')
        s = disk_name[0]
        disk_info = psutil.disk_usage(id.device)
        disk_used[s + '盘使用率：'] = '{}%'.format(disk_info.percent)
        disk_used[s + '剩余空间：'] = '{}GB'.format(disk_info.free // 1024 // 1024 // 1024)
    return disk_used
 
 
if __name__ == '__main__':
    with open(log_name, 'w') as f:
        ret = get_disk_info()
        for k, v in ret.items():
            f.write('{}{}。\n'.format(k, v))
 
        for item in root_dir:
            print(item)
            all_size = 0
            for parent, dir_names, file_names in os.walk(item):  # 遍历文件夹
                for filename in file_names:
                    path = os.path.join(parent, filename)  # 获取文件路径
                    stat_info = os.stat(path)  # 读取文件属性
                    upload_time = time.ctime(stat_info.st_mtime)
 
                    if stat_info.st_mtime > cur_time - 86400:
                        all_size += stat_info.st_size
                        #if stat_info.st_size // 1024 <= 5:
                        #    f.write('\n{}\n\t大小：{}KB,  上传时间：{}。'.format(path, stat_info.st_size // 1024, upload_time))
 
            f.write('\n\n {}本日备份大小：{}GB.\n'.format(item, all_size // 1024 // 1024 // 1024))
    with open(log_name, 'rb') as logfile:
        sendmail.sendmail('Syslog服务器备份监控', str(logfile.read(), encoding='GBK'))	