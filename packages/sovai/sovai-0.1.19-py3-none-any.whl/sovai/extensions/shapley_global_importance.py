import pandas as pd
import numpy as np
import random
from xgboost import XGBClassifier
from sklearn.cluster import KMeans
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.preprocessing import StandardScaler
import shap
from joblib import Parallel, delayed

import hashlib
from sklearn.cluster import OPTICS, KMeans
from sklearn.cluster import MeanShift


def hash_of_df(df, sample_size=100):
    # Sample the DataFrame and convert to a byte string
    df_sample = (
        df.sample(n=min(sample_size, len(df)), random_state=42).to_string().encode()
    )

    # Compute and return the hash
    return hashlib.sha256(df_sample).hexdigest()


## speed, kmeans, meanshift, hdbscan
class ClusteringExplainer:
    def __init__(self, random_state=42):
        self.random_state = random_state
        self.model = None
        self.shap_values = None

    def fit(self, X, y):
        classes_weights = compute_sample_weight(class_weight="balanced", y=y)
        self.model = XGBClassifier(
            objective="multi:softprob", random_state=self.random_state
        )
        self.model.fit(X, y, sample_weight=classes_weights)

        explainer = shap.Explainer(self.model)
        self.shap_values = explainer(X)

    def get_shap_values_df(self, X):
        mean_shap_values = np.abs(self.shap_values.values).mean(axis=2)
        shap_values_df = pd.DataFrame(mean_shap_values, columns=X.columns)
        return shap_values_df


from sklearn.cluster import HDBSCAN


def simulation_task(df, i, clustering_method, kmeans_random_state, xgb_random_state):
    # Limit rows to a maximum of 5000
    X = df.sample(frac=1, random_state=i).reset_index(drop=True)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Clustering
    if clustering_method == "KMEANS":
        num_clusters = random.randint(
            5, 10
        )  # Assuming you want to randomize number of clusters for KMeans
        clustering = KMeans(n_clusters=num_clusters, random_state=kmeans_random_state)
    elif clustering_method == "MEANSHIFT":
        clustering = MeanShift()
    elif clustering_method == "HDBSCAN":
        clustering = HDBSCAN(min_cluster_size=5)  # Hardcoded to a minimum of 5 clusters
    else:
        raise ValueError("Unsupported clustering method: {}".format(clustering_method))

    clustering.fit(X_scaled)
    y = clustering.labels_

    # Handling noise points for HDBSCAN
    if clustering_method == "HDBSCAN":
        # Assign noise points to a new label (largest label number + 1)
        noise_label = max(y) + 1
        y[y == -1] = noise_label

    # SHAP value calculation
    clust_explnr = ClusteringExplainer(random_state=xgb_random_state)
    clust_explnr.fit(X_scaled, y)
    return clust_explnr.get_shap_values_df(X)


def run_simulations(df, num_simulations=4, clustering_method="KMEANS"):
    # Generate a hash of the DataFrame
    data_hash = hash_of_df(df)

    # Prepare tasks for parallel execution
    tasks = []
    for i in range(num_simulations):
        # Derive random states from the hash and iteration number
        random.seed(int(data_hash, 16) + i)
        kmeans_random_state = random.randint(0, 1000)
        xgb_random_state = random.randint(0, 1000)

        tasks.append(
            delayed(simulation_task)(
                df, i, clustering_method, kmeans_random_state, xgb_random_state
            )
        )

    # Run simulations in parallel
    all_shap_values = Parallel(n_jobs=-1)(tasks)

    # Average SHAP values across all simulations
    avg_shap_values = pd.concat(all_shap_values).groupby(level=0).mean()
    avg_shap_values.index = df.index
    return avg_shap_values
