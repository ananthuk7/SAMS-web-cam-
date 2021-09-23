import cv2
import os


def handle_file(f,filename,folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    cv2.imwrite(folder+"/"+filename,f)
    print("stored")


def register_face(USER):
    print (USER)
    size = 40
    webcam = cv2.VideoCapture(0) #Use camera 0

    # We load the xml file
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #-----------------------------------------------
    i=1
    while (webcam.isOpened()):
        print("TRUEEEEEEEEE")
        (rval, im) = webcam.read()
        im=cv2.flip(im,1,0) #Flip to act as a mirror
        print("IMGGGGGGGGGGG",im)
        # Resize the image to speed up detection


        # width=int(im.shape[1]/size)
        # height=int(im.shape[0] /size)
        # dim=(width,height)
        # mini = cv2.resize(im,dim)
        # print("MINIIIIIII",mini)
        #
        # detect MultiScale / faces
        mini = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(mini, 1.1, 4)
        print("FACESSSSSSSSS",faces)
        # Draw rectangles around each face
        print("LENGTHHHH",len(faces))
        for (x, y, w, h) in faces:
            print ("face detected")
            #(x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
            cv2.rectangle(im, (x, y), (x + w, y + h),(0,255,0),thickness=4)
            #Save just the rectangle faces in SubRecFaces
            cv2.imshow('cp',im)
            sub_face = im[y:y+h, x:x+w]

            cv2.imshow('cp1', sub_face)
            FaceFileName = USER+"_"+str(i) + ".jpg"

            path="F:/ML/Tkprjct/SAMS_completed/DATABASE/"+USER
            handle_file(sub_face,FaceFileName,path)


            #cv2.imwrite(os.path.join(path, FaceFileName), sub_face)
            print("Saved")
            #cv2.imwrite(FaceFileName, sub_face)
            i+=1
            # Show the image
        cv2.imshow('User Registeration',   im)
        key = cv2.waitKey(10)
        # if Esc key is press then break out of the loop
        if key == 27 or i==100: #The Esc key
            print ("face recognized")
            break
    cv2.destroyAllWindows()
    webcam.release()
        
#-------------------------------------------------------------------------------

#register_face("helo")
