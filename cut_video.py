import cv2, os, re
import math
import numpy as np
import json as js
import libs.find_file_by_kwd as ff
import libs.time_frame_converter as tfc


INPUT_DIR_NAME = "vids"
OUTPUT_DIR_NAME = "pics"
COMMON_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def editFrame(frame, x1, y1, sz):
    return frame[y1:y1+sz, x1:x1+sz]

def savePic(outDir, ss, c, pic):
    pic_ext = '.png'
    for s in ss:
        if(c<s[1]):
            detailDir = os.path.join(outDir,s[0])
            cv2.imwrite( os.path.join(detailDir,str(int(c))+pic_ext), pic)
            break

def vid2Pics(inDir, outDir, tgt, ext):
    fps = 0
    fCounter = 0
    videoName = tgt["name"] + ext
    videoStatus = []

    # get video object
    cap = cv2.VideoCapture( os.path.join(inDir, videoName) )
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    # get frame rate
    if int(major_ver)  < 3 :
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        print( "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps) )
    else :
        fps = cap.get(cv2.CAP_PROP_FPS)

    for s in tgt["status"]:
        end_time = 0
        if(s["until"] == "inf"):
            end_time = float("inf")
        else:
            end_time = tfc.timeStr2frame(s["until"], fps)
        videoStatus.append( (s["label"],end_time ) )

    # start capture
    while( cap.isOpened() ):
        ret, frame = cap.read()
        if(ret):
            if( fCounter%math.ceil(fps)==0 ):
                # do resize or some actions.
                edited_frame = editFrame(frame, 210, 120, 360)
                # save picture
                savePic(outDir, videoStatus, fCounter, edited_frame)
                # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # cv2.imshow('frame',gray)
            fCounter = fCounter +1
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()


def controlSaveDir(fName):
    picDir = os.path.join(COMMON_DIR_PATH, OUTPUT_DIR_NAME)
    if not os.path.exists(picDir):
        os.makedirs(picDir)

    fileDir = os.path.join(picDir, fName)
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)

    return fileDir

def makeSaveDirs(jContents):
    for c in jContents["videoAndLabels"]:
        for s in c["status"]:
            controlSaveDir(s["label"])



def main():
    inDir = os.path.join(COMMON_DIR_PATH, INPUT_DIR_NAME)

    jContents = []
    for jName in ff.findFNameInDirByKwd(inDir, "json"):
        with open( os.path.join(inDir, jName) , 'r') as jFile:
            jContents = js.load(jFile)

    makeSaveDirs(jContents)

    if os.path.exists(inDir):
        # use each file @json file
        for content in jContents["videoAndLabels"]:
            print(content["name"])
            tgtFiles = ff.findFNameInDirByKwd(inDir, content["name"])
            # cut file which is realy existed in vid dir.
            outDir = os.path.join(COMMON_DIR_PATH, OUTPUT_DIR_NAME)
            # _, ext = os.path.splitext(tgt)
            vid2Pics(inDir, outDir, content, ".mp4")
    else:
        print("make directory '{}', and put videos in it.".format(inDir))

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

