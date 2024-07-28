# Maxplotlib

## Autovisualization API

Example:

```bash
maxplotlib "textbook-quality art with sine and cosine waves"
```

| ![Example Output Option 1](examples/example_output/option0.png) | ![Example Output Option 2](examples/example_output/option1.png) |
|:------------------------------------------:|:------------------------------------------:|
|               **Option 1**                  |               **Option 2**                  |
| ![Example Output Option 3](examples/example_output/option2.png) | ![Example Output Option 4](examples/example_output/option3.png) |
|               **Option 3**                  |               **Option 4**                  |


General:

```bash
maxplotlib prompt --output=optional_output_folder
```

### Setup

Make sure a **server** with a known IP address is on (see **Server** if you are doing this yourself).

```bash
pip install maxplotlib
export SERVER_IP=192.168....
```

### How does it work?

Llama 3.1 (implemented in [`mlx_lm`](https://github.com/ml-explore/mlx-examples/blob/main/llms/README.md)) generates [`matplotlib`](https://github.com/matplotlib/matplotlib) python scripts which are executed to produce images for the API response.

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
