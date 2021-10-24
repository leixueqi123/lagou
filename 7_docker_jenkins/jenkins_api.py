# -*- coding:utf-8 -*-
import requests
# url ='http://leixueqi:123456@localhost:8080/job/first_job/build/'
# re = requests.post(url)
# print (re.text)





# url ='http://leixueqi:123456@localhost:8080/job/pipline_pressure/lastBuild/buildNumber'
# re = requests.get(url)
# print (re.text)


#url ='http://leixueqi:123456@localhost:8080/job/pipline_pressure/<buildNumber>/api/json'
# import json
# url ='http://leixueqi:123456@localhost:8080/job/pipline_pressure/12/api/json'
# re = requests.get(url)
# print (json.dumps(re.json(),indent=2))

#
# from jenkinsapi.jenkins import  Jenkins
# jk = Jenkins(url,username,password,useCrumb=True)
#这样就能进行api调用了



import configparser
import datetime
import logging
import os
import re

from jenkinsapi.jenkins import Jenkins

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def get_jk_config(chose):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getcwd(),'jenkins_server.ini'))
    username  = config.get(chose,'username')
    password  = config.get(chose,'password')
    host = config.get(chose, 'host')
    port = config.get(chose, 'port')
    url = "http://"+host+":"+port
    return url,username,password

class JenkinsInfo():
    def __init__(self,job_name,chose='jenkins'):
        self.job_name = job_name
        config = get_jk_config(chose)
        self.jk = Jenkins(*config,useCrumb=True)

    def __get_job_from_keys(self):
        choose_list = []
        print (self.jk.keys())
        for my_job_name in self.jk.keys():
            if self.job_name in my_job_name:
                choose_list.append(my_job_name)
        return choose_list

    def __job_build(self,my_job_name):
        if self.jk.has_job(my_job_name):
            my_job_name = self.jk.get_job(my_job_name)
            if not my_job_name.is_queued_or_running():
                try:
                    last_build = my_job_name.get_last_buildnumber()
                except:
                    last_build = 0
                print (last_build)
                build_num = last_build + 1
                try:
                    self.jk.build_job(my_job_name)
                except Exception as e:
                    log.error(str(e))

                while True:
                    if not my_job_name.is_queued_or_running():
                        count_build = my_job_name.get_build(build_num)
                        start_time = count_build.get_timestamp() + datetime.timedata(hours=8)
                        console_out = count_build.get_console()
                        status = count_build.get_status()
                        change = count_build.get_changeset_items()
                        log.info(" "+str(start_time)+"发起的"+my_job_name+"构建完成，构建的")
                        p2 = re.compile(r".*Error.*")
                        err_list = p2.findall(console_out)
                        log.info("打包日志为："+str(console_out))
                        if status == 'SUCCESS':
                            if len(change) > 0:
                                for data in change:
                                    for file_list in data['affectPaths']:
                                        log.info(f"发起的{my_job_name}变更的备注：{data['msg']}")
                                    log.info(f"发起的{my_job_name}变更的提交人：{data['author']['fullName']}")
                            else:
                                log.info(f"发起的{my_job_name}没有变更内容")
                        else:
                            if len(err_list)>0:
                                log.warning(f"构建的{my_job_name}包含了以下错误")
                                for err in err_list:
                                    log.error(err)
                        break
            else:
                log.warning(f"发布的{my_job_name} jenkins is running")
        else:
            log.warning(f"发布的{my_job_name} 没有该服务")


    def run(self):
        my_job_name = self.__get_job_from_keys()
        if len(my_job_name) == 1:
            self.__job_build(my_job_name[0])
        elif len(my_job_name) == 0:
            log.error("输入的job名不正确")


if __name__ == '__main__':
    jk = JenkinsInfo("pipline_pressure")
    jk.run()








