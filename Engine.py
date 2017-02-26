#!/usr/bin/python


class Engine(object):
    
    def __init__(self, config, resources):
        self.config = config
        self.resources = resources

        self.dependencies = []


    #
    def buildDepenencyList(self, starting_name):
        to_check = [starting_name]

        imported_set = set()

        visited = set()
        has_unresolved = set()

        # unresolved dependencies and imports
        for res_name in to_check:
            if res_name in visited:
                continue
            visited.add(res_name)

            resource = self.resources[res_name]

            if not resource.unresolved:
                resource.unresolved = set()

            for req_name in resource.requires:
                # skip self-provided required
                if not req_name in resource.provides:
                    resource.unresolved.add(req_name)
                    has_unresolved.add(res_name)
                    
                to_check.append(req_name)

            for imp_name in resource.imports:
                imported_set.add(imp_name)
                to_check.append(imp_name)

            
        dependencies_set = set()
        
        last_dep_count = len(has_unresolved)

        # resolve dependencies -- NEEDS EDGE CASE TESTS!
        while len(has_unresolved):
            has_unresolved_list = list(has_unresolved)

            for res_name in has_unresolved_list:
                resource = self.resources[res_name]

                for unres_name in resource.unresolved:
                    res_needed = self.resources[unres_name]

                    if len(res_needed.unresolved):
                        continue

                    if not unres_name in dependencies_set:
                        dependencies_set.add(unres_name)
                        self.dependencies.extend(res_needed.provides)

                # remove already resolved
                resource.unresolved -= dependencies_set

                print "{} => {}".format(res_name, resource.unresolved)

                # when there are no unresolved, we can be added to depenencies
                if not len(resource.unresolved):
                    self.dependencies.append(res_name)
                    dependencies_set.add(res_name)
                    has_unresolved.remove(res_name)

            if last_dep_count == len(has_unresolved):
                # TODO: throw exception
                print "Nothing Resolved. Breaking out"
                break
            
            last_dep_count = len(has_unresolved)
        
        for imp_name in imported_set:
            self.dependencies.extend(self.resources[imp_name].provides)

        return self.dependencies
    
        
            

                



        

            




                

                


            

    




