s = input ("Enter a word : ")
t = s[0]
s3 = s[0]
for i in range (1,len(s)):
  if s[i] == t: 
     s3 += '#'
  else:
     s3 += s[i]
     
     
print(s3)