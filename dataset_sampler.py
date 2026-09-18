import pandas as pd
import random

def sample_garment(dataset_path, n_samples=1):
    # Load first parquet file for sampling
    df = pd.read_parquet(f"{dataset_path}/data/train-00000-of-00039.parquet")
    samples = df.sample(n=n_samples, random_state=42)
    return samples[['garment_id', 'cut', 'material', 'size', 'damage']].to_dict('records')

if __name__ == "__main__":
    dataset_path = "C:/contract-manifest/6-datasource/zenodo-second-hand-fashion-v3"
    samples = sample_garment(dataset_path, 1)
    print(samples)
