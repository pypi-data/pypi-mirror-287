# Viznu

Viznu is a simple and intuitive library for data visualization and preprocessing for machine learning (ML) and deep learning (DL) applications. It abstracts away the complexity of handling dataframes and generating visualizations, allowing you to quickly gain insights from your data with minimal code.

## Features

- Load train, test, and validation datasets easily.
- Display high-level information about loaded datasets.
- Generate various types of visualizations for data exploration.
- Print detailed information and distribution plots for specific columns.

## Installation

You can install Viznu using pip:

```sh
pip install viznu
```

## Usage

Here’s an example of how to use Viznu:

```python
from viznu import Viznu

# Create an instance of Viznu
viz = Viznu()

# Load all datasets from the specified directory
viz.loadAll("./datasets")

# Print high-level information about all loaded datasets
viz.info()

# Print detailed information about the training dataset
viz.infoFor('train')

# Set the current dataset to 'train'
viz.setCurrentDatasetTo('train')

# Plot the distribution of a specific column
viz.plot_distribution('Annual_Premium')

# Print detailed information and plot the distribution of a specific column
viz.colInfo('Annual_Premium')
```

## Methods

### Data Loading

- **loadTrainData(path: str)**: Load training data from the specified CSV file.
- **loadTestData(path: str)**: Load test data from the specified CSV file.
- **loadValidationData(path: str)**: Load validation data from the specified CSV file.
- **loadAll(directory: str = '.')**: Load train, test, and validation data files from the specified directory. Assumes files are named as `train.csv`, `test.csv`, and `validation.csv`.

### Information Display

- **info()**: Print high-level information about the loaded datasets.
- **infoFor(data_type: str)**: Print detailed information about the specified dataset (`train`, `test`, `validation`, or `all`).

### Visualization

- **plot_distribution(column: str, kind: str = 'box')**: Plot the distribution of the specified column. Supported plot types are `box` and `hist`.
- **colInfo(col: str)**: Print detailed information and plot the distribution of the specified column in the current dataset.

### Dataset Management

- **setCurrentDatasetTo(type: str)**: Set the current dataset to the specified type (`train`, `test`, or `val`).

## Examples

### Loading Datasets

```python
viz.loadTrainData("path/to/train.csv")
viz.loadTestData("path/to/test.csv")
viz.loadValidationData("path/to/validation.csv")
```

### Displaying Information

```python
viz.info()
viz.infoFor('train')
```

### Visualizing Data

```python
viz.plot_distribution('Annual_Premium', kind='hist')
viz.colInfo('Annual_Premium')
```

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue on GitHub.

## Author

Apekshik Panigrahi - [apekshik@gmail.com](apekshik@gmail.com)

## Acknowledgments

Inspired by the need to simplify data visualization and preprocessing in ML and DL workflows.