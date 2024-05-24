# Filename: anomaly_detection.py

import pathway as pw

# Define schema for the Pathway table
class InputSchema(pw.Schema):
    transaction_id: int
    transaction_amount: float
    transaction_time: str

# Create a Pathway table from the CSV file
table = pw.io.csv.read("/workspaces/Pathway-Anomalies-Detection/transactions_with_anomalies.csv", schema=InputSchema)

# Define a threshold for anomaly detection
threshold = 140

# Detect anomalies based on the threshold
def detect_anomalies(transaction_amount):
    return transaction_amount > threshold

# Apply the anomaly detection function
anomalies = table.select(
    table.transaction_id,
    table.transaction_amount,
    table.transaction_time,
    is_anomaly=pw.apply(detect_anomalies, table.transaction_amount)
)

# Write the anomalies to an output CSV file
pw.io.csv.write(anomalies, "anomalies.csv")

# Run the Pathway pipeline
pw.run()
