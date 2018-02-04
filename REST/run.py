# Stephen Giuliani
# Spring 2018 - i524
# Eve/REST

from eve import Eve
import psutil
import platform
from datetime import datetime
# from flask import jsonify
import json

message = "--Welcome--\n"\
    "Intended for localhost usage only. Default route = '/showme/[query]'\n"\
    "Available Queries:\n"\
    "    themoney\n    ram\n    uname\n    disk\n    user\n"\
    "Example:  curl -i http://localhost:5000/showme/ram\n"

print(message)
app = Eve()


# Uses json.dumps to convert the pulled data into output-form
def format(data):
    output = json.dumps(data, indent=4)+"\n"
    return output


# Returns everything outlined below
@app.route('/showme/themoney', methods=['GET'])
def themoney():
    ALL = {
        "_ALL DATA_": "_ALL INFO_",
        "RAM - Total": psutil.virtual_memory().total,
        "RAM - Available": psutil.virtual_memory().available,
        "RAM - Used": psutil.virtual_memory().used,
        "RAM - Percent Available": str(100 - psutil.virtual_memory().percent) + "%",
        "RAM - Free": psutil.virtual_memory().free,
        "uname - Node": platform.uname().node,
        "uname - System": platform.uname().system,
        "uname - Release": platform.uname().release,
        "uname - Version": platform.uname().version,
        "uname - Processor": platform.uname().processor,
        "Disk Usage - Total": psutil.disk_usage('/').total,
        "Disk Usage - Used": psutil.disk_usage('/').used,
        "Disk Usage - Free": psutil.disk_usage('/').free,
        "Disk Usage - Percent": str(psutil.disk_usage('/').percent) + "%",
        "CPU - Cores": psutil.cpu_count(),
        "CPU - Usage": str(psutil.cpu_percent()) + "%",
        "User Data - User": psutil.users()[0].name,
        "User Data - Terminal": psutil.users()[0].terminal,
        "User Data - Host": psutil.users()[0].host,
        "User Data - StartTime": datetime.fromtimestamp(psutil.users()[0].started).strftime("%m-%d-%Y %H:%M:%S")
        }
    return format(ALL)


# Returns system RAM
@app.route('/showme/ram', methods=['GET'])
def ram():
    ram = {
            "_RAM DATA_": "_Bytes_",
            "Total": psutil.virtual_memory().total,
            "Available": psutil.virtual_memory().available,
            "Used": psutil.virtual_memory().used,
            "Percent Available": str(100-psutil.virtual_memory().percent) + "%",
            "Free": psutil.virtual_memory().free
            }
    return format(ram)


# Returns the data you'd get from running 'uname' in a terminal
@app.route("/showme/uname", methods=['GET'])
def uname():
    unamedata = {
            "_UNAME_": "_Info_",
            "Node": platform.uname().node,
            "System": platform.uname().system,
            "Release": platform.uname().release,
            "Version": platform.uname().version,
            "Processor": platform.uname().processor,
            "Architecture": platform.uname().architecture()[0]
            }
    return format(unamedata)


# Returns the disk status in terms of bytes
@app.route("/showme/diskspace", methods=['GET'])
def disk():
    diskusage = {
            "_DISK USAGE_": "_Bytes_",
            "Total": psutil.disk_usage('/').total,
            "Used": psutil.disk_usage('/').used,
            "Free": psutil.disk_usage('/').free,
            "Percent": str(psutil.disk_usage('/').percent)+"%",
            "CPU Cores": psutil.cpu_count(),
            "CPU Usage": str(psutil.cpu_percent())+"%"
            }
    return format(diskusage)


# Returns the user's information
@app.route("/showme/user", methods=['GET'])
def user():
    userinfo = {
            "_USER INFO_": "_Info_",
            "User": psutil.users()[0].name,
            "Terminal": psutil.users()[0].terminal,
            "Host": psutil.users()[0].host,
            "StartTime": datetime.fromtimestamp(psutil.users()[0].started).strftime("%m-%d-%Y %H:%M:%S")
            }
    return format(userinfo)


if __name__ == '__main__':
    app.run()
    
