import os
import cv2
import numpy as np
from PIL import Image

image_folder = '../img/'
video_name = 'video.avi'
height = 900
width = 1440

picFrames = []

def vinit(nums):
    id = 0
    trans = 0
    for n in nums:
        picFrames = [[trans, str(id)+'.jepg']] + picFrames
        trans += n
        id += 1
    return trans

def uni_size(im, w, h, fill_color=(255, 255, 255)):
    x, y = im.size
    size = ()
    if x/y >= w/h:
        size = (w, int(w*(y/x)))
    else:
        size = (int(h*(x/y)), h)
    im = im.resize(size, resample = 0)
    new_im = Image.new('RGB', (w, h), fill_color)
    new_im.paste(im, (int((w - size[0]) / 2), int((h - size[1]) / 2)), mask=None)
    return new_im

def vidgen(nums, audioLen):
    penult = vinit(nums)
    for item in picFrames:
        resized = uni_size(Image.open(item[1]), width, height)
        os.remove(item[1])
        resized.save(item[1], 'jpeg')

    FPS = 60 # Sets the FPS of the entire video
    currentFrame = 0 # The animation hasn't moved yet, so we're going to leave it as zero
    startFrame = 0
    trailingSeconds = audioLen - penult # Sets the amount of time we give our last image (in seconds)
    blendingDuration = 1.5
    blendingStart = 3 # Sets the time in which the image starts blending before songFile

    for i in picFrames:
        i[0] = i[0] * FPS # Makes it so that iterating frame-by-frame will result in properly timed slideshows

    im1 = Image.open(picFrames[-1][1]) # Load the image in
    im2 = im1 # Define a second image to force a global variable to be created

    current = picFrames[-1][1] # We're going to let the script know the location of the current image's location
    previous = current # And this is to force/declare a global variable
    fourcc = cv2.VideoWriter_fourcc(*'FMP4')
    video = cv2.VideoWriter("../vid/slideshow.mp4",fourcc,60,(width,height),True)

    while currentFrame < picFrames[0][0] + trailingSeconds*FPS:  # RHS defines the limit of the slideshow
        for i in picFrames:  # Loop through each image timing
            if currentFrame >= i[0] - (blendingStart * FPS):  # If the image timing happens to be for the
                # current image, the continue on...
                # (Notice how picFrames is reversed)
                print(str(currentFrame) + str(i[0] - (blendingStart * FPS)))

                if not current == i[1]:  # Check if the image file has changed
                    previous = current  # We'd want the transition to start if the file has changed
                    current = i[1]
                    startFrame = i[0] - (blendingStart * FPS)

                    # The two images in question for the blending is loaded in
                    im1 = Image.open(previous)
                    im2 = Image.open(current)
                break
        try:
            diff = Image.blend(im1, im2, min(1.0, (currentFrame - startFrame) / float(FPS) / blendingDuration))
        except:
            pass
        video.write(cv2.cvtColor(cv2.UMat(np.array(diff)), cv2.COLOR_RGB2BGR))
        currentFrame += 1  # Next frame

    # At this point, we'll assume that the slideshow has completed generating, and we want to close everything off to prevent a corrupted output.
    video.release()