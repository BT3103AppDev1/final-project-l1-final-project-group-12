import firebaseApp from '@/firebase.js'; // npm install firebase
import { getFirestore } from "firebase/firestore"
import { doc, collection, setDoc,  getDocs, getDoc, deleteDoc, updateDoc } from "firebase/firestore";

const db = getFirestore(firebaseApp);

async function getStockDocRef(collectionName, userEmail, stock) {
    const userDocRef = doc(db, collectionName, `${userEmail}_${collectionName}` );
    const stocksCollectionRef = collection(userDocRef, 'stocks');
    const stockDocRef = doc(stocksCollectionRef, stock.Stock);
    return stockDocRef;
}

async function extractData(collectionName, userEmail) {
    try {
        const userDocRef = doc(db, collectionName, `${userEmail}_${collectionName}`);
        const querySnapshot = await getDocs(collection(userDocRef, 'stocks'));
        const data = querySnapshot.docs.map(doc => doc.data());
        return data;

    } catch (error) {
        console.error("Error extracting data:", error);
        throw error;
    }
}

async function addInstrument(collectionName, userEmail, stock) {
    try {
        const stockDocRef = await getStockDocRef(collectionName, userEmail, stock);
        const individualStockSnapshot = await getDoc(stockDocRef);
       
        if (individualStockSnapshot.exists()) {
            // Stock exists, update the quantity and price
            const existingData = individualStockSnapshot.data();
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
            await setDoc(stockDocRef, stock);
        }
        
        alert("Saving your data for coin : " + stock.Stock);        //TODO: Show Popup window
    
    } catch (error) {
        console.error("Error adding document: ", error);        //TODO: Show Popup window
        throw error;
    }
}


async function deleteInstrument(collectionName, userEmail, stock) {
    try {
        const stockDocRef = await getStockDocRef(collectionName, userEmail, stock);
        console.log("Stock Doc Ref:", stockDocRef); // Log the stockDocRef
        await deleteDoc(stockDocRef);
        alert("Document successfully deleted " + stock.Stock);
        
    } catch (error) {
        console.error("Error deleting document:", error);
        throw error;
    }
}

async function editInstrument(collectionName, userEmail, stock, updatedData) {
    if (!isNaN(parseFloat(updatedData.Buy_Price)) && 
        !isNaN(parseFloat(updatedData.Buy_Quantity)) && 
        updatedData.Buy_Price > 0 && 
        updatedData.Buy_Quantity > 0) {

        try {
            const userDocRef = doc(db, collectionName, `${userEmail}_${collectionName}`);
            const stocksCollectionRef = collection(userDocRef, 'stocks');
            const docRef = doc(stocksCollectionRef, stock.Stock);

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


export { extractData, deleteInstrument, editInstrument, addInstrument };
