# If the file is not present
f = open('sample.txt', 'w')
f.write("Hello world")
f.close()

# write multiline strings
f = open('sample_1.txt', 'w')
f.write('Hello world')
f.write('\nHow are you?')
f.close()

# If the file is already present
f = open('sample.txt', 'w')
f.write('shahrukh khan')
f.close()

# append mode
f = open('sample_1.txt', 'a')
f.write('\nI am fine')
f.close()

# write lines
L = ['hello\n', 'hi\n', 'how are you\n', 'I am fine']

f = open('sample.txt', 'w')
f.writelines(L)
f.close()

# reading from files
f = open('sample.txt', 'r')
s = f.read()
print(s)
f.close()

# reading upto n chars
f = open('sample.txt', 'r')
s = f.read(10)
print(s)
f.close()

# readline() -> to read line by line
f = open('sample.txt', 'r')
print(f.readline(), end='')
print(f.readline(), end='')
f.close()

# reading entire using readline
f = open('sample.txt', 'r')

while True:
  data = f.readline()

  if data == '':
    break
  else:
    print(data, end='')

f.close()

