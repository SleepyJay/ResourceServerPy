# ResourceServerPy - Readme
ResourceServer ported to Python

### Introduction
ResourceServer was a project written to manage JavaScript class/file dependencies. Originally, it was written in Perl and AFAIK, is still used in production code in a previous company. 

The idea is that a single request is made for a named resource in a particular directory--think RESTful. This directory will have a certain configuration file inside, and thus it is possible to use a different configuraion by using a different URL. The named resource looks like a filename, but it is treated as a starting point for collecting dependencies. 

Each source file will describe the resources that it requires (these must come before the source), imports (these can come at any point) and provides (the names of resources provided by this source file). These are the basis for the actual stream of data that would be returned in the response. 

Note that because we are using resource names, we don't have to track where files physically live on disk anymore. They can move around without having to alter HTML or other files. 

This project is in the early stages. There are tons of features to add, such as caching the scan data, manipulating the output, outputting debug information, etc. Also, we could be using this for many kinds of data, such as CSS or even Images. 

### Examples
Suppose you request a JavaScript source, such as:
```
http://project.domain.com/resource/dinner/com.sleepjay.cheeseburger.jsr
```

First, we find a configuration file inside ```resource/dinner/```. This will describe all of the source directories we should scan for source files and compile information for use later. 

Next, we start with our resource in the request, in this example ```com.sleepjay.cheeseburger``` (also, the extension can be used to denote that we only care about JS files). Each resource that ```com.sleepjay.cheeseburger``` depends on will collect it's dependencies and so on. This list of resources is then sorted in such a way that the dependencies are properly sorted. 

Last, we take this list, pull all of the sources, and compile an ordered stream of the files these resources represent. This data would be sent back in the response.


### Running 
Provided is a run.py file. This runs through an example file path and print a lot of messages, serving as a manual test of the code. Better testing coverage is planned, as well as handling requests, routes, and responses.  

