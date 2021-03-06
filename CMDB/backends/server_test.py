#coding=utf-8
from xmlrpclib import ServerProxy, Fault
from urlparse import urlparse
import json

class Server(object):
    def __init__(self, connection_string, id, su_hostname):
        self.name = urlparse(connection_string).hostname
        self.connection = ServerProxy(connection_string)
        self.id = id
        self.su_hostname =su_hostname
        self.tmp_dic = {}
        self.stats_list = []

    def refresh(self):
        #key以group，name和管理地址的id做为key
        # print '=========================================================>>>>>>>>>'
        
        try:
            self.connection.supervisor.getAllProcessInfo()
        except Exception as e:
            print e
        else:
            for i in self.connection.supervisor.getAllProcessInfo():

                self.tmp_dic["%s:%s:%s" % (i['group'], i['name'],self.id)] = i 
                self.tmp_dic["%s:%s:%s" % (i['group'], i['name'],self.id)]['su_hostname'] = self.su_hostname
                self.tmp_dic["%s:%s:%s" % (i['group'], i['name'],self.id)]['id'] = self.id

                # print i

                # self.dic["fields"] = i
                # self.dic["fields"]['su_hostname'] = self.su_hostname


                # self.dic["status"] = i 
                # self.dic["status"]['su_hostname'] = self.su_hostname
                # self.dic['statename']=i['statename']
                # self.dic['description']=i['description']
                # self.dic['name']=i['name']
                # self.dic['logfile']=i['logfile']
                # print self.dic["%s:%s" % (i['group'], i['name'])]['description']
                # print self.dic.keys()
                # print self.dic.values()

            for k,v in self.tmp_dic.items():
                self.stats_list.append(v)
            # self.stats_list  = json.dumps(self.stats_list )
            # print self.stats_list 

    def stop(self, name):
        try:
            return self.connection.supervisor.stopProcess(name)
        except Fault, e:
            if e.faultString.startswith('NOT_RUNNING'):
                return False
            raise

    def start(self, name):
        try:
            return self.connection.supervisor.startProcess(name)
        except Fault, e:
            if e.faultString.startswith('ALREADY_STARTED'):
                return False
            raise

    def start_all(self):
        return self.connection.supervisor.startAllProcesses()

    def restart(self, name):
        self.stop(name)
        return self.start(name)

#======test========

# test = Server('http://user:123@192.168.11.11:9001',2,"test001")
# test.refresh()
# test.stop('beanstalk-11304')

# stat = test.dic
# # statues = stat.values()
# testkey = stat.keys()

# for i in testkey:
#     print stat[i]['description']



