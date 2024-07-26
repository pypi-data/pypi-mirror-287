"""
# Merge-Conda-YAML

This is a very simple piece of script that allows user to merge multiple YAML 
files generated by anaconda into a single unified YAML. The output of this script is two filetypes, 
one is the merged YAML file while the other is the requirements.txt file ready to be scanned by pip.

- Four yamls are saved in a directory:
  - One with default entries
  - One with versions of all entries
  - One with versions of only prioritized entries (defined in `getPiorityList()` function)
  - One with only the names of the packages
- Three .txts are saved in the same directory:
  - One with versions of all entries
  - One with versions of only prioritized entries (defined in `getPiorityList()` function)
  - One with only the names of the packages

**Changing Output Filenames**

In order to change the name of the output files, edit the "dump(output_yaml)" function definition.

**Changing Priority List**

The list of prioritized packages is defined in "getPiorityList()" function definition and can be changed from there

Usage:

`cli_conda_merge /path/to/env1.yaml /path/to/env2.yaml`

"""


import sys
import argparse
import os
import datetime
from os import path
from collections import OrderedDict, deque
from copy import deepcopy

import yaml


class MergeError (Exception):
    """Exceptions that will be used to notify users if any error occurred during the merge"""
    pass


def getPriorityList():
    """ 
    A simple funciton that reutrns all the packages that 
    need to be treated as high-priority dependencies 
    """
    priorities = ['pytorch', 'tensorflow']
    return priorities


def prioritySort(dependencies):
    """ 
    Function that will sort the dependencies for pip's requirements.txt format
    while prioritizing the packages defined in getPriorityList() function
    """
    priorityList = getPriorityList()

    # Removing duplicates
    dependencies = list(dict.fromkeys(dependencies))

    for i in dependencies:
        for priority in priorityList:
            if i.startswith(priority):
                dependencies.insert(0, dependencies.pop(dependencies.index(i)))
                continue

    return dependencies


def getPipRequirementsContent(dependencies, versions=True, priorityVersions=True):
    """ Function to convert conda dependencies and pip dependencies to a single pip list and sort it """
    priorityList = getPriorityList()

    if isinstance(dependencies[-1], dict):
        pips = dependencies.pop(-1)
        pips = pips.get('pip')
    else:
        pips = []

    # Add one "=" sign to match with pip's requirements
    if versions:
        for i in range(0, len(dependencies)):
            entry = dependencies[i]
            if "=" in entry:
                name = entry[:entry.index("=")]
                entry = entry[entry.index("="):]
                formattedEntry = name + "=" + entry
                dependencies[i] = formattedEntry

    # Add pips in the full list
    for pip in pips:
        dependencies.append(pip)

    # Priority sort pips
    dependencies = prioritySort(dependencies)

    # Manipulate version numbers based on function arguments
    if versions:
        # Remove duplicates
        dependencies = list(dict.fromkeys(dependencies))
        return dependencies
    else:
        if priorityVersions:
            for i in range(0, len(dependencies)):
                isPriority = False
                for priority in priorityList:
                    if dependencies[i].startswith(priority):
                        isPriority = True
                        break
                if isPriority:
                    continue
                else:
                    if "=" in dependencies[i]:
                        dependencies[i] = dependencies[i][:dependencies[i].index(
                            "=")]
            # Remove duplicates
            dependencies = list(dict.fromkeys(dependencies))
            return dependencies
        else:
            for i in range(0, len(dependencies)):
                if "=" in dependencies[i]:
                    dependencies[i] = dependencies[i][:dependencies[i].index(
                        "=")]
            # Remove duplicates
            dependencies = list(dict.fromkeys(dependencies))
            return dependencies


def sortYamlDeps(dependencies):
    """ Function that will sort and prioritize dependencies of the environment YAML """
    # # ! this line assumes that there is always a pip at the end
    # # of dependencies and thus runs into error
    # pips = dependencies[len(dependencies)-1]

    # # Convert pips to list
    # """
    # remember to convert it back to dict. like this:
    # """
    # pips = pips.get('pip')

    # seperate conda packages from pip packages
    # we need to make sure there is a pip dict at the end
    if isinstance(dependencies[-1], dict):

        pips = dependencies.pop(-1)
        print(pips)
        # convert pips from a dict to a list for a simpler comparision
        pips = pips.get('pip')

        # Remove duplicates from pip. If conda package of the same
        # name is available, remove its counterpart from pip.
        for condadep in dependencies:
            for pipdep in pips:
                if condadep.startswith(pipdep) or pipdep.startswith(condadep):
                    pips.remove(pipdep)

        # Sort both lists based on priorities
        dependencies = prioritySort(dependencies)
        pips = prioritySort(pips)

        # Put pips back in dependencies list as a dict
        dependencies.append({'pip': pips})
    else:
        dependencies = prioritySort(dependencies)

    return dependencies


