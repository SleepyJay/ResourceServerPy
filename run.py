#!/usr/bin/python

from ResourceServer import ResourceServer 
import pprint

pp = pprint.PrettyPrinter(indent=4)

# route might be like one of (or something else):
#   /resource/config/com.sleepyjay.station.Workspace.Organize.jsr
#   /resource/js/config/com.sleepyjay.station.Workspace.Organize

res_path = 'tests/rsconfigs/basic_config/com.sleepyjay.hamburger.jsr' # jsr defaults to js

rs = ResourceServer(res_path)
output = rs.start()

print "res_path: '{}'".format(rs.res_path)

print "\n----==Config==----"
pp.pprint(rs.config)

print "\n----==scanner.reources==----"
pp.pprint(rs.scanner.resources)

print "\n----==scanner.path_map==----"
pp.pprint(rs.scanner.path_map)

print "\n----==depEngine.dependencies==----"
pp.pprint(rs.depEngine.dependencies)

print "\n----==output==----"
print output

