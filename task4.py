import psutil
import memory
import network
from datetime import datetime
import configparser
import time
import re

while True:
    print("=========================================================================================================", '\n\n' )
    def cpu():
        cp = '{ \n "CPU load" : ' + '"' +str(psutil.cpu_percent()) + '"'
        return cp + '\n' + '}'
    print(cpu())




    print("=========================================================================================================", '\n\n' )

    def memov():
        ovmem = 'Overall usage memory = ' + '"' + str(memory.psutil.virtual_memory()) + ' MHz"'
        ovmem = re.sub(r'=', '" : "', ovmem)
        ovmem = re.sub(r',', ' MHz",' + '\n' + '"',ovmem)
        ovmem = ovmem.replace(r'" : "', '= { \n', 1)
        return ovmem + '\n' + '}'
    print(memov())




    print("=========================================================================================================", '\n\n' )

    def memsw():
        swmem = 'Overall usage virtual memory = ' + '"' + str(memory.psutil.swap_memory()) + ' MHz"'
        swmem = re.sub(r'=', '" : "', swmem)
        swmem = re.sub(r',', ' MHz",' + '\n' + '"', swmem)
        swmem = swmem.replace(r'" : "', '= { \n', 1)
        return swmem + '\n' + '}'
    print(memsw())




    print("=========================================================================================================", '\n\n' )

    def net():
        ip = 'Network information = ' + '"' + str(network.psutil.net_io_counters()) + '"'
        ip = re.sub(r'=', '" : "', ip)
        ip = re.sub(r',', '",' + '\n' + '"', ip)
        ip = ip.replace(r'" : "', '= { \n', 1)
        return ip + '\n' + '}'
    print(net())




    print("=========================================================================================================", '\n\n' )

    def disk():
        ip = 'Disc usage = ' + '"' + str(psutil.disk_io_counters()) + '"'
        ip = re.sub(r'=', '" : "', ip)
        ip = re.sub(r',', '",' + '\n' + '"', ip)
        ip = ip.replace(r'" : "', '= { \n', 1)
        return ip + '\n' + '}'
    print(disk())


    print("=========================================================================================================")


    Config = configparser.ConfigParser()
    Config.read("config")

    def ConfigSectionMap(section):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    config_name = ConfigSectionMap("common")['output']
    config_interval = ConfigSectionMap("common")['interval']

    f=open("monitoring."+config_name, "a")
    def stroki():
        total_line_count = sum(1 for line in open("monitoring." +config_name))
        a=(total_line_count/47+1)
        return a
    print(stroki())

    f.write("SNAPSHOT " + str(stroki()) + " " + str(datetime.now()) + '\n\n' + cpu() + '\n' + memov() + '\n' + memsw() +'\n' + net() + '\n'+ disk() + '\n' + "===============================================================================================================================================================================================================" + '\n')
    f.close()

    time.sleep(300)