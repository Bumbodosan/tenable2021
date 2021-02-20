import re

agestring = "\"age\""
usernamestring = "\"user_name\":\""

def ParseNamesByGroup(blob, group_name):
	matchingusers = []
	allmatches = re.findall("\[(.*?)\]", blob)
	for line in allmatches: 
		usernamesearch = re.search(usernamestring + "(.*?)\",", line)
		groupsearch = re.search("\"Group\":\"" + group_name + "\"", line)
		if usernamesearch and groupsearch: 
			matchingusers.append(usernamesearch.group(1))
	return matchingusers
   
# data = raw_input()
data = open("blob.data", "r")
group_name = data.split('|')[0]
blob = data.split('|')[1]
result_names_list = ParseNamesByGroup(blob, group_name)
print result_names_list