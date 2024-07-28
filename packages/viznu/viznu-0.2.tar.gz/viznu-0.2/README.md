# Viznu

Viznu is a simple and intuitive library for data visualization and preprocessing for machine learning (ML) and deep learning (DL) applications.

## Installation

You can install Viznu via pip:

```sh
pip install viznu
```

## Usage 

Here's how you can use it: 

```py
from viznu import Viznu

viz = Viznu()
viz.load_train_data("path/to/train.csv")
viz.info_on('train')
viz.plot_distribution('Annual_Premium')
viz.col_info('Annual_Premium')
```