import { initializeApp } from 'firebase/app';

const firebaseConfig = {
    apiKey: "AIzaSyD4jJ82I-l7CdIfSPeZGr_36jhRpba-CBc",
    authDomain: "democpp-e9e67.firebaseapp.com",
    projectId: "democpp-e9e67",
    storageBucket: "democpp-e9e67.appspot.com",
    messagingSenderId: "504403846956",
    appId: "1:504403846956:web:e87f28732ef47d3cae6e89"
    };

// Initialize Firebase
const firebaseApp = initializeApp(firebaseConfig);

export default firebaseApp;