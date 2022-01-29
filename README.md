# SONOS Web controller

Minimal web controller for the smart speaker by sonos. The interface allows to start, stop and skip the current tracks. Moreover the volume can be changed. Furthermore predefined radio stations can be played. 


## Installation
- Download/Clone Repo
- build image 
  ```bash
  docker build --pull --rm -f "DOCKERFILE" -t sonoswebcontroller:latest "."
  ```
- run 
  ```bash
  docker run --rm -d  -p 80:80/tcp sonoswebcontroller:latest
  ```
- Visit the website at IP of the host and enjoy 


## Modify radio stations
- Edit `radio_stations.json`
- Each station needs a unique name and the URL to the stream. 
- Optional: add a cover in the static folder and the file name to the `radio_stations.json`

