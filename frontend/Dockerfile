# Use a Node.js base image for building and serving the app
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package.json ./

# Install all dependencies, including devDependencies
RUN npm install

# Copy the rest of the frontend files
COPY . .

# Build the Svelte app
RUN npm run build

# Expose port 8080
EXPOSE 8080

# Start the app using sirv
CMD ["npx", "sirv", "public", "--host", "0.0.0.0", "--port", "8080"]
