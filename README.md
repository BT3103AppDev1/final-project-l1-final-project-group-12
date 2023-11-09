[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/WcPKYd5y)

## 📌 Prerequisites

1. Node.js (v18.16.0)
2. Python (v3.11)
3. Pip (v22.3.1)

## 🚀 Installing Dependencies and Configuration

Clone Smartfolio's source code to your local machine

```
git clone https://github.com/BT3103AppDev1/final-project-l1-final-project-group-12.git
```

For Windows users, run the following commands in Powershell from Root:

```
npm install; if ($?) { pip install -r requirements.txt }
```

In command prompt:

```
npm install && pip install -r requirements.txt
```

## 🖥️ Starting development

Starting the server-side for development and APIs query

```
npm run server
```

Starting the client-side for development

```
npm run dev
```

## Production

Both the backend and frontend server has to be deployed for the app to work as expected. Presently, the client is being served by https://smartfolio-7gt75z5x3q-as.a.run.app.

### 1. Server Deployment

Due to complexities of deployment of a mixed language architecture, the backend is containerized and deployed on Google Cloud Run. An extensive user guide on Docker and GCR deployment can be found here
https://docs.docker.com/get-started/02_our_app/

To deploy on GCR via Docker images

```
gcloud run deploy your-service-name --image gcr.io/your-project-id/your-image-name:your-tag --platform managed
```

### 2. Client Deployment

```
npm run build
firebase deploy
```
