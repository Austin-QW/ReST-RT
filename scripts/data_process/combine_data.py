# combine_jsonl.py
import json

# Paths to the input JSONL files and the output file
file1_path = "./d2p_q&a.jsonl"  # Replace with your first file's path
file2_path = "./p2d_combined.jsonl"  # Replace with your second file's path
output_path = "./all_combined.jsonl"  # Path for the combined output file

# Open the output file in write mode
with open(output_path, "w") as outfile:
    # Process the first file
    with open(file1_path, "r") as infile1:
        for line in infile1:
            # Write each line from file1 to the output file
            outfile.write(line)

    # Process the second file
    with open(file2_path, "r") as infile2:
        for line in infile2:
            # Write each line from file2 to the output file
            outfile.write(line)

print(f"Combined {file1_path} and {file2_path} into {output_path}")

