import os
from sys import argv, getsizeof
from time import time
from hashlib import sha256


def process(directory):
    children = os.listdir(directory)
    for child in children:
        childpath = directory + "\\%s" % child
        if os.path.isdir(childpath):
            print("Processing directory %s" % childpath)
            process(childpath)
        elif os.path.isfile(childpath):
            logdetails(childpath)


def logdetails(filepath):
    if not os.path.isfile(filepath):
        print("Asked to log details of something not a file, returning.")
        print("Path: %s" % filepath)
        return False
    filename = os.path.basename(filepath)
    filehash = hashfile(filepath)
    filesize = os.path.getsize(filepath)
    _files[filepath] = (filename, filehash, filesize)
    if filehash in _hashes.keys():
        _hashes[filehash].append(filepath)
    else:
        _hashes[filehash] = [filepath]


def hashfile(path):
    buffer_size = 65536
    shasha = sha256()
    with open(path, 'rb') as filetohash:
        while True:
            data = filetohash.read(buffer_size)
            if not data:
                break
            shasha.update(data)
    return shasha.hexdigest()


def distilhashes(hashes):
    newhashes = {}
    for hashvalue in hashes.keys():
        if len(hashes[hashvalue]) > 1:
            newhashes[hashvalue] = hashes[hashvalue]
    return newhashes


def reducetounit(number, exponent=0):
    if number < 1024:
        return "{:,.3g}".format(number) + " " + getbytesunit(exponent)
    else:
        return reducetounit(number / 1024, exponent + 1)


def getbytesunit(exponent):
    return {
        0: 'bytes',
        1: 'kB',
        2: 'MB',
        3: 'GB',
        4: 'TB',
        5: 'PB',
    }.get(exponent, False)


if len(argv) > 1:
    _rootpath = argv[1]
else:
    _rootpath = os.getcwd()
# _rootpath = os.getcwd() + '\\sample'
if not os.path.exists(_rootpath):
    print("Provided path does not exists.")
    exit(1)
if not os.path.isdir(_rootpath):
    print("Provided path not a directory.")
    exit(1)

_timestart = time()
print("Processing path %s" % _rootpath)

_files = {}
_hashes = {}
process(_rootpath)
_timeend = time()
_timetaken = _timeend - _timestart


print("Files processed:")
for _filepath in _files.keys():
    _filename, _filehash, _filesize = _files[_filepath]
    print("  %s: \n    %s\n    %s\n    %d" % (_filepath, _filename, _filehash, _filesize))

_duplicates = distilhashes(_hashes)
_totalduplicatespace = 0
if len(_duplicates) > 0:
    print("\n\nDuplicates found:")
    for _duplicate in _duplicates.keys():
        print("\n  Duplicate hash: %s" % _duplicate)
        _filesize = 0
        for _duplicatepath in _duplicates[_duplicate]:
            _filesize = os.path.getsize(_duplicatepath)
            print("     %s" % _duplicatepath)
        _duplicatespace = _filesize * (len(_duplicates[_duplicate]) - 1)
        print("  Space wasted: %s " % reducetounit(_duplicatespace))
        _totalduplicatespace += _duplicatespace
else:
    print("\n\nNO DUPLICATES FOUND")

print("\nRun statistics:")
print("  Time taken: {0:.2f} seconds".format(_timetaken))
print("  File count: {:,}".format(len(_files)))
print("  File list in memory: %s" % reducetounit(getsizeof(_files)))
print("  Duplicate hashes found: {:,}".format(len(_duplicates)))
print("  Duplicate hashes list in memory: %s" % reducetounit(getsizeof(_duplicates)))
print("  Space wasted by duplicates: %s" % reducetounit(_totalduplicatespace))
