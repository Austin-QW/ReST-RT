import os
import json
input_path = "./all_combined.jsonl"  # Your input file
output_path = "./all_combined_renamed.jsonl"  # Your output file

with open(input_path, "r") as infile, open(output_path, "w") as outfile:
    for line in infile:
        data = json.loads(line)
        if "prompt" in data:
            data["instruction"] = data.pop("prompt")  # Rename "prompt" → "instruction"
        if "completion" in data:
            data["output"] = data.pop("completion")   # Rename "completion" → "output"
        outfile.write(json.dumps(data) + "\n")  # Write modified line