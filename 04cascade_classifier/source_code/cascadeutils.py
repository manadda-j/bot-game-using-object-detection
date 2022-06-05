import os

def generatePostitve(dir, name):
    with open('' + dir, 'w') as f:
        for filename in os.listdir(name):
            f.write(name + '/' + filename + '\n')

def generateNegative(dir, name):
    with open('' + dir, 'w') as f:
        for filename in os.listdir(name):
            f.write(name + '/' + filename + '\n')

if __name__ == '__main__':
    print('cascadeutils')
    # generatePostitve('pos.txt', 'positive')
    generateNegative('neg.txt', 'negative')

# https://docs.opencv.org/3.4.11/d3/d52/tutorial_windows_install.html
# https://sourceforge.net/projects/opencvlibrary/files/3.4.11/

# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=11Axel.txt --images=11Axel/
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=11Axel.txt --images=11Axel/
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=11Test.txt --images=11Raccoon/
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=11Axel.txt --images=11Axel/
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=11Axel.txt --images=11Axel/
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=positive.txt --images=fix-pos/


# generate positive samples from the annotations to get a vector file using:
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 5000 -vec pos.vec

# train the cascade-0 classifier model using:
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade-0/ -vec 11Axel.vec -bg 11Background.txt -w 24 -h 24
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade-0/ -vec 11Axel.vec -bg 11Background.txt -numPos 10 -numNeg 10000 -numStages 10 -w 24 -h 24
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade-0-1/ -vec pos.vec -bg neg.txt -numPos 2000 -numNeg 2000 -numStages 10 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999

# my final classifier training arguments:
# D:/NIDA/Instruction/2564-2/BADS7203/Project/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade-0/ -vec 11Test.vec -bg 11Background.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 50 -numNeg 1000 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999
# C:/Users/Ben/learncodebygaming/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade-0/ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 2604 -numNeg 1200 -numStages 20 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999
