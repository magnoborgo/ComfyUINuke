import nuke
import logging
import os
import sys
import json
import random
import time
import glob


if sys.version_info[0] < 3:
    import urllib2 as request
else:
    from urllib import request
    import importlib


__version__ = "0.0.2"
__author__ = "Magno Borgo"
__creation__ = "Mar 12 2024"
__date__ = "Mar 13 2024"
__web__ = "www.boundaryvfx.com"


log = logging.getLogger(__name__)
log.info("Loading %s " % os.path.abspath(__file__))

def signature(thenode):
    name = "ComfyUI_Nuke" 
    header = '''<span style="color:#aaa;font-family:sans-serif;font-size:8pt">'''
    extratext = '''<br>by <a href="https://github.com/magnoborgo/" style="color:#aaa">Magno Borgo</a>\nBoundary Visual Effects</span>'''
    version = "<br>v " + str(__version__) + " created " + __creation__ + ", updated " + __date__ 
    try:
        thenode["bvfxsignature"].setValue(name+header+version+extratext)
    except Exception:
        pass

def check_comfyuidir(dir):
    if os.path.exists(dir):
        if os.path.exists(dir+"main.py"):
            return True
        else:
            nuke.message("Found a directory but its not the correct one.\nPlease configure the directory location of comfyUI on the settings")
    else:
        nuke.message("Please configure the directory location of comfyUI on the settings")
    
    return False


def get_workflows(wflow_knob):
    wfdir = os.path.dirname(__file__)+'/Workflows/'
    files = glob.glob(wfdir+"*.json")
    #print(wflow_knob)
    wlist = []
    for _ in files:
        wlist.append(os.path.splitext(os.path.basename(_))[0])

    wlist = sorted(wlist,reverse=True)
    wflow_knob.setValues(wlist)
    wflow_knob.setValue("basic_workflow")
    

    #<-------- setup write node -------->



def main(thenode):

    SERVER = thenode["server_address"].getText()
    comfyUI_DIR = thenode["comfy_directory"].getText()

    if not check_comfyuidir(comfyUI_DIR):
        return

    thenode["status"].setValue(" ")
    wflow_knob=thenode["workflow_list"].value()



    #<------dynamic workflow importer ------->
    f = open(os.path.dirname(__file__)+'/Workflows/'+wflow_knob+'.json', "r")
    prompt = json.loads(f.read())
    f.close()
    translator = __import__(wflow_knob)

    if sys.version_info[0] < 3:
        reload(translator)
    else:
        importlib.reload(translator)

    #<------dynamic workflow importer end ------->
    
    prompt = translator.map(prompt,thenode)
    print(prompt)    
    
    reply = queue_prompt(prompt,SERVER)
    outputs=""
    if reply[0]: # valid reply
        # ---------------------------------------------------------- #
        task = nuke.ProgressTask('Waiting comfyUI')
        task.setProgress(0)
        tcount=0.0
        # ---------------------------------------------------------- #
        promptid = json.loads(reply[1].read())
        thenode["status"].setValue(reply[1].msg+" waiting for "+promptid["prompt_id"])# str(reply[1].read())
        success = False
        while True:
            if task.isCancelled():
                    break
            tcount+=1
            task.setProgress(int(tcount))
            req=request.urlopen(request.Request(SERVER+"/history"),timeout=10)
            req=json.loads(req.read())
            #print(req)
            if promptid["prompt_id"] in req.keys():

                # 'outputs': {'9': {'images': [{'filename': 'ComfyUI_00048_.png', 'subfolder': '', 'type': 'output'}]}},
                outputs = req[promptid["prompt_id"]]['outputs']["9"]["images"][0]["filename"]
                success = req[promptid["prompt_id"]]['status']["status_str"]

                result=thenode["status"].setValue(time.strftime('%H:%M:%S')+" "+success.upper()+" " +outputs+ " ready")  
                
                break
            if tcount >98:
                tcount=98 # keep it locked until server reply
            time.sleep(1)

        del(task)
        if success:
            read = nuke.toNode(thenode.name()+".Read_result")
            read["file"].setValue(comfyUI_DIR+"/output/"+outputs)
            read['reload'].execute()

    else:
        #print(type(reply[1]))
        text =  "<font color='red'>"+time.strftime('%H:%M:%S') + " Error: "+ str(reply[1]).replace("<","").replace(">","")+ "</font>"
        thenode["status"].setValue(text)



def is_prompt_ready(server="http://127.0.0.1:8188"):
    req = request.Request(server+"/history")
    #print(req.read())


def queue_prompt(prompt,server="http://127.0.0.1:8188"):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    try:
        req =  request.Request(server+"/prompt", data=data)
        response = request.urlopen(req,timeout=10)
        response = (True,response)
    except:
        e = sys.exc_info()
        #print(e[0],e[1],e[2])
        response = (False,e[1])

    return response

    #response.read() example from comfyUI {"prompt_id": "e097666e-2534-4668-ac21-ea634b12cdab", "number": 10, "node_errors": {}}'

if __name__ == '__main__':
    main(nuke.selectedNode())