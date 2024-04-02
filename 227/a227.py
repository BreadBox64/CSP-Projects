# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
from tkinter import *
from tkinter.scrolledtext import *
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import Style

root = Tk()
frame = Frame(root, padx = 8, pady = 8, bg = "#404040")
frame.grid(column = 0, row = 0)
for i in range(5):
	frame.grid_columnconfigure(i, pad = 8)
for i in range(4):
	frame.grid_rowconfigure(i, pad = 8)

# Save function.
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open(filename, mode = 'w')
  text = textBox.get("1.0", END)
  
  file.write(text)
  file.close()

def genExec(command):
	def f():    
		textBox.delete(1.0, END)
		textBox.insert(END, command + " working...\n")
		textBox.update()
		url = urlEntry.get()
		url = "::1" if len(url) == 0 else url

		p = subprocess.Popen(command + ' ' + url, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		cmd_results, cmd_errors = p.communicate()

		textBox.insert(END, cmd_results)
		textBox.insert(END, cmd_errors)
	return f

commandFrame = Frame(frame, borderwidth = 2, relief = 'solid', bg = "#404040")
commandFrame.grid(column = 0, row = 0, columnspan = 3, sticky = "ew")
for i in range(3):
	commandFrame.grid_columnconfigure(i, weight = 1)

pingButton = Button(commandFrame, text = "ping", command = genExec('ping'), bg = "#404040", fg = "#FFFFFF")
pingButton.grid(column = 0, row = 0, sticky = "ew", padx = 4, pady = 4)
tracertButton = Button(commandFrame, text = "tracert", command = genExec('tracert'), bg = "#404040", fg = "#FFFFFF")
tracertButton.grid(column = 1, row = 0, sticky = "ew", padx = 4, pady = 4)
nslookupButton = Button(commandFrame, text = "nslookup", command = genExec('nslookup'), bg = "#404040", fg = "#FFFFFF")
nslookupButton.grid(column = 2, row = 0, sticky = "ew", padx = 4, pady = 4)

saveButton = Button(frame, text = "Save Results", command = mSave, bg = "#404040", fg = "#FFFFFF")
saveButton.grid(column = 4, row = 0)

urlLabel = Label(frame, text = "Enter a URL of interest: ", 
	compound = "center",
	font = ("arial", 14),
	bd = 0, 
	relief = FLAT,
	bg = "#404040",
	fg = "#FFFFFF")
urlLabel.grid(column = 1, row = 3)
urlEntry = Entry(frame, font = ("arial", 14), bg = "#404040", fg = "#FFFFFF")
urlEntry.grid(column = 2, row = 3, columnspan = 2, sticky = "nsew")
textBox = ScrolledText(frame, height = 10, width = 100, bg = "#404040", fg = "#FFFFFF")
textBox.grid(column = 0, row = 1, columnspan = 5, rowspan = 2)

root.mainloop()