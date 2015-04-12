# coding=utf-8
'''
Created on 2015年3月24日

@author: Administrator
'''
class notebook: 
    def get_name(self):
        return self.name
    def set_name(self, n):
        self.name = n
    def get_id(self):
        return self.id
    def set_id(self,i):
        self.id = i
    def set_count(self,c):
        self.count = c
    def get_count(self):
        return self.count
        
if __name__ == "__main__":
    print '__main__%s' % 'note'