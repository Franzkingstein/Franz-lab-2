s = input(" Enter a string")
not_index = s.find("not")
bad_index = s.find("bad")
if not_index < bad_index:
    s = s.replace(s[not_index:bad_index+3],"Good")
print(s)
