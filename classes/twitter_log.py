class Twitter_log_csv:
			
	def save_csv(self, dfs_list, names_list):
		""" get list of dataframes and list of strings.
		Saves dataframes to .csv with names of strings
		inside /csv folder"""
		for i in range(len(dfs_list)):
			dfs_list[i].to_csv("./csv/"+names_list[i], index=False, encoding='utf-8')
			