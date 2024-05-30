
import os
import pickle
import click
import mlflow

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from hyperopt import STATUS_OK


mlflow.set_tracking_uri(uri="sqlite:///mlflow.db")
mlflow.set_experiment("green-taxi-experiment")

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):
     mlflow.autolog()
     with mlflow.start_run():
        mlflow.set_tag("developer", "linda")
        mlflow.set_tag("model", "randomforestregressor")
        X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
        X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))
        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)

        rmse = mean_squared_error(y_val, y_pred, squared=False)
        mlflow.log_metric("rmse",rmse)
     return {'loss':rmse, 'status':STATUS_OK}


if __name__ == '__main__':
    run_train()
