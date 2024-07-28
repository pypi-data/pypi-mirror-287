# viznu/core.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Viznu:
    def __init__(self):
        self.train_data = None
        self.test_data = None
        self.validation_data = None
        self.curr_dataset = "train"

    def load_train_data(self, path: str):
        self.train_data = pd.read_csv(path)
        print(f"Training data loaded from {path}")

    def load_test_data(self, path: str):
        self.test_data = pd.read_csv(path)
        print(f"Test data loaded from {path}")

    def load_validation_data(self, path: str):
        self.validation_data = pd.read_csv(path)
        print(f"Validation data loaded from {path}")

    def info_on(self, data_type: str = 'all'):
        if data_type == 'train' or data_type == 'all': 
            self._print_info('Train', self.train_data)
        
        if data_type == 'test' or data_type == 'all':
            self._print_info('Test', self.test_data)

        if data_type == 'validation' or data_type == 'all':
            self._print_info('Validation', self.validation_data)

        if data_type not in ['train', 'test', 'validation', 'all']:
            print("Invalid data type. Choose from 'train', 'test', 'validation', or 'all'.")

    def _print_info(self, name: str, df: pd.DataFrame):
        if df is not None:
            print(f"\n{name} Data Info:")
            print(f"Shape: {df.shape}")
            print("\nHead:")
            print(df.head())
            print("\nInfo:")
            df.info()
        else:
            print(f"\n{name} data not loaded.")

    def plot_distribution(self, column: str, kind: str = 'box'):
        if self.curr_dataset == 'train':
            df = self.train_data
        elif self.curr_dataset == 'test':
            df = self.test_data
        elif self.curr_dataset == 'validation':
            df = self.validation_data
        else:
            print("Invalid data type. Choose from 'train', 'test', or 'validation'.")
            return

        if df is not None and column in df.columns:
            plt.figure(figsize=(7, 4))
            if kind == 'box':
                sns.boxplot(x=df[column])
            elif kind == 'hist':
                sns.histplot(df[column], kde=True)
            else:
                print(f"Invalid plot kind: {kind}. Supported kinds: 'box', 'hist'.")
                return

            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.show()
        else:
            print(f"Column {column} not found in the dataset or dataset is not loaded.")

    def col_info(self, col: str):
        if self.curr_dataset == 'train':
            df = self.train_data
        elif self.curr_dataset == 'test':
            df = self.test_data
        elif self.curr_dataset == 'validation':
            df = self.validation_data
        else:
            print("Invalid data type. Choose from 'train', 'test', or 'validation'.")
            return

        if df is not None and col in df.columns:
            print(f"\nColumn '{col}' Info:")
            print(f"Unique values: {df[col].nunique()}")
            print(f"Missing values: {df[col].isnull().sum()}")
            print(f"\nBasic Statistics:")
            if pd.api.types.is_numeric_dtype(df[col]):
                print(df[col].describe())
            else:
                print(df[col].value_counts())

            plt.figure(figsize=(10, 6))
            if pd.api.types.is_numeric_dtype(df[col]):
                sns.histplot(df[col], kde=True)
            else:
                sns.countplot(y=df[col], order=df[col].value_counts().index)
            plt.title(f'Distribution of {col}')
            plt.xlabel(col)
            plt.ylabel('Frequency')
            plt.show()
        else:
            print(f"Column {col} not found in the dataset or dataset is not loaded.")