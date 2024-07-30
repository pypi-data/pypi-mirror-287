import pandas as pd
import numpy as np
from sklearn.decomposition import PCA, TruncatedSVD, FactorAnalysis
from sklearn.random_projection import GaussianRandomProjection
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
# import umap
import warnings


def preprocess_panel_data(df, verbose=False):
    """Preprocess the panel data."""
    try:
        if verbose:
            print("Initial shape:", df.shape)

        df_ffilled = df.groupby(level="ticker").ffill()
        df_filled = df_ffilled.groupby(level="ticker").bfill()

        imputer = SimpleImputer(strategy="median")
        df_imputed = pd.DataFrame(
            imputer.fit_transform(df_filled),
            columns=df_filled.columns,
            index=df_filled.index,
        )

        df_imputed.replace([np.inf, -np.inf], np.nan, inplace=True)
        df_imputed.dropna(inplace=True)

        if verbose:
            print("Final shape:", df_imputed.shape)

        return df_imputed
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        return None


def postprocess_reduced_data(reduced_data, original_df):
    """Convert reduced data back to panel format."""
    try:
        result_df = pd.DataFrame(
            reduced_data,
            index=original_df.index,
            columns=[f"component_{i}" for i in range(reduced_data.shape[1])],
        )
        return result_df
    except Exception as e:
        print(f"Error in postprocessing: {e}")
        return None


def apply_dimensionality_reduction(df, method, n_components, random_state=42):
    """Apply dimensionality reduction technique."""
    try:
        df_processed = preprocess_panel_data(df, verbose=False)
        if df_processed is None or df_processed.empty:
            return df

        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(df_processed)

        if np.isnan(data_scaled).any() or np.isinf(data_scaled).any():
            print("Warning: NaNs or inf values present after scaling")
            return df

        reducer_methods = {
            "pca": PCA,
            "truncated_svd": TruncatedSVD,
            "factor_analysis": FactorAnalysis,
            "gaussian_random_projection": GaussianRandomProjection,
            # "umap": umap.UMAP,
        }
        reducer = reducer_methods[method](
            n_components=n_components, random_state=random_state
        )
        reduced_data = reducer.fit_transform(data_scaled)

        result_df = postprocess_reduced_data(reduced_data, df_processed)
        return result_df if result_df is not None else df
    except Exception as e:
        print(f"Error during dimensionality reduction: {e}")
        return df


def dimensionality_reduction(
    df, method="pca", explained_variance=0.95, n_components=None, verbose=False
):
    """
    Perform dimensionality reduction on panel data.

    Parameters:
    df (pd.DataFrame): Input DataFrame with MultiIndex (ticker, date)
    method (str): Dimensionality reduction method.
    explained_variance (float): Amount of variance to be explained if n_components is None.
    n_components (int, optional): Number of components to keep.
    verbose (bool): If True, print debugging information

    Returns:
    pd.DataFrame: Reduced data in panel format
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        df_pivot = preprocess_panel_data(df, verbose)
        if df_pivot is None or df_pivot.empty:
            print(
                "Preprocessing failed or resulted in empty DataFrame. Returning original DataFrame."
            )
            return df

        if verbose:
            print("Shape after preprocessing:", df_pivot.shape)

        if n_components is None:
            if method in ["pca", "truncated_svd"]:
                pca = PCA(random_state=42)
                pca.fit(df_pivot)
                cumulative_variance_ratio = np.cumsum(pca.explained_variance_ratio_)
                n_components = (
                    np.argmax(cumulative_variance_ratio >= explained_variance) + 1
                )
                if verbose:
                    print(
                        "Number of components based on variance threshold:",
                        n_components,
                    )
            else:
                n_components = min(
                    int(df_pivot.shape[1] * explained_variance), df_pivot.shape[1]
                )

        return apply_dimensionality_reduction(df, method, n_components)
