# Run

Navigate to the root of the project and create the Whisper image:
```shell
docker build -t whisper .
```

Run the container with a volume where your videos are located:

```shell
docker run -it -v /path/to/your/videos:/path/in/the/container image_name
```


Replace `/path/to/your/video`s with the path to your videos on your local machine, and `/path/in/the/container` with the path where you want these videos to be accessible inside the container. Also, replace image_name with the name of the Docker image you created.
