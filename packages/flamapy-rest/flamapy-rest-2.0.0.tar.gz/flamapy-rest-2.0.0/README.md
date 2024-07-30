<div align="center">

  <a href="">[![Pytest Testing Suite](https://github.com/flamapy/flamapy-rest/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/flamapy/flamapy-rest/actions/workflows/tests.yml)</a>
  <a href="">[![Commits Syntax Checker](https://github.com/flamapy/flamapy-rest/actions/workflows/commits.yml/badge.svg?branch=main)](https://github.com/flamapy/flamapy-rest/actions/workflows/commits.yml)</a>
  <a href="">![PyPI](https://img.shields.io/pypi/v/flamapy-rest?label=pypi%20package)
  <a href="">![PyPI - Downloads](https://img.shields.io/pypi/dm/flamapy-rest)
</div>

# 

<div id="top"></div>
<br />
<div align="center">

  <h3 align="center">FLAMAPY rest API</h3>

  <p align="center">
    A new and easy way to use FLAMA
    <br />
    <a href="https://github.com/flamapy/flamapy-fm-dist/issues">Report Bug</a>
    ·
    <a href="https://github.com/flamapy/flamapy-fm-dist/issues">Request Feature</a>
  </p>
</div>
<!-- ABOUT THE PROJECT -->

## About The Project

FLAMAPY Feature model distribution provides an easier way of using FLAMA when analysing feature models. It packs the most used plugins for analyis of feature models adding a layer of convenience to use the framework or integrate it. 

Feature Model Analysis has a crucial role in software product line engineering, enabling us to understand, design, and validate the complex relationships among features in a software product line. These feature models can often be complex and challenging to analyze due to their variability, making it difficult to identify conflicts, dead features, and potential optimizations. This is where this distribution comes in.

Please note: This is a living document and we will continue to update and improve it as we release new versions of the plugins and receive feedback from our users. If there's anything you don't understand or if you have any suggestions for improvement, don't hesitate to contact us. We're here to help!

Three main interfaces are provided:
* A REST API: The REST API allows for easy integration with other tools and applications. It is also a more user friendly interface for those who are not familiar with the command line.

Whant it to runint, simply run
```bash
pip install flamapy-rest
gunicorn --bind 0.0.0.0:8000 app:app
```

Alternatively, you can use docker in this way:
```bash
chmod +x start-server.sh
./start-server.sh
```
Or go to [the render deployed version]() it isn't fast, but its free. 

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Docker](https://www.docker.com/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [FLAMAPY](https://github.com/flamapy)
* [Flasgger](https://github.com/flasgger/flasgger)

<p align="right">(<a href="#top">back to top</a>)</p>

# Using the distribution REST API
The easies way is to execute the following command: docker run -p 8000:8000 flamapy/flamapy-fm-dist and open localhost:8000
<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

First, you will need to install [Docker](https://docs.docker.com/desktop/).

### Instalation

1. Clone the repository

2. If you are running Windows, run
  ```sh
  $ cd flamapy-dm-dist
  $ ./start-server.cmd
  ```
  
3. If you are running Linux or MacOS, run
  ```sh
  $ cd flamapy-dm-dist
  $ ./start-server.sh
  ```
  
This script will build, install and deploy the API in http://localhost:8000, you can access all the endpoints through an application like [Postman](https://www.postman.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

### API Documentation

All the documentation is registered with Swagger UI and OAS 3.0. It is accesible through /api/v1/docs. This documentation is generated dinamically by relyin gon flasgger. DO not forget to document your code in the route files!

<p align="right">(<a href="#top">back to top</a>)</p>
