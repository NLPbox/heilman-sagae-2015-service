# heilman-sagae-2015-service

[![Travis Build Status](https://travis-ci.org/NLPbox/heilman-sagae-2015-service.svg?branch=master)](https://travis-ci.org/NLPbox/heilman-sagae-2015-service)  
[![Docker Build Status](https://img.shields.io/docker/build/nlpbox/heilman-sagae-2015-service.svg)](https://hub.docker.com/r/nlpbox/heilman-sagae-2015-service/)  

This docker container allows you to build, install and run the
[ Heilman and Sagae (2015) RST discourse parser](https://github.com/EducationalTestingService/discourse-parsing)
in a docker container with an added REST API.

## build

docker build -t heilman-sagae-service .

## run

docker run -p 8000:8000 -ti heilman-sagae-service

## Usage Examples

### CURL

```
$ cat test.txt 
Altough they didn't like him, they accepted the offer.

$ curl -X POST -F "input=@test.txt" http://localhost:8000/parse -F output_format=original
{"scored_rst_trees": [{"score": -1.8205391822426933, "tree": "(ROOT (nucleus:span (text 0)) (satellite:attribution (text 1)))"}], "edu_tokens": [["Altough", "they", "did", "n't", "like", "him", ","], ["they", "accepted", "the", "offer", "."]]}
```

### Javascript

```
>>> var xhr = new XMLHttpRequest();

>>> xhr.open("POST", "http://localhost:8000/parse")

>>> var data = new FormData();
>>> data.append('input', 'Altough they didn\'t like him, they accepted the offer.');
>>> data.append('output_format', 'original');

>>> xhr.send(data);
>>> console.log(xhr.response); // wait before calling
{"edu_tokens": [["Altough", "they", "did", "n't", "like", "him", ","], ["they", "accepted", "the", "offer", "."]], "scored_rst_trees": [{"score": -1.8205391822426933, "tree": "(ROOT (nucleus:span (text 0)) (satellite:attribution (text 1)))"}]}
```
