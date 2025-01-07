import pandas as pd

    
logs = pd.read_csv("Tp_1/logs.csv")

failed_attempts = logs[logs["status"] == "failed"]

failed_counts = failed_attempts.groupby("ip_address").size().reset_index(name="failed_count")

suspicious_ips = failed_counts[failed_counts["failed_count"] > 2]

if not suspicious_ips.empty:
    print("Adresses IP suspectes :")
    print(suspicious_ips)
else:
    print("Aucune adresse IP suspecte détectée.")


