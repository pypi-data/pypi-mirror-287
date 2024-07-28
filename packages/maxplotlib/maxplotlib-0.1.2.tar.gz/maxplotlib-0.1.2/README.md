# Maxplotlib

## 1. Autovisualization API

`text` -> `charts and graphs` autovisualization API

Example:

```bash
plot "five circles like the olympics logo"
```

General:

```bash
plot description --output=folder
```

### Setup

Make sure a **server** with a known IP address is on (see **Server** if you are doing this yourself).

```bash
pip install maxplotlib
export SERVER_IP=192.168....
```

### How does it work?

Prompts Llama 3.1 (implemented in [`mlx_lm`](https://github.com/ml-explore/mlx-examples/blob/main/llms/README.md)) to generate [`matplotlib`](https://github.com/matplotlib/matplotlib) python scripts. Executes those scripts, capturing the generated images in the process, and sends the images with metadata in the API response. 

### Server

Turning on a **server** allows other people to use your machine as a compute engine for `maxplotlib` API calls.

To turn on a **server**, install the requirements:

```bash
pip install 'maxplotlib[server]'
```

Then, navigate to the `server` directory and run the launch script:

```bash
cd src/server
./run_server
```
Once the **server** is on, remote `maxplotlib` API calls to your IP address will run on your machine.

## 2. Visualization functions

Python functions to produce visualizations for geospatial data, machine learning, & graph theory.