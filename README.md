# Food Classifier App with [TensorFlow 2](https://www.tensorflow.org/) model on [Google Cloud Run](https://cloud.google.com/run/)

This repo contains a web app for classifying 3 types of local Singaporean Food using the following APIs and platforms

- TensorFlow 2: using tf.image, tf.keras.models and tf.data (for training)
- Google Cloud Platform: Cloud Run, Cloud Build, Cloud Storage
- Starlette, a lightweight ASGI framework/toolkit

----------
## Deploy with Google Cloud Run

### Pre-requisites
- Google Cloud Account
- Enable Cloud Run and Cloud Build API

### Deploy
To run the webapp on Google Cloud Run, launch Cloud Shell from your Dashboard.

- export PROJECT_ID={your project id here}
- Run `gcloud config set project $PROJECT_ID`
- Run `git clone https://github.com/yoke2/food_classifier_tf2_cloud_run.git`
- Change directory: `cd food_classififer_tf2_cloud_run`
- Build container image with [Google Cloud Build](https://cloud.google.com/cloud-build/) by running `gcloud builds submit --tag gcr.io/$PROJECT_ID/food_classifier`
    - If prompted that Cloud Build API not enabled on the project, enter 'y' to enable and retry
- Deploy container built: `gcloud run deploy --image gcr.io/$PROJECT_ID/food_classifier --platform managed --allow-unauthenticated --memory 1024M`
    - You will be prompted for the service name: press Enter to accept the default name
    - You will be prompted for region: select the region us-central1
- You will receive an URL to access the app. This can be seen on the Cloud Run page for `dimsumapp` in the Dashboard as well

----------
## Docker Installation

You can test your changes locally by installing Docker and using the following command:

```
docker build -t food-tf2-cr . && docker run --rm -it -p 8080:8080 food-tf2-cr
```

----------
## Local Installation

* Install dependencies
```
$ pip install packaging
$ pip install -r requirements.txt
```

## Run app
```
$ python app/server.py serve
```

----------
## Reference

* Based on [fast.ai's guide for production deployment to Render](https://course.fast.ai/deployment_render.html)
* [Google Cloud Run Docs](https://cloud.google.com/run/docs/)
* [Repository for supplementary package containing supporting functions](https://github.com/yoke2/suptools)
