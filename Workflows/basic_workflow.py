import random
import nuke
def map(prompt,thenode):
    # use the "class_type": "KSampler" number
    prompt['3']["inputs"]["seed"]=thenode["smp_seed"].getValue() if thenode["smp_seed"].getValue() > 0 else random.randrange(0, 100000000)
    prompt['3']["inputs"]["steps"]=thenode["smp_steps"].getValue()
    prompt['3']["inputs"]["cfg"]=thenode["smp_cfg"].getValue()
    prompt['3']["inputs"]["denoise"]= thenode["smp_denoise"].getValue()
    #  "class_type": "CLIPTextEncoder"
    prompt['6']["inputs"]["text"]= thenode["prompt_p"].getText()
    prompt['7']["inputs"]["text"]= thenode["prompt_n"].getText()
    # "class_type": "EmptyLatentImage", just a placeholder for the final img size
    prompt['5']["inputs"]["height"] = thenode["smp_height"].getValue()
    prompt['5']["inputs"]["width"]= thenode["smp_width"].getValue()
    
    return prompt
