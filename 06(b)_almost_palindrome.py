# O(n) Time | O(1) Space
def almost_palidrome(s):
	start=0
	end =len(s)-1
	while start < end:
		if s[start] != s[end]:
			return valid_palindorme(s,start+1,end) or valid_palindorme(s,start,end-1)
		start+=1
		end-=1
	return True 	






def valid_palindorme(s,start,end):
	while(start<end):
		if s[start] != s[end]:
			return False
		start+=1
		end-=1	
	return True		


print(almost_palidrome('abca'))	