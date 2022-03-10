# We are simply using the Python dictionary here

hashmap = {} 

hashmap["John"] = 18
hashmap["Anne"] = 36

print(hashmap["John"])

# It's worth mentioning that these are average case time complexity. 
# A hash table's worse time complexity is actually O(N) due to hash 
# collision and other things. For the vast majority of the cases and 
# certainly most coding interviews, the assumption of constant time 
# lookup/insert/delete is valid.