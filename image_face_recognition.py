import cv2
import face_recognition


def facerecognition():
    #loading the image to detect
    original_image = cv2.imread('images/testing/trump-modi-unknown.jpg')


    modi_image = face_recognition.load_image_file('images/samples/modi.jpg')
    modi_face_encodings = face_recognition.face_encodings(modi_image)[0]

    trump_image = face_recognition.load_image_file('images/samples/trump.jpg')
    trump_face_encodings = face_recognition.face_encodings(trump_image)[0]

    #Save the encodings and the corresponding labels in seperate arrays in the same order
    known_face_encodings = [modi_face_encodings,trump_face_encodings]
    known_face_names = ["Narendra Modi","Donald Trump"]

    #load the unknown image to recognize faces in it
    image_to_recognize = face_recognition.load_image_file('images/testing/trump-modi-unknown.jpg')

    
    all_face_locations = face_recognition.face_locations(image_to_recognize,model='hog')

    
    all_face_encodings = face_recognition.face_encodings(image_to_recognize,all_face_locations)

    
    print('There are {} no of faces in this image'.format(len(all_face_locations)))

    
    for current_face_location,current_face_encodings in zip(all_face_locations,all_face_encodings):
        
        top_pos,right_pos,bottom_pos,left_pos = current_face_location


       
        all_matches = face_recognition.compare_faces(known_face_encodings,current_face_encodings)

        
        name_of_person = 'Unknown Face'

        #check if the all matches have at lleast on item
        #if yes, get the index number of face that is located in the first index of all_maches
        if True in all_matches:
            first_match_index = all_matches.index(True)
            name_of_person = known_face_names[first_match_index]

        
        cv2.rectangle(original_image,(left_pos,top_pos),(right_pos,bottom_pos),(0,255,0),2)

        

        
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(original_image,name_of_person,(left_pos,bottom_pos), font, 0.5,(0,0,0),3)
        cv2.putText(original_image,name_of_person,(left_pos,bottom_pos), font, 0.5,(255,255,255),1)

        

    
    cv2.imshow("Faces identified (Press q to quit)",original_image)

    cv2.waitKey(0)


    cv2.destroyAllWindows()


facerecognition()