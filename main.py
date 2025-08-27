
import csv, math, json, pathlib

# Simple Bayesian likelihood demo for rare disease dataset
data_path = pathlib.Path(__file__).parent/"data"/"patients.csv"
with open(data_path, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    patients = list(reader)

# Hypothesis: patient has disease if symptom_score > threshold
threshold = 0.7
true_pos = sum(1 for p in patients if float(p["symptom_score"])>threshold and p["disease"]=="1")
false_pos = sum(1 for p in patients if float(p["symptom_score"])>threshold and p["disease"]=="0")
true_neg = sum(1 for p in patients if float(p["symptom_score"])<=threshold and p["disease"]=="0")
false_neg = sum(1 for p in patients if float(p["symptom_score"])<=threshold and p["disease"]=="1")

out = {
    "threshold": threshold,
    "true_pos": true_pos,
    "false_pos": false_pos,
    "true_neg": true_neg,
    "false_neg": false_neg,
    "sensitivity": true_pos/(true_pos+false_neg+1e-9),
    "specificity": true_neg/(true_neg+false_pos+1e-9)
}
print(json.dumps(out, indent=2))
(pathlib.Path(__file__).parent/"results"/"output.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
