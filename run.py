#!/usr/bin/python

from ResourceServer import ResourceServer 

# route might be like one of (or something else):
#   /resource/config/com.liquidpixels.station.Workspace.Organize.jsr
#   /resource/js/config/com.liquidpixels.station.Workspace.Organize

res_path = 'test_config/com.sleepyjay.Workspace.Main.jsr' # jsr defaults to js
rs = ResourceServer(res_path)

print rs.resource

rs.start()




