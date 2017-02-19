# ResourceServerPy - ToDo


### Version 0.1 (Public Git Minimum):

* Read config:
	* //@ classpath
 		* Use +> to separate full from relative path fragments
 		* Use => to provide a full alias to a classpath
	* //@ echo
* scan paths for source 
* Read souce:
	* //@ import
	* //@ require
	* //@ echo
	* //@ end
* build dependency map
* output: 
	* as source 
	* as list: `//@ emit list`
* add directory handler
* pass starting resource
* tests:
	* parse only given resource type
	* get correct dependency map


### Version 0.2:
* ??


### Backlog
* verbose and logging
* plugable lexer
* plugable emitter
* allow quotable classpaths
* directives:
 	* //@ set $value
	* //@ group use
	* //@ group use if
	* //@ group start
	* //@ group end
	* //@ group default
	* //@ alert on error ?
	* //@ load ?
	* //@ inquire ?
	* //@ allow ?
	* //@ rewrite
	* //@ classpath
	* //@ skippath
	* //@ define
	* //@ preloaded
	* //@ resource import
	* //@ resource require
	* //@ resource exclude
	* //@ resource load
	* //@ lint (warn | puke | strip | ignore) (commabrace | console)
	* //@ emitter gzip
	* //@ emitter headers
	* //@ emitter copyright
	* //@ emitter format
	* //@ emitter mimetype
* resource.rsc files
* scanCache.rsc files