def stripPinnedDep(dep):
    """ Function to strip the pinned dependency from an entry """
    if "=" in dep:
        name = dep[:dep.index("=")]

    dep = dep[dep.index("=")+1:]

    if "=" in dep:
        version = dep[:dep.index("=")]
    else:
        version = dep

    return (name + "=" + version)


def stripPinnedVerDep(dep):
    """ Function to keep only the package name and remove everything else """
    if "=" in dep:
        name = dep[:dep.index("=")]
    else:
        return dep
    return name


def removePinnedDependencies(dependencies, versions=True, priorityVersions=True):
    """ 
    Function that will strip down each dpendency based on the arguments recieved.
     -If versions is True, version of all entries will be left untouched, if it 
      is False, all versions will be removed.
     -If priorityVersions is True, the versions of prioritized package's will be
      untouched regardless of the 'version' variable.
    """
    newDeps = []
    priorityList = getPriorityList()
    pips_present = False
    for i in dependencies:
        isPriority = False
        # Ignore pip as they already have pinned versions and nothing else
        if isinstance(i, dict):
            pips = i
            pips_present = True
            continue

        # Dealing with entries and keeping pinned versions of all entries
        if (versions):
            newDeps.append(stripPinnedDep(i))

        # Dealing with entries and keeping pinned versions of only the priorities
        if not versions:
            if priorityVersions:
                for priority in priorityList:
                    if i.startswith(priority):
                        isPriority = True
                        break
                if isPriority:
                    newDeps.append(stripPinnedDep(i))
                    continue
                else:
                    newDeps.append(stripPinnedVerDep(i))
            else:
                newDeps.append(stripPinnedVerDep(i))

    # Removing duplicates
    newDeps = list(dict.fromkeys(newDeps))
    # only append if pip was found in yaml file
    if pips_present:
        newDeps.append(pips)

    return newDeps


def dump(output_yaml):
    """Function used to dump the final state of the output files

    This Function will deal with the dumping of the merged YAML
    file as well as the requirements.txt file formatted to be used by PIP

    """
    # Outputting to files
    today = datetime.datetime.today()
    suffix = str(today.day) + str(today.month) + "_" + \
        str(today.hour) + str(today.minute) + str(today.second)
    directory = "conda_merge_result_{}".format(suffix)
    cwd = os.getcwd()
    cwd = path.join(cwd, directory)
    if not path.isdir(cwd):
        try:
            os.mkdir(cwd)
        except OSError:
            print("Creation of path %s failed" % path)

    outputyamlfilename = "conda_env_merged"
    outputreqfilename = "requirements_merged"

    # Writing YAML file with pinned versions and dependencies
    pVpDDeps = sortYamlDeps(output_yaml.get('dependencies'))
    output_yaml['dependencies'] = pVpDDeps
    with open(path.join(cwd, outputyamlfilename + "_default.yml"), 'w') as f:
        yaml.dump(output_yaml, f, indent=2, default_flow_style=False)

    # Writing YAML file with pinned versions only
    pVDeps = removePinnedDependencies(pVpDDeps.copy())
    output_yaml['dependencies'] = pVDeps
    with open(path.join(cwd, outputyamlfilename + "_versions_all.yml"), 'w') as f:
        yaml.dump(output_yaml, f, indent=2, default_flow_style=False)

    # Writing YAML file with pinned versions of prioritized packages only
    pVPriorityDeps = removePinnedDependencies(
        pVpDDeps.copy(), versions=False, priorityVersions=True)
    output_yaml['dependencies'] = pVPriorityDeps
    with open(path.join(cwd, outputyamlfilename + "_versions_priority.yml"), 'w') as f:
        yaml.dump(output_yaml, f, indent=2, default_flow_style=False)

    # Writing YAML file with package names only
    nameOnlyDeps = removePinnedDependencies(
        pVpDDeps.copy(), versions=False, priorityVersions=False)
    output_yaml['dependencies'] = nameOnlyDeps
    with open(path.join(cwd, outputyamlfilename + "_names_only.yml"), 'w') as f:
        yaml.dump(output_yaml, f, indent=2, default_flow_style=False)

    # Writing requirements.txt file with versions
    pipListVersionsAll = getPipRequirementsContent(pVDeps.copy())
    with open(path.join(cwd, outputreqfilename + "_versions_all.txt"), 'w') as rf:
        for pipdep in pipListVersionsAll:
            rf.write(pipdep)
            rf.write("\n")

    # Writing requirements.txt file with versions of prioritized packages only
    pipListVersionsPriority = getPipRequirementsContent(
        pVDeps.copy(), versions=False)
    with open(path.join(cwd, outputreqfilename + "_versions_priority.txt"), 'w') as rf:
        for pipdep in pipListVersionsPriority:
            rf.write(pipdep)
            rf.write("\n")

    # Writing requirements.txt file with no versions
    pipListVersionsNone = getPipRequirementsContent(
        pVDeps.copy(), versions=False, priorityVersions=False)
    with open(path.join(cwd, outputreqfilename + "_names_only.txt"), 'w') as rf:
        for pipdep in pipListVersionsNone:
            rf.write(pipdep)
            rf.write("\n")

    print("\nThe output YAML and pip requirements have been written in {} and {}.".format(
        outputyamlfilename, outputreqfilename))


def merge_envs(args):
    """Main entry point for the script"""
    # Check if all the yaml files exist
    for f in args.yamls:
        if not path.exists(f):
            raise MergeError("The following file does not exist: {}".format(f))

    # Load all files
    yaml_files = []
    for f in args.yamls:
        with open(f) as file:
            yaml_files.append(yaml.safe_load(file))

    # The main loop that will be calling the merge files fucntion
    output_yaml = {}
    for i in range(0, len(yaml_files)):
        if i == 0:
            output_yaml = yaml_files[i]
            continue
        output_yaml = merge(output_yaml, yaml_files[i])

    dump(output_yaml)


def merge(yaml1, yaml2):
    """Function that will handle the merging of two yamls"""
    # Extracting keys out from both the YAMLs
    keys1 = []
    keys2 = []
    keys_output = ['name', 'channels', 'dependencies']
    merged_yaml = {}

    for key, _ in yaml1.items():
        keys1.append(key)
    for key, _ in yaml2.items():
        keys2.append(key)

    # Making sure that the YAMLs are in proper format"""
    # TODO: add name of the YAML file that has faulty format
    if ('channels' not in keys1 or 'dependencies' not in keys1 or 'channels' not in keys2 or 'dependencies' not in keys2):
        raise MergeError(
            "One of the YAML files seems to be corrupted. Please make sure that it is in proper format. (Proper format must contain 'channels' and 'dependencies' keys.")

    # Resolve name of the output file's env
    # If a name does not exist in both yamls, use a generic placeholder
    outputName = yaml1.get(keys_output[0])
    if outputName is None:
        outputName = yaml2.get(keys_output[0])
        if outputName is None:
            outputName = "myenv"    # Generic placeholder
    merged_yaml[keys_output[0]] = outputName

    # Merging channels while keeping their priorities in mind
    try:
        env_definitions = [yaml1, yaml2]
        output_channels = merge_channels(
            env.get('channels') for env in env_definitions)
    except MergeError as exc:
        print("Falied to merge channel priorities.\n{}\n".format(exc.args[0]),
              file=sys.stderr)
        raise
    if output_channels:
        merged_yaml[keys_output[1]] = output_channels

    # Merging dependencies (including pip dependencies)
    output_dependencies = resolve_dependencies(
        env.get('dependencies') for env in env_definitions)

    if output_dependencies:
        merged_yaml[keys_output[2]] = output_dependencies
    return merged_yaml


def resolve_dependencies(dependencies_list):
    """Merge all dependencies to one list and return it.

    Two overlapping dependencies (e.g. package-a and package-a=1.0.0) are not
    unified, and both are left in the list (except cases of exactly the same
    dependency). Conda itself handles that very well so no need to do this ourselves.

    """
    pips = []
    merged_dependencies = []
    for dependenciess in dependencies_list:
        if dependenciess is None:  # not found in this environment definition
            continue
        for dep in dependenciess:
            if isinstance(dep, dict) and dep['pip']:
                pips.append(dep['pip'])
            elif dep not in merged_dependencies:
                merged_dependencies.append(dep)
    merged_dependencies = sorted(merged_dependencies)
    if pips:
        piplist = merge_pips(pips)
        merged_dependencies.append(piplist)
    return merged_dependencies


