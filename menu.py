import nuke
import bvfx_comfyuinuke
import logging
import os

log = logging.getLogger(__name__)
log.info("Loading %s " % os.path.abspath(__file__))

def bvfxsignature():
    thenode = nuke.thisNode()
    if "comfyUI_Nuke" in thenode.name():
        bvfx_comfyuinuke.signature(thenode)

nuke.addOnCreate(bvfxsignature, nodeClass="Group")