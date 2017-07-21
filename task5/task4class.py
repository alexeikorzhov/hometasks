import psutil
import configparser
import re
import time
from datetime import datetime


while True:
    class Stat:
        a = r'='
        b = '" : "'
        c = "= { \n"

    class Info(Stat):
#        d = Template(r'=', '" : "')
        def cpu(self):
            cp = '{ \n "CPU load" : ' + '"' + str(psutil.cpu_percent()) + '"'
            return cp + '\n' + '}'

        def memov(self):
            ovmem = 'Overall usage memory = ' + '"' + str(psutil.virtual_memory()) + ' MHz"'
            ovmem = re.sub(super().a, super().b, ovmem)
            ovmem = re.sub(r',', ' MHz",' + '\n' + '"', ovmem)
            ovmem = ovmem.replace(r'" : "', super().c, 1)
            return ovmem + '\n' + '}'

        def memsw(self):
            swmem = 'Overall usage virtual memory = ' + '"' + str(psutil.swap_memory()) + ' MHz"'
            swmem = re.sub(super().a, super().b, swmem)
            swmem = re.sub(r',', ' MHz",' + '\n' + '"', swmem)
            swmem = swmem.replace(r'" : "', super().c, 1)
            return swmem + '\n' + '}'

        def net(self):
            ip = 'Network information = ' + '"' + str(psutil.net_io_counters()) + '"'
            ip = re.sub(super().a, super().b, ip)
            ip = re.sub(r',', '",' + '\n' + '"', ip)
            ip = ip.replace(r'" : "', super().c, 1)
            return ip + '\n' + '}'

        def disk(self):
            ip = 'Disc usage = ' + '"' + str(psutil.disk_io_counters()) + '"'
            ip = re.sub(super().a, super().b, ip)
            ip = re.sub(r',', '",' + '\n' + '"', ip)
            ip = ip.replace(r'" : "', super().c, 1)
            return ip + '\n' + '}'

    st = Info()
    st.cpu()
    st.memov()
    st.memsw()
    st.net()
    st.disk()


    Config = configparser.ConfigParser()
    Config.read("configur")


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

    class file():

        f = open("monitoring." + config_name, "a")


        def stroki():
            total_line_count = sum(1 for line in open("monitoring." + config_name))
            a = (total_line_count / 47 + 1)
            return a
        print(stroki())

        f.write("SNAPSHOT " + str(stroki()) + " " + str(
            datetime.now()) + '\n\n' + st.cpu() + '\n' + st.memov() + '\n' + st.memsw() + '\n' + st.net() + '\n' + st.disk() + '\n' + "===============================================================================================================================================================================================================" + '\n')
        f.close()

    time.sleep(30)