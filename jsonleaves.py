import json
import sys

class JSONLeaves:
	def json_paths(self, json_string):
		json_dict = json.JSONDecoder().decode(json_string)
		paths = self.dict_paths(json_dict)
		path_dict = {}
		for path in paths:
			path_dict[path[0]] = path[1]
		return json.dumps(path_dict, sort_keys=True, indent=4, separators=(',', ': '))

	def list_to_path(self, path_list):
		path = str(path_list[0])
		for item in path_list[1:len(path_list)]:
				path += "." + str(item)
		return path

	def dict_paths(self, dictionary, root = []):
		if type(dictionary) is not dict:
			item_path = self.list_to_path(root)
			return [(item_path, dictionary)]

		paths = []
		root = list(root)
		for key, value in dictionary.items():
			sub_tree_root = root + [key]
			items =  self.dict_paths(value, sub_tree_root)
			for item in items:
				paths.append(item)
		return paths

json_terminal = JSONLeaves()
sys.stdout.write(json_terminal.json_paths(sys.stdin.read()))
sys.stdout.write("\n")