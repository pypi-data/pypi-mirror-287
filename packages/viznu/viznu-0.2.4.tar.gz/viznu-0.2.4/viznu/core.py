import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Viznu:
    def __init__(self):
        self.dataset_types = ["train", "test", "val"]
        self.train_data = None
        self.test_data = None
        self.validation_data = None
        self.curr_dataset = "train"
    
    def setCurrentDatasetTo(self, type: str): 
        if type not in self.dataset_types:
            print("Tried to set INVALID dataset type. Check type input into method.")
        else: 
            self.curr_dataset = type

    # LOAD DATA METHODS START HERE
    def loadTrainData(self, path: str):
        self.train_data = pd.read_csv(path)
        print(f"Training data loaded from {path}")

    def loadTestData(self, path: str):
        self.test_data = pd.read_csv(path)
        print(f"Test data loaded from {path}")

    def loadValidationData(self, path: str):
        self.validation_data = pd.read_csv(path)
        print(f"Validation data loaded from {path}")

    def loadAll(self, directory: str = '.'):
        """
        Load train, test, and validation data files from the specified directory.
        Assumes files are named as train.csv, test.csv, and validation.csv.
        """
        train_path = os.path.join(directory, 'train.csv')
        test_path = os.path.join(directory, 'test.csv')
        validation_path = os.path.join(directory, 'validation.csv')

        if os.path.exists(train_path):
            self.loadTrainData(train_path)
        else:
            print(f"No training data found at {train_path}")

        if os.path.exists(test_path):
            self.loadTestData(test_path)
        else:
            print(f"No test data found at {test_path}")

        if os.path.exists(validation_path):
            self.loadValidationData(validation_path)
        else:
            print(f"No validation data found at {validation_path}")

    # INFO PRINTING METHODS START HERE. 
    def info(self):
        """
        Prints high-level information about the loaded datasets.
        """
        print("Datasets loaded:")
        if self.train_data is not None:
            print("- Train dataset loaded. Sample from train data:")
            print(self.train_data.head())
            print("Shape of train table: ", self.train_data.shape)
        else:
            print("- Train dataset not loaded")

        if self.test_data is not None:
            print("- Test dataset loaded. Sample from test data:")
            print(self.test_data.head())
            print("Shape of test table: ", self.test_data.shape)
        else:
            print("- Test dataset not loaded")

        if self.validation_data is not None:
            print("- Validation dataset loaded. Sample from validation data:")
            print(self.validation_data.head())
            print("Shape of validation table: ", self.validation_data.shape)
        else:
            print("- Validation dataset not loaded")

    def infoFor(self, data_type: str):
        if data_type == 'train' or data_type == 'all':
            self._printShapeHeadAndInfo('Train', self.train_data)
        
        if data_type == 'test' or data_type == 'all':
            self._printShapeHeadAndInfo('Test', self.test_data)

        if data_type == 'validation' or data_type == 'all':
            self._printShapeHeadAndInfo('Validation', self.validation_data)

        if data_type not in ['train', 'test', 'validation', 'all']:
            print("Invalid data type. Choose from 'train', 'test', 'validation', or 'all'.")

    def _printShapeHeadAndInfo(self, name: str, df: pd.DataFrame):
        if df is not None:
            print(f"\n{name} Data Info:")
            print(f"Shape: {df.shape}")
            print("\nHead:")
            print(df.head())
            print("\nInfo:")
            df.info()
        else:
            print(f"\n{name} data not loaded.")

    def colInfo(self, col: str):
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

# Example usage:
# viz = Viznu()
# viz.load_all("./datasets")
# viz.info_on('train')
# viz.plot_distribution('Annual_Premium')
# viz.col_info('Annual_Premium')