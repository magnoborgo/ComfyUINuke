import random
import nuke
import os
def map(prompt,thenode):
    # use the "class_type": "KSampler" number
    prompt['3']["inputs"]["seed"]=thenode["smp_seed"].getValue() if thenode["smp_seed"].getValue() > 0 else random.randrange(0, 100000000)
    prompt['3']["inputs"]["steps"]=thenode["smp_steps"].getValue()
    prompt['3']["inputs"]["cfg"]=thenode["smp_cfg"].getValue()
    prompt['3']["inputs"]["denoise"]= thenode["smp_denoise"].getValue()
    #  "class_type": "CLIPTextEncoder"
    prompt['6']["inputs"]["text"]= thenode["prompt_p"].getText()
    prompt['7']["inputs"]["text"]= thenode["prompt_n"].getText()
    # image input nodes
    # "class_type": "LoadImageMask",

    write1 = nuke.toNode(thenode.name()+".Write_source")   
    nuke.execute(write1,nuke.frame(),nuke.frame()) # render the frame 
    prompt['22']["inputs"]["image"]= os.path.basename(write1["file"].getValue())
    # class_type": "LoadImage"
    write2 = nuke.toNode(thenode.name()+".Write_source1") 
    nuke.execute(write2,nuke.frame(),nuke.frame()) # render the frame 
    prompt['23']["inputs"]["image"]= os.path.basename(write2["file"].getValue())


    return prompt
