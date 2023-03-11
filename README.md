# Clean Architecture - Python Demo

This repository demonstrates one way of implementing a Clean Architecture variant in Python.

## Structure

* Ports - Application public entry point
* Adapters - Application exit points that interface with other data sources
* App - Application Logic & Service
* Domain - Enterprise / Domain logic

### Patterns

To ensure the code adhere to the dependency rules, the `app` module defines an interface that is implemented by the relevant repository
in the `adapters` module. This way, the adapter can import and implement the interface that an application service expects to see.

This pattern was adapted from Golang.

## Implementation

To keep things simple, the code implements a very simple API that queries **ColorMind** for color schemes.

The `api` port exposes an HTTP API with 3 enpoints that correspond to 3 actions that can be performed against the ColorMind public API.

Each API call is forwarded via the service inside the `app` module to the repository inside the `adapters` module,
is responsible for making calls to the public ColorMind API.

Responses are sent back from the repository via the service to the port and to the user making the request.

The application is runnable as a uWSGI application: `uwsgi --http 127.0.0.1:8000 --master -w server:app` 