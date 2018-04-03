from sys import argv

sciprt, filename = argv

fi = open(filename, 'w')

#print fi.read()
print fi
#fi.write("some string")
fi.close()