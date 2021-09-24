import sys

print("{:-^80}".format("sys.argv"))
print(sys.argv[0][-16:])

print("{:-^80}".format("sys.copyright"))
print(sys.copyright)

print("{:-^80}".format("sys.getwindowsversion()"))
print(sys.getwindowsversion())

print("{:-^80}".format("sys.version"))
print(sys.version)

print("{:-^80}".format("sys.path"))
print(sys.path)

sys.exit()