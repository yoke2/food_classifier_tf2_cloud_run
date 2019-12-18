# Food Classifier App with TensorFlow 2.0 model

This repo contains a web app for classifying 3 types of local Singaporean Food using the following APIs and platforms

- TensorFlow 2.0, using tf.image, tf.keras.models and tf.data (for training)
- Starlette

----------
## Docker Installation

You can test your changes locally by installing Docker and using the following command:

```
docker build -t food-tf2 . && docker run --rm -it -p 5000:5000 food-tf2
```

----------
## Local Installation

* Install dependencies
```
$ pip install -r requirements.txt
```

## Run app
```
$ python app/server.py serve
```

----------
## Reference

* Based on [Guide for production deployment to Render](https://course.fast.ai/deployment_render.html)
