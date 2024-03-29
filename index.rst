===================================================
Strelok
===================================================

.. image:: https://badge.fury.io/py/strelok.svg
    :target: https://badge.fury.io/py/strelok


.. image:: https://static.pepy.tech/badge/strelok
   :target: https://pepy.tech/project/strelok

.. image:: https://static.pepy.tech/badge/strelok/week
   :target: https://pepy.tech/project/strelok

.. image:: https://static.pepy.tech/badge/strelok/month
   :target: https://pepy.tech/project/strelok

Overview
========

The Strelok library is a powerful tool for automated feature engineering in machine learning projects. It provides a simple and intuitive way to generate new features, handle missing values, perform feature selection, and create interaction features. With Strelok, you can streamline your feature engineering process and improve the performance of your models.

Installation
============

To install Strelok, you can use `pip`:

.. code-block:: bash

   pip install strelok

Features
========

The Strelok library offers the following key features:

1. Mathematical Transformations: Generate new features by applying various mathematical transformations, such as logarithmic, exponential, square root, and more.

2. Missing Value Imputation: Fill missing values in your dataset using strategies like mean, median, mode, constant, forward fill, backward fill, interpolation, or KNN imputation.

3. Interaction Feature Generation: Create new features by combining existing features through operations like multiplication, addition, subtraction, and division.

4. Feature Selection: Select the most relevant features from your dataset using methods like univariate selection, recursive feature elimination (RFE), L1 regularization (Lasso), random forest importance, or correlation-based selection.

Method Details
==============

Before diving into examples of how to use the Strelok library, let's understand some of the core classes and their input parameters.

Pipeline
~~~~~~~~
This is the main class you'll interact with when using Strelok. It orchestrates the entire feature engineering process.

- `target_col` (string): The name of the column in your dataset which you want to target with Mathematical transformation or MissingValueImputation.

Methods:

- `add_feature(feature)`: Adds a feature object (e.g., an instance of `MathematicalTransformationFeature`, `MissingValueImputation`, or `InteractionFeature`) to the pipeline. The pipeline will process these features in the order they were added.

- `set_feature_selector(selector, not_X_col, y_col)`: Sets a feature selection method for the pipeline. Only one feature selection method can be active at a time. The `selector` should be an instance of `FeatureSelection`.
   - `feature_selector` (FeatureSelection): An instance of the FeatureSelection class representing the feature selection method.
   - `not_X_col` (list of strings, optional): A list of column names that should not be included as input features for feature selection. By default, it is an empty list. If y_col is provided, it is automatically appended to the not_X_col list to prevent the target column from being selected as the most relevant feature during feature selection. This ensures that the target column is excluded from the set of input features considered for selection.
   - `y_col` (list of strings): A list of column names representing the target variable. Default is an empty list.

- `generate_features(data)`: Applies all added features and the feature selector (if any) to the provided dataframe `data`, and returns a new dataframe with the engineered features. 



MathematicalTransformation
~~~~~~~~~~~~~~~~~~~~~~~~~~

This class performs mathematical transformations on a feature. 

- `name` (string): The name of the new feature. This name will be used to represent the transformed feature in the output dataframe.
- `transformation_type` (string): The type of mathematical transformation to apply. Supported values are:
    - 'logarithm': Applies the natural logarithm transformation. The input column should only contain positive numbers.
    - 'square_root': Applies the square root transformation. The input column should only contain non-negative numbers.
    - 'exponential': Applies the exponential transformation. Optional parameter 'power' (int or float) can be provided to specify the power of the transformation. Default is 1.
    - 'box_cox': Applies the Box-Cox transformation. The Box-Cox transformation requires the input column to contain positive values.
    - 'reciprocal': Applies the reciprocal transformation. The input column should contain non-zero values.
    - 'power': Applies the power transformation. Optional parameter 'power' (int or float) can be provided to specify the power of the transformation. Default is 2.
    - 'binning': Applies binning to the input column. Optional parameter 'num_bins' (int) can be provided to specify the number of bins. Default is 10.
    - 'standardization': Applies standardization to the input column. Optional parameters 'mean' (float) and 'std' (float) can be provided to specify the mean and standard deviation for standardization. By default, the mean and standard deviation are calculated from the input column.
    - 'rank': Computes the rank of the values in the input column.
    - 'difference': Computes the difference between the values in the input column and another feature specified by the 'other_feature' parameter.
    - 'relative_difference': Computes the relative difference between the values in the input column and a specified 'other_value'.

