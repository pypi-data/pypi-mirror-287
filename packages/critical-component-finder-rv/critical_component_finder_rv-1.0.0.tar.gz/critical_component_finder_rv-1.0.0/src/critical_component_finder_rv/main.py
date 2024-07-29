import os
import re
from sys import exit
import argparse
import codecs
from collections import defaultdict
from graphviz import Digraph
import networkx as nx

valid_headers = ['h', '.hpp']
valid_sources = ['.c', '.cc', '.cpp']
valid_extensions = valid_headers + valid_sources
found_dirs = dict()
include_regex = re.compile('#include\s+["<"](.*)[">]')
graph_color = 'red'
files = []

def get_extension(path):
    return path[path.rfind('.'):]

def find_all_headers_in_include(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            find_all_headers_in_include(entry.path)
        else:
            if get_extension(entry.path) in valid_headers:
                entry_components = entry.path.split('/')
                iter = 0

                while entry_components[iter] != 'include':
                    iter += 1

                entry_components = entry_components[iter + 1:]
                name = ''
                for component in entry_components:
                    name += component + '/'

                found_dirs[name[:-1]] = entry.path

def find_all_files(path):
    files = []
    for entry in os.scandir(path):
        if entry.path[entry.path.rfind('/'):] == '/include':
            find_all_headers_in_include(entry.path)
        if entry.is_dir():
            files += find_all_files(entry.path)
        elif get_extension(entry.path) in valid_extensions:
            files.append(entry.path)
    return files

def find_neighbors(path, root_folder):
    f = codecs.open(path, 'r', "utf-8", "ignore")
    code = f.read()
    f.close()
    includes = include_regex.findall(code)
    res = []

    for include in includes:
        curr_dir = path[0:path.rfind('/')]

        if include in found_dirs:
            res.append(found_dirs[include])
            continue

        found_header = False
        
        while (True):
            possible_header_path  = curr_dir + '/' + include
            if os.path.exists(possible_header_path):
                res.append(os.path.abspath(possible_header_path))
                found_header = True
                break
            curr_dir = curr_dir[0:curr_dir.rfind('/')]
            if (curr_dir  == root_folder):
             break
        if (found_header):
            continue
        res.append('@unknownlib@/' + include)    

    return res

def create_graph(files, create_cluster, label_cluster, strict):
	folder_to_files = defaultdict(list)
	for path in files:
		folder_to_files[os.path.dirname(path)].append(path)
	nodes = {path for path in files}
	graph = Digraph(strict=strict)
	for folder in folder_to_files:
		with graph.subgraph(name='cluster_{}'.format(folder)) as cluster:
			for path in folder_to_files[folder]:
				color = 'black'
				node = path
				ext = get_extension(path)
				if ext in valid_extensions:
					color = graph_color
				if create_cluster:
					cluster.node(node)
				graph.node(node)
				neighbors = find_neighbors(path)
				for neighbor in neighbors:
					if neighbor != node and neighbor in nodes:
						graph.edge(node, neighbor, color=color)
			if create_cluster and label_cluster:
				cluster.attr(label=folder)
	return graph

def lines(path):
    with open(path, 'r', encoding="utf-8") as file:
        counter = 0
        for line in file:
            counter += 1

        return counter

def create_nx_graph(files):
	graph = nx.DiGraph()
	folder_to_files = defaultdict(list)
	for path in files:
		folder_to_files[os.path.dirname(path)].append(path)
	for path in files:
		graph.add_node(path)

	for folder in folder_to_files:
		for path in folder_to_files[folder]:
			node = path
			neighbors = find_neighbors(path)
			for neighbor in neighbors:
				if neighbor != node and graph.has_node(neighbor):
					graph.add_edge(neighbor, node, weight = lines(neighbor))
                
	return graph

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('folder', help='Path to the folder to scan')
	parser.add_argument('output', help='Path of the output file without the extension')
	parser.add_argument('-f', '--format', help='Format of the output', default='pdf', \
		choices=['bmp', 'gif', 'jpg', 'png', 'pdf', 'svg'])
	parser.add_argument('-v', '--view', action='store_true', help='View the graph')
	parser.add_argument('-c', '--cluster', action='store_true', help='Create a cluster for each subfolder')
	parser.add_argument('--cluster-labels', dest='cluster_labels', action='store_true', help='Label subfolder clusters')
	parser.add_argument('-s', '--strict', action='store_true', help='Rendering should merge multi-edges', default=False)
	parser.add_argument('-cc','--critical-component', action = 'store_true', help = 'Finds longest to compile chain')
	args = parser.parse_args()
	files = find_all_files(args.folder)
	graph = create_graph(files, args.cluster, args.cluster_labels, args.strict)
	graph.render(args.output, cleanup=True, view=args.view)
	if (args.critical_component):
		graph = create_nx_graph(files)
		try:
			longest_path = nx.dag_longest_path(graph, weight='weight')
			print(*longest_path)
		except nx.HasACycle:
			print("Include map has cycles!")
			exit()