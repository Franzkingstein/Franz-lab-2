def cs (string, substring):
   count  = 0 
   start = 0 
   while start (len(string)):
    pos = start.find(substring,start)
    if pos != -1:
      start = pos +1
      count +=1
    else:
       break
   return count
string = input("Enter a String")
substring = input("Enter the substring")
print(cs(string,substring))