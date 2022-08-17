s1 = ''.join([chr(i) for i in range(ord('0'), ord('9'))])
s2 = ''.join([chr(i) for i in range(ord('A'), ord('z'))])
s3 = ''.join([chr(i) for i in range(ord('0'), ord('Z'))])
s4 = ''.join([chr(i) for i in range(ord('а'), ord('я'))])

print(s1, s2, s3, s4, sep='\n\n')

q = '1\u2155'
print(q, 
       f'{q.isdecimal() = }', 
       f'{q.isdigit() = }', 
       f'{q.isnumeric() = }',
       sep='\n', end='\n\n')
