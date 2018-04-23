import os, glob


def findFNameInDirByKwdCore(dirPath, kwd, tgt):
    tgt = os.path.join(dirPath, tgt.format(kwd))
    return [os.path.basename(r) for r in glob.glob(tgt)]

def findFNameInDirByKwd(dirPath, kwd):
    return findFNameInDirByKwdCore(dirPath, kwd, "*{}*")

def findFNameInDirByKwdHead(dirPath, kwd):
    return findFNameInDirByKwdCore(dirPath, kwd, "{}*")

def findFNameInDirByKwdTail(dirPath, kwd):
    return findFNameInDirByKwdCore(dirPath, kwd, "*{}")

def findFNameInDirByKwds(dirPath, kwds):
    fileList = []
    for k in kwds:
        fileList.extend( findFNameInDirByKwd(dirPath, k) )
    return fileList

#
# def main():
#     INPUT_DIR_NAME = "vids"
#     fnames = [ "201801232200"
#              , "dummy"
#              ]
# 
#     d = os.path.dirname(os.path.realpath(__file__))
#     d = os.path.dirname(d)
#     inDir = os.path.join(d, INPUT_DIR_NAME)
# 
#     fileList.extend( findFNameInDirByKwds(inDir, fnames) )
# 
# if __name__ == '__main__':
#     main()
#

