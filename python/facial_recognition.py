import face_recognition

# identifying faces in the picture
def recognise_faces(known_image_location, unknown_image_location):
    known_image = face_recognition.load_image_file(known_image_location)
    unknown_image = face_recognition.load_image_file(unknown_image_location)

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    return results[0]

# res = recognise_faces('joe.jpg','obama.jpg')
# print(res[0])