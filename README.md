### End to End Data Science project

## 📊 Experiment Tracking (MLflow + DagsHub)

This project uses **MLflow integrated with DagsHub** to track machine learning experiments, including model parameters, evaluation metrics, and artifacts.

### 🔹 Setup

MLflow is connected to DagsHub using the DagsHub Python SDK:

```python
import dagshub
dagshub.init(
    repo_owner="NishitaAgrawal-DS",
    repo_name="Machine-Learning",
    mlflow=True
)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)