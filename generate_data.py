import numpy as np
import pandas as pd

def generate_data(filename="transactions_with_anomalies.csv", num_transactions=100):
    # Set seed for reproducibility
    np.random.seed(42)

    # Generate random data
    data = {
        "transaction_id": range(1, num_transactions + 1),
        "transaction_amount": np.random.normal(loc=100, scale=20, size=num_transactions),
        "transaction_time": pd.date_range(start="2024-01-01", periods=num_transactions, freq="T")
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Introduce anomalies: manually set some values to be significantly higher or lower
    anomalies_indices = np.random.choice(df.index, size=5, replace=False)
    df.loc[anomalies_indices, 'transaction_amount'] = np.random.uniform(200, 300, size=5)

    # Save the DataFrame to a CSV file for reference
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    generate_data()
