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
    prompt['19']["inputs"]["height"] = thenode["smp_height"].getValue()
    prompt['19']["inputs"]["width"]= thenode["smp_width"].getValue()
    write1 = nuke.toNode(thenode.name()+".Write_source")    
    nuke.execute(write1,nuke.frame(),nuke.frame())
    prompt['11']["inputs"]["image"]= os.path.basename(write1["file"].getValue())
    

    return prompt
