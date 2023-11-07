import firebaseApp from "@/firebase.js"; // npm install firebase
import { getAuth } from "firebase/auth";

const auth = getAuth();

export { auth };
