# Use a base image that includes both Python and Node.js
FROM nikolaik/python-nodejs:python3.11-nodejs18

# Set the working directory to /app
WORKDIR /app

# Copy package.json (and package-lock.json if available) from the app folder to the /app directory
COPY package*.json ./
# Copy requirements.txt from the root to the /app directory
COPY requirements.txt ./
# Install Node.js dependencies
RUN npm install

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app folder contents to /app
COPY app/ .

# Expose the port the app runs on
EXPOSE 8080

# Set the command to start the server
CMD ["npm", "run", "server"]
