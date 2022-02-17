#palindrome number

x=input().lower()
rev=x[::-1]
m_p = int((len(x)-1)/2)
if (x[:m_p] == rev[:m_p]):
	print("Palindrome")
else:
	print("Not Palindrome") 