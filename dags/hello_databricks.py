# from databricks.connect import DatabricksSession
from databricks.sdk import WorkspaceClient

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator


w = WorkspaceClient()

print("hello databricks")