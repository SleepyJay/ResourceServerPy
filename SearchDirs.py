
import os

def searchHashified(start_path, looking_for):
	results = {}

	for (path,dirs,files) in os.walk(start_path):
		# skip hidden dirs blindly for now
		for dir in dirs:
			if(str(dir).startswith('.')):
				dirs.remove(dir)
			
		if(looking_for in str(path)):
			results[path] = files
		
		else:
			for filename in files:
				if(looking_for in str(filename)):
					if not path in results:
						results[path] = []
						
					results[path].append(filename)
	
	asList = []
	for key in results:
		asList.append(key)
		for file in results[key]:
			asList.append(os.path.join(key, file))
		
	return results


def searchAsPaths(start_path, looking_for):
	results = []

	for (path,dirs,files) in os.walk(start_path):
		# skip hidden dirs blindly for now
		for dir in dirs:
			if(str(dir).startswith('.')):
				dirs.remove(dir)
			
		if(looking_for in str(path)):
			results.append(path)
		
		else:
			for filename in files:
				if(looking_for in str(filename)):
					results.append(os.path.join(path, filename))
		
	return results

def buildFlat(start_path):
	results = {}

	for (path,dirs,files) in os.walk(start_path):
		# skip hidden dirs blindly for now
		for dir in dirs:
			if(str(dir).startswith('.')):
				dirs.remove(dir)
		
		for filename in files:
			path = os.path.join(dirname, name)
		
		if(looking_for in str(path)):
			results[path] = files
		
		else:
			for filename in files:
				if(looking_for in str(filename)):
					if not path in results:
						results[path] = []
						
					results[path].append(filename)
	
	return results	

# Build the directory structure as a hash
def buildStructure(start_path):
	results = {}
	followDirs(start_path, results)
	return {start_path: results}

# Follows a directory and fills in the hash as it goes
def followDirs(dirname, leaf):
	for name in os.listdir(dirname):
		path = os.path.join(dirname, name)

		if(str(name).startswith('.')):
			pass # skip hidden dirs blindly for now
		elif os.path.isdir(path):
			leaf[name] = {}
			followDirs(path, leaf[name])
		elif os.path.isfile(path):
			leaf[name] = None
	
			
def findInStructure(structure, lookingfor):
	pass