- `diff_col` (string, optional): The name of the existing column to be transformed, if not defined the column default to target_col in `Pipeline`
- `kwargs` (dictionary, optional): Additional parameters for specific transformation types.

In addition to the common inputs mentioned earlier, some mathematical transformations in the `MathematicalTransformation` class require additional parameters:

- 'exponential' transformation:

  - `power` (int or float, optional): The power of the exponential transformation. Default is 1.

- 'power' transformation:

  - `power` (int or float, optional): The power of the power transformation. Default is 2.

- 'binning' transformation:

  - `num_bins` (int, optional): The number of bins for binning. Default is 10.

- 'standardization' transformation:

  - `mean` (float, optional): The mean value for standardization. If not provided, the mean is calculated from the input column.
  - `std` (float, optional): The standard deviation for standardization. If not provided, the standard deviation is calculated from the input column.

- 'difference' transformation:

  - `other_feature` (string): The name of the other feature to compute the difference with.

- 'relative_difference' transformation:

  - `other_value` (float): The value to compute the relative difference with.

MissingValueImputation
~~~~~~~~~~~~~~~~~~~~~~

This class imputes missing values in a feature.

- `name` (string): The name of the new feature. This name will be used to represent the imputed feature in the output dataframe.
- `imputation_strategy` (string): The imputation strategy. Supported values are:
    - 'mean': Replaces missing values with the mean value of the non-missing values in the column. Suitable for numeric columns.
    - 'median': Replaces missing values with the median value of the non-missing values in the column. Suitable for numeric columns.
    - 'mode': Replaces missing values with the most frequent value in the column. Suitable for both numeric and categorical columns.
    - 'constant': Replaces missing values with a constant value (0).
    - 'forward_fill': Fills missing values with the previous non-missing value in the column (forward fill).
    - 'backward_fill': Fills missing values with the next non-missing value in the column (backward fill).
    - 'interpolation': Performs linear interpolation to fill missing values.
    - 'knn': Performs K-nearest neighbors imputation using the specified number of neighbors.
    - 'multiple': Performs multiple imputation using an iterative imputer.
    - 'missing_indicator': Creates a binary indicator column that flags missing values.

- `diff_col` (string, optional): The name of the existing column to be transformed. If not defined, the column defaults to the `target_col` in the `Pipeline`.

In addition to the common inputs mentioned earlier, some imputation strategies in the `MissingValueImputation` class require additional parameters:

- `knn` strategy:
    - `n_neighbors` (int): The number of nearest neighbors to consider when performing K-nearest neighbors imputation.

- `multiple` strategy:
    - No additional inputs are required. The `max_iter` and `random_state` parameters are set to default values.

InteractionFeature
~~~~~~~~~~~~~~~~~~
This class creates a new feature that is the interaction of two or more features.

- `name` (string): The name of the new feature. This name will be used to represent the interaction feature in the output dataframe.
- `interaction_type` (string): The type of interaction. Supported values are:
    - 'addition': Adds the values in the specified columns.
    - 'subtraction': Subtracts the values in the second column from the first. Only two columns are allowed in this case.
    - 'multiplication': Multiplies the values in the specified columns.
    - 'division': Divides the values in the first column by those in the second. Only two columns are allowed in this case, and the second column should not contain zero values.
- `columns` (list of strings): The names of the existing columns to be interacted. The list should contain at least two column names.

Feature Selection
~~~~~~~~~~~~~~~~~

This class selects top 'k' features based on a selection method.

