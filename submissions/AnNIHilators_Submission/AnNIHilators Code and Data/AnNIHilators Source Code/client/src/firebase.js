import { firebase } from "@firebase/app";
import "@firebase/firestore";
import "@firebase/analytics";

const firebaseApp = firebase.initializeApp({
  apiKey: "AIzaSyA_KxcPxGehY5h5m8uqVktp_X06hqvlQjI",
  authDomain: "gsa-eula.firebaseapp.com",
  databaseURL: "https://gsa-eula.firebaseio.com",
  projectId: "gsa-eula",
  storageBucket: "gsa-eula.appspot.com",
  messagingSenderId: "1091609007867",
  appId: "1:1091609007867:web:73a68c6d44e5e948f2025e",
  measurementId: "G-2QKRJYXR32",
});

// firebaseApp.analytics();

export const db = firebaseApp.firestore();
