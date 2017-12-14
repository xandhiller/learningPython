import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = "* " + lines[i]

for i in range(len(lines)):
    print(lines[i])

# Save lines in the 'text' variable

text = ''
for i in range(len(lines)):
    text = text + lines[i]+"\n"

pyperclip.copy(text)