- `method` (string): The feature selection method. Supported values are:
    - 'univariate': Selects features based on statistical tests.
    - 'rfe': Selects features using recursive feature elimination.
    - 'lasso': Selects features based on L1 regularization using Lasso.
    - 'random_forest': Selects features based on their importance in a trained random forest model.
    - 'pearson_correlation': Selects features based on Pearson correlation with the target.
    - 'spearman_correlation': Selects features based on Spearman correlation with the target.
    - 'box_cox': Selects features based on Box-Cox transformation.

- `k` (integer): The number of features to select.

In addition to the common inputs mentioned earlier, some feature selection methods in the `FeatureSelection` class require additional parameters:

- `correlation` methods (inlcudes `pearson` and `spearman`):
    - `correlation_threshold` (float): The threshold for selecting features based on their correlation with the target. Only features with a correlation above this threshold will be selected. Hence `k` is not required

- `box_cox` method:
    - `box_cox_threshold` (float): The threshold for selecting features based on their skewness using Box-Cox transformation. Only features with a skewness above this threshold will be selected.

Usage Examples
==============


Mathematical Transformations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pandas as pd
   from strelok import feat

   df = pd.DataFrame({'feature1': [1, 2, 3, 10], 'feature2': [2, 3, 4, 5], 'feature3': [1, 1, 1, 0], 'target': [0, 0, 0, 1]})
   pipeline = feat.Pipeline(target_col = 'feature1')

   log_feature = feat.MathematicalTransformation(name='logarithm_of_feature1', transformation_type='logarithm', diff_col='feature2') #diff_col not required, if left undefined target_col will be used

   pipeline.add_feature(log_feature)

   df_new = pipeline.generate_features(data=df)

Missing Value Imputation
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pandas as pd
   import numpy as np
   from strelok import feat

   df = pd.DataFrame({'feature1': [1, np.nan, 3, 10], 'feature2': [2, 3, 4, 5], 'feature3': [1, 1, 1, 0], 'target': [0, 0, 0, 1]})

   pipeline = feat.Pipeline(target_col = 'feature1')
   
   pipeline.add_feature(feat.MissingValueImputationFeature(name='feature1', imputation_strategy='mean'))

   df_new = pipeline.generate_features(data=df)

Interaction Feature Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pandas as pd
   from strelok import feat

   df = pd.DataFrame({'feature1': [1, 2, 3, 10], 'feature2': [2, 3, 4, 5], 'feature3': [1, 1, 1, 0], 'target': [0, 0, 0, 1]})
   pipeline = feat.Pipeline(target_col = 'feature1')
   
   pipeline.add_feature(feat.InteractionFeature(method = 'add', columns=['feature1', 'feature2']))

   pipeline.generate_features(data=df)

Feature Selection
~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pandas as pd
   from strelok import feat

   df = pd.DataFrame({'feature1': [1, 2, 3, 10], 'feature2': [2, 3, 4, 5], 'feature3': [1, 1, 1, 0], 'target': [0, 0, 0, 1]})
   pipeline = feat.Pipeline(target_col = 'feature1')
   
   pipeline.set_feature_selector(feat.FeatureSelection(method='univariate', k=2), not_X_col=[], y_col=['target'])

   pipeline.generate_features(data=df)

Complete example pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   
   import pandas as pd
   from strelok import feat

   df = pd.DataFrame({'feature1': [1, np.nan, 3, 4],
                     'feature2': [5, 6, 7, 8],
                     'target': [0, 1, 0, 1]})

   pipeline = feat.Pipeline(target_col='feature1')

   # Add features to the pipeline
   pipeline.add_feature(feat.MissingValueImputationFeature(name='feature1', imputation_strategy='mean'))
   pipeline.add_feature(feat.MathematicalTransformationFeature(name='squared', transformation_type='power', power=2))
   pipeline.add_feature(feat.InteractionFeature(method = 'add', columns=['feature1', 'feature2', 'squared']))
   pipeline.set_feature_selector(feat.FeatureSelection(method='univariate', k=3), not_X_col=[], y_col=['target'])



   # Generate features on the dataset
   processed_data = pipeline.generate_features(data=df)

   # Print the processed data
   print(processed_data)