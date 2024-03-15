import random
import nuke
import os
import logging

log = logging.getLogger(__name__)
log.info("Loading %s " % os.path.abspath(__file__))

def map(prompt,thenode):
    text_prompts= {}
    for _ in prompt:
        if prompt[_]["class_type"] == "KSampler":
            prompt[_]["inputs"]["seed"]=thenode["smp_seed"].getValue() if thenode["smp_seed"].getValue() > 0 else random.randrange(0, 100000000)
            prompt[_]["inputs"]["steps"]=thenode["smp_steps"].getValue()
            prompt[_]["inputs"]["cfg"]=thenode["smp_cfg"].getValue()
            prompt[_]["inputs"]["denoise"]= thenode["smp_denoise"].getValue()


        if prompt[_]["class_type"] == "CLIPTextEncode":
            # text prompt handled later
            text_prompts[_] = (prompt[_])
            
        if prompt[_]["class_type"] == "LoadImage":
            write1 = nuke.toNode(thenode.name()+".Write_source")    
            nuke.execute(write1,nuke.frame(),nuke.frame())
            prompt[_]["inputs"]["image"]= os.path.basename(write1["file"].getValue())

        if prompt[_]["class_type"] == "LoadImageMask":
            write2 = nuke.toNode(thenode.name()+".Write_source1") 
            nuke.execute(write2,nuke.frame(),nuke.frame()) # render the frame 
            prompt[_]["inputs"]["image"]= os.path.basename(write2["file"].getValue())
          

    textprompt_indexes = sorted(text_prompts.keys())

    for n, _ in enumerate(sorted(text_prompts.keys())):
        # check for "positive" in the name, otherwise assumes the lower index is the positive prompt
        if "positive" in text_prompts[_]["_meta"]["title"]:
            prompt[_]["inputs"]["text"]= thenode["prompt_p"].getText()
        elif "negative" in text_prompts[_]["_meta"]["title"]: 
            prompt[_]["inputs"]["text"]= thenode["prompt_n"].getText()
        else:
            if n == 0:
                prompt[_]["inputs"]["text"]= thenode["prompt_p"].getText()
            if n == 1:   
                prompt[_]["inputs"]["text"]= thenode["prompt_n"].getText()





    # write1 = nuke.toNode(thenode.name()+".Write_source")    
    # nuke.execute(write1,nuke.frame(),nuke.frame())
    # prompt['22']["inputs"]["image"]= os.path.basename(write1["file"].getValue())
    # # print(prompt['22']["inputs"]["image"])
    # # prompt['5']["inputs"]["height"] = thenode["smp_height"].getValue()
    # # prompt['5']["inputs"]["width"]= thenode["smp_width"].getValue()




    return prompt
