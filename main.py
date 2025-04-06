import os

print("data ingestion starting.............")
os.system("python src/data_ingestion.py")
print("data ingestion completed.")

print("data preprocessing starting.............")
os.system("python src/data_preprocessing.py")
print("data preprocessing completed.")

print("feature engineering starting.............")
os.system("python src/feature_engineering.py")
print("feature engineering completed.")

print("model building starting.............")
os.system("python src/model_building.py")
print("model building completed.")


print("model evaluation starting.............")
os.system("python src/model_evaluation.py")
print("model evaluation completed.")