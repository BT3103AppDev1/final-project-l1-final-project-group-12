const { spawn } = require("child_process");

// Helper function to execute Python script and get output
const executePythonScript = (scriptPath, args) => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", [scriptPath, ...args]);
    let dataString = "";
    pythonProcess.stdout.on("data", (data) => {
      dataString += data.toString();
    });
    pythonProcess.stderr.on("data", (data) => {
      reject(data.toString());
    });
    pythonProcess.on("close", (code) => {
      resolve(dataString);
    });
  });
};
