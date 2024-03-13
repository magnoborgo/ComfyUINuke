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

## Use

I'm providing 3 basic workflows templates as examples.
Workflows must have a "translation.py" to work inside nuke (check Workflows folder)


## Bug report and suggestions

Are welcome, I'm looking for improvement ideas and UI suggestions, new functionalities, etc.
Open to colaboration, submit your commits!

## To do

A proper workflow translator. 
Sequence handling

## EXR handling
Check this extension that allows to use exr
https://github.com/spacepxl/ComfyUI-HQ-Image-Save

## Coffee
<a href="https://www.paypal.com/paypalme/MBORGO">Love it? Buy me a coffee</a>
