from firebase import Firebase


firebaseConfig = {
  "apiKey": "AIzaSyAnBNGgcqUBFhHV-J1rs3z8ZIuxR8PXcz4",
  "authDomain": "tobacco-booking-project.firebaseapp.com",
  "databaseURL": "https://tobacco-booking-project-default-rtdb.firebaseio.com",
  "projectId": "tobacco-booking-project",
  "storageBucket": "tobacco-booking-project.appspot.com",
  "messagingSenderId": "1052763825914",
  "appId": "1:1052763825914:web:502056c5a5a0acf0fb8b43",
  "measurementId": "G-FKVD3MKBSL"
}


firebase = Firebase(firebaseConfig)
database = firebase.database()
storage = firebase.storage()
