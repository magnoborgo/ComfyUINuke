import random
import nuke
import os
def map(prompt,thenode):
    prompt['3']["inputs"]["seed"]=thenode["smp_seed"].getValue() if thenode["smp_seed"].getValue() > 0 else random.randrange(0, 100000000)
    prompt['3']["inputs"]["steps"]=thenode["smp_steps"].getValue()
    prompt['3']["inputs"]["cfg"]=thenode["smp_cfg"].getValue()
    prompt['3']["inputs"]["denoise"]= thenode["smp_denoise"].getValue()
    prompt['6']["inputs"]["text"]= thenode["prompt_p"].getText()
    prompt['7']["inputs"]["text"]= thenode["prompt_n"].getText()

    write = nuke.toNode(thenode.name()+".Write_source")  
    write["disable"].setValue(False)  
    nuke.execute(write,nuke.frame(),nuke.frame())
    write["disable"].setValue(True)
    prompt['9']["inputs"]["image"]= os.path.basename(write["file"].getValue())

    write = nuke.toNode(thenode.name()+".Write_source1")  
    write["disable"].setValue(False)  
    nuke.execute(write,nuke.frame(),nuke.frame())
    write["disable"].setValue(True)
    prompt['14']["inputs"]["image"]= os.path.basename(write["file"].getValue())


    return prompt
