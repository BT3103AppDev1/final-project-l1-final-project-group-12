const functions = require("firebase-functions");
const app = require("./app/api/server");

exports.app = functions.https.onRequest(app);
