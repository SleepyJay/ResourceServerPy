#!/usr/bin/python

from ResourceServer import ResourceServer 
import pprint

pp = pprint.PrettyPrinter(indent=4)

# route might be like one of (or something else):
#   /resource/config/com.liquidpixels.station.Workspace.Organize.jsr
#   /resource/js/config/com.liquidpixels.station.Workspace.Organize

res_path = 'tests/rsconfigs/basic_config/com.sleepyjay.Workspace.Main.jsr' # jsr defaults to js

rs = ResourceServer(res_path)
rs.start()

pp.pprint(rs.config)





