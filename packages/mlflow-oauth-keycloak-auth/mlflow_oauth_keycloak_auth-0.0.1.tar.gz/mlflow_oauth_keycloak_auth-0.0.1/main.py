import mlflow
import src.mlflow_oauth_keycloak_auth.authentication as mlflow_auth
from time import sleep

mlflow_auth.init()
mlflow_auth.authenticate()

mlflow.set_tracking_uri("https://mlflow.mlops.smiwit.de")
exp = mlflow.get_experiment_by_name("Default")
print(exp)
mlflow_auth.validate_or_refresh()
