# comfyUINuke
![Static Badge](https://img.shields.io/badge/Nuke_v12-PASS-green) ![Static Badge](https://img.shields.io/badge/Nuke_v13-PASS-green) ![Static Badge](https://img.shields.io/badge/Nuke_v14-PASS-green) ![Static Badge](https://img.shields.io/badge/Nuke_v15-PASS-green) 
![Static Badge](https://img.shields.io/badge/OSX-green) ![Static Badge](https://img.shields.io/badge/WIN-green) ![Static Badge](https://img.shields.io/badge/Linux-green) 

use stable diffusion via comfyUI inside Nuke

You need to have a running comfyUI to use it.
Tutorials and proper documentation will follow.

## Install

Edit you init.py and add the folder to plugin path:

`nuke.pluginAddPath("/Users/youruser/.nuke/comfyUINuke")`

Press Tab and create comfyUI_Nuke toolset

Setup the settings tab with your server address and disk folder.
Default server: http://127.0.0.1:8188
Directory: /wherever/you/installed/ComfyUI/

Save the toolset with your defaults.


## Demo

<a href="http://www.youtube.com/watch?feature=player_embedded&v=p5Z8fSBkCoo" target="_blank"><img src="http://img.youtube.com/vi/p5Z8fSBkCoo/mqdefault.jpg"
alt="Click to Watch the video" width="240" height="135" border="10" /><br>View the demo on Youtube</a>


## Use

I'm providing 3 basic workflows templates as examples.
Workflows must have a "translation.py" to work inside nuke (check Workflows folder)

## Errors

Common error codes and causes:<br><br>
`[Errno 61] Connection Refused`<br>ComfyUI is not running or wrong network address<br>

`[Http Error 400 or 40X] Bad Request`<br> The workflow .json file has something incompatible on it.
Usually your system has a checkpoint that has another name, ".safetensors" instead of ".ckpt" for example.
ComfyUI terminal will tell you which parameter is wrong.
Drag the workflow from the "ComfyUINuke/Workflows" folder into ComfyUI, fix the issue and save the workflow file overwriting the problematic one.


## Bug report and suggestions

Are welcome, I'm looking for improvement ideas and UI suggestions, new functionalities, etc.
Open to colaboration, submit your commits! Submit issues here on Github.

## To do

A proper workflow translator. Proper documentation and tutorials
Sequence handling

## EXR handling
Check this extension that allows to use exr
https://github.com/spacepxl/ComfyUI-HQ-Image-Save

## Workflows
If you want to get some specific workflow translated inside Nuke, lets talk.

## Coffee
<a href="https://www.paypal.com/paypalme/MBORGO">Love it? Buy me a coffee</a>
