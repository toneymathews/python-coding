# UDDDUDUU. ans is 1. only one valley will be counted between two sea levels. initial position is sealevel
#Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike, he took exactly  steps. For every step he took, he noted if it was an uphill or a downhill step. Gary's hikes start and end at sea level. We define the following terms:
#
#A mountain is a non-empty sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
#A valley is a non-empty sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
#Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
status = 0
valley = 0
n = int(input().strip())
#steps = [str(steps_temp) for steps_temp in input().strip().split(' ')]
steps = str(input().strip())
#print (steps)
for i in range(0,len(steps)):
     if steps[i] == "U":
        status = status+1
     else:
        status = status-1
     if (status == 0 and steps[i] == "U" and i != 0):
        valley = valley + 1
print (valley)



#print (len(steps))
#for i in range(1,len(steps)):
#    if steps[i] == "U":
#        status = status+1
#    else:
#        status = status-1
#    if status < 1:
#        if (steps[i-1] == "D" and steps[i] == "U"):
#            valley = valley + 1

        
        
