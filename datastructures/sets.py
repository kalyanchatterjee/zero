# Sets are immutable
projects = {"Alexur", "CEOtally", "DGC"}

myproject = "Alexur"

print (myproject in projects)

newprojects = ["Interesting One", "Profitable One"]

# Update
projects.update(newprojects)

print(projects)

# Usage - DFS, BFS - Knowing the existence of a key --- the "in" operator