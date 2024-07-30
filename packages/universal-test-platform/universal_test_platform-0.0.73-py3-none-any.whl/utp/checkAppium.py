import os
import platform
import subprocess
from time import sleep
import click
from utp.checkport import isPortUsed
from utp.utils import OS, getSubprocessOutput, readCommand

def checkAppium():
    """check appium installed and is running"""
    
    if isPortUsed(4723): 
        click.secho("appium have running before", bg='black', fg='yellow')
        return None
    
    #check appium is installed
    if platform.system() == OS.WINDOWS.value:
        appiumStatus, appiumError = readCommand("where.exe appium")
    elif platform.system() == OS.LINUX.value:
        appiumStatus, appiumError = readCommand("which appium")
    else:
        appiumStatus, appiumError = readCommand("which appium | grep $(npm config get prefix)")
       
    if appiumError:
        if appiumError.count("Could not find") > 0:
            click.secho("Prepare facilitator", bg='black', fg='yellow')
            os.popen("npm install -g appium").read()
        else:
            click.secho(appiumError, bg='black', fg='yellow')
            exit(1)
    elif not (appiumStatus and appiumStatus.strip()):
        click.secho("Prepare facilitator", bg='black', fg='yellow')
        os.popen("npm install -g appium").read()
    
    process = subprocess.Popen(["appium" ,"driver", "list", "--installed"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    driverInstalled =  getSubprocessOutput(process)
    if driverInstalled.count("uiautomator2") <= 0:
        click.secho("installing uiautomator2", bg='black', fg='green')
        os.popen("appium driver install uiautomator2").read()
    
    process = subprocess.Popen(["appium" ,"plugin", "list", "--installed"],shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    appiumStatus= getSubprocessOutput(process)
    #check device farm is installed
    if appiumStatus.count("device-farm") <= 0:
        click.secho("Prepare local device-farm", bg='black', fg='yellow')
        subprocess.Popen(["appium", "plugin", "install", "--source", "npm", "appium-device-farm"], shell=True,).wait()
        # subprocess.Popen(["appium", "plugin", "install", "--source", "npm", "appium-dashboard"]).wait()
        # os.popen("appium plugin install --source=npm appium-dashboard").read()
        click.secho("Prepared", bg='black', fg='yellow')
    

    handler= subprocess.Popen(["appium", "server", "-ka", "800",  "--use-plugins", "device-farm", "-pa", "/wd/hub", "--plugin-device-farm-platform","android"], shell= platform.system() == OS.WINDOWS.value, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                            
    
    sleep(5)
    click.secho("http://127.0.0.1:4723/device-farm", bg='black', fg='green')
    
    return handler