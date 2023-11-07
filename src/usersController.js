// ALL functions in this file are related to User data, and has absolutely zero effect on the database.

import firebaseApp from "@/firebase.js"; // npm install firebase
import { getAuth } from "firebase/auth";

const auth = getAuth();

export { auth };
