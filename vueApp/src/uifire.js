import firebase from 'firebase/compat/app'
import 'firebase/compat/auth'

// ------------------------------ Firebase Config ------------------------------ //
// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCsdwvGXo3lwvM-TNOX_MuwFxAk97DfRQA",
  authDomain: "smartfolio-16224.firebaseapp.com",
  projectId: "smartfolio-16224",
  storageBucket: "smartfolio-16224.appspot.com",
  messagingSenderId: "281279681132",
  appId: "1:281279681132:web:0996924688f2e29d417e49",
  measurementId: "G-M1C9W3B0SG"
};

firebase.initializeApp(firebaseConfig)

export default firebase