def merge_pips(pips):
    """Merge pip requirements lists the same way as `merge_dependencies` work"""
    return {'pip': sorted({req for reqs in pips for req in reqs})}


def merge_channels(channels_list):
    """Merge multiple channel priorities list and output a unified one.

    Use a directed-acyclic graph to create a topological sort of the priorities,
    so that the order from each environment file will be preserved in the output.
    If this cannot be satisfied, a MergeError is raised.
    If no channel priories are found (all are None), return an emply list.
    This part of code is an extract taken from https://github.com/amitbeka/conda-merge
    """
    dag = DAG()
    try:
        for channels in channels_list:
            if channels is None:  # not found in this environment definition
                continue
            for i, channel in enumerate(channels):
                dag.add_node(channel)
                if i > 0:
                    dag.add_edge(channels[i-1], channel)
        return dag.topological_sort()
    except ValueError as exc:
        raise MergeError(
            "Can't satisfy channels priority: {}".format(exc.args[0]))


class DAG(object):
    """Directed acyclic graph for merging channel priorities.

    This is a stripped down version adopted from:
    https://github.com/thieman/py-dag (MIT license)

    """

    def __init__(self):
        """ DAG:__init__
        Args:
        Returns:
           
        """
        self.graph = OrderedDict()

    def __len__(self):
        """ DAG:__len__
        Args:
        Returns:
           
        """
        return len(self.graph)

    def add_node(self, node_name):
        """ DAG:add_node
        Args:
            node_name:     
        Returns:
           
        """
        if node_name not in self.graph:
            self.graph[node_name] = []

    def add_edge(self, from_node, to_node):
        """ DAG:add_edge
        Args:
            from_node:     
            to_node:     
        Returns:
           
        """
        if from_node not in self.graph or to_node not in self.graph:
            raise KeyError('one or more nodes do not exist in graph')
        if to_node not in self.graph[from_node]:
            test_graph = deepcopy(self.graph)
            test_graph[from_node].append(to_node)
            if self.validate():
                self.graph[from_node].append(to_node)
            else:
                raise ValueError("{} -> {}".format(from_node, to_node))

    @property
    def independent_nodes(self):
        """Return a list of all nodes in the graph with no dependencies."""
        dependent_nodes = set(node for dependents in self.graph.values()
                              for node in dependents)
        return [node for node in self.graph.keys()
                if node not in dependent_nodes]

    def validate(self):
        """Return whether the graph doesn't contain a cycle"""
        if len(self.independent_nodes) > 0:
            try:
                self.topological_sort()
                return True
            except ValueError:
                return False
        return False

    def topological_sort(self):
        """Return a topological ordering of the DAG.

        Raise an error if this is not possible (graph is not valid).

        """
        in_degree = {}
        for node in self.graph:
            in_degree[node] = 0

        for from_node in self.graph:
            for to_node in self.graph[from_node]:
                in_degree[to_node] += 1

        queue = deque()
        for node in in_degree:
            if in_degree[node] == 0:
                queue.appendleft(node)

        sorted_nodes = []
        while queue:
            independent_node = queue.pop()
            sorted_nodes.append(independent_node)
            for next_node in self.graph[independent_node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.appendleft(next_node)

        if len(sorted_nodes) == len(self.graph):
            return sorted_nodes
        else:
            raise ValueError('graph is not acyclic')


def parse_args():
    """Parse command line arguments (or user provided ones as list)"""
    description = ""
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    # Place the files that were recieved in 'yamls' namespace
    parser.add_argument('yamls', nargs='*', default="",
                        help="File path(s) to conda yaml file(s) to be merged sperated by a space.")
    # parser.add_argument('--output', '-o', default="merged_output.yaml",
    #                     help='Name of merged output file.')
    return parser.parse_args()


def main():
    """Main entry point for console_scripts of setup.py"""
    args = parse_args()
    try:
        merge_envs(args)
    except MergeError:
        return 1


if __name__ == '__main__':
    main()
