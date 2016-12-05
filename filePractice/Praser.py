#coding=utf-8
import os
import os.path
import ConfigParser
class student_info(object):
    def __init__(self,recordfile):
        self.logfile=recordfile
        self.cfg=ConfigParser.ConfigParser()
    def cfg_load(self):
        self.cfg.read(self.logfile)
        # 打印
    def cfg_dump(self):
        se_list=self.cfg.sections()
        print "----------"
        for se in se_list:
            print se
            print self.cfg.items(se)
        print "----------"
        # 删除一项
    def delete_item(self,section,key):
        self.cfg.remove_option(section,key)
        # 删除一组
    def delete_section(self,section):
        self.cfg.remove_section(section)
        # 增加一组
    def add_section(self,section):
        self.cfg.add_section(section)
        # 设置一项
    def set_item(self,section,key,value):
        self.cfg.set(section,key,value)
        # 保存
    def save(self):
        fp=open(self.logfile,'w')
        self.cfg.write(fp)
        fp.close()
if __name__ == '__main__':
    info = student_info('imooc.txt')
    info.cfg_load()
    info.cfg_dump()
    info.set_item('userinfo','pwd','123')
    info.cfg_dump()
    info.add_section('login')
    info.set_item('login','time','2015-1-1')
    info.cfg_dump()
    info.save()
