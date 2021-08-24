# !pip install pandas

from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

# +
from azureml.core import Workspace, Dataset

subscription_id = '5a4ab2ba-6c51-4805-8155-58759ad589d8'
resource_group = 'aml-quickstarts-155546'
workspace_name = 'quick-starts-ws-155546'

ws = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(ws, name='HeartFailure_Dataset')
dataset = dataset.to_pandas_dataframe()
# -

# TODO: Split data into train and test sets.

# ## YOUR CODE HERE ###a

run = Run.get_context()

x = dataset
y = x.pop("DEATH_EVENT")

# +
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=223)


# +
def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")


    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/model.joblib')

if __name__ == '__main__':
    main()
quit
# -





