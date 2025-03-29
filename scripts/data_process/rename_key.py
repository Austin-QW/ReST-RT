import os
import json
input_path = "/home/wqi/ReST-RT/ReST-RT/data/train/all_prompts_train.jsonl"  # Your input file
output_path = "/home/wqi/ReST-RT/ReST-RT/data/train/original.jsonl"  # Your output file

with open(input_path, "r") as infile, open(output_path, "w") as outfile:
    for line in infile:
        data = json.loads(line)
        if "prompt" in data:
            data["instruction"] = data.pop("prompt")  # Rename "prompt" → "instruction"
        if "completion" in data:
            data["output"] = data.pop("completion")   # Rename "completion" → "output"
        outfile.write(json.dumps(data) + "\n")  # Write modified line