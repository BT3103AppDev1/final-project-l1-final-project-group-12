import firebaseApp from '@/firebase.js'; // npm install firebase
import { getFirestore } from "firebase/firestore"
import { doc, collection, setDoc,  getDocs, getDoc, deleteDoc, updateDoc } from "firebase/firestore"
import { getAuth } from 'firebase/auth';

const db = getFirestore(firebaseApp);
const auth = getAuth();
const collectionName = "EquityPortfolio";

async function extractData() {
    try {
        const querySnapshot = await getDocs(collection(db, collectionName), { source: 'server' });
        const data = querySnapshot.docs.map(doc => doc.data());
        return data;

    } catch (error) {
        console.error("Error extracting data:", error);
        throw error;
    }
}

async function addInstrument(stock) {
    try {
        // Check if the stock exists in the database
        const stockDocRef = doc(db, collectionName, stock.Stock);
        const stockDocSnapshot = await getDoc(stockDocRef);

        if (stockDocSnapshot.exists()) {
            // Stock exists, update the quantity and price
            const existingData = stockDocSnapshot.data();
            const updatedQuantity = parseFloat(existingData.Buy_Quantity) + parseFloat(stock.Buy_Quantity);
            const updatedPrice = (existingData.Buy_Price * existingData.Buy_Quantity + stock.Buy_Price * stock.Buy_Quantity) / updatedQuantity; // Calculate the new average price

            // Update the document with the new data
            await setDoc(stockDocRef, {
                Stock: stock.Stock,
                Code: stock.Stock,                  // TO BE EDITED: Show Ticker 
                Buy_Price: updatedPrice,
                Buy_Quantity: updatedQuantity
            });
        } else {
            // Stock doesn't exist, add a new document
            await setDoc(doc(db, collectionName, stock.Stock), stock);
        }
        
        alert("Saving your data for coin : " + stock.Stock);        //TODO: Show Popup window
    
    } catch (error) {
        console.error("Error adding document: ", error);        //TODO: Show Popup window
        throw error;
    }
}


async function deleteInstrument(stock) {
    try {
        await deleteDoc(doc(db, collectionName, stock));
        alert("Document successfully deleted!" + stock);
        
    } catch (error) {
        console.error("Error deleting document:", error);
        throw error;
    }
}

async function editInstrument(stock, updatedData) {
    if (!isNaN(parseFloat(updatedData.Buy_Price)) && !isNaN(parseFloat(updatedData.Buy_Quantity)) && updatedData.Buy_Price > 0 && updatedData.Buy_Quantity > 0) {
        try {
            const docRef = doc(db, collectionName, stock);
            await updateDoc(docRef, updatedData);
            alert("Document successfully updated!");

        } catch (error) {
            alert("Error updating document:" + error);
            throw error;
        }

    } else {
        alert ("Please enter valid positive numbers.")
    }
}


export { extractData, deleteInstrument, editInstrument, addInstrument, auth };
