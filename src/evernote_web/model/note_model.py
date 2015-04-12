# coding=utf-8
'''
Created on 2015年3月24日

@author: Administrator
'''
class note: 
    def get_name(self):
        return self.name
    def set_name(self, n):
        self.name = n
    def get_id(self):
        return self.id
    def set_id(self,i):
        self.id = i
        
if __name__ == "__main__":
    print '__main__%s' % 'note'