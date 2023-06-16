import json, os, sys, yaml

# Check file name

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    else:
        print("Error: " + sys.argv[1] + " not found")
        exit(1)
else:
    print("Usage: yaml2json.py <source_file.yaml> [target_file.json]")

output = json.dump(source_content)

if len(sys.argv) < 3:
    print(output)
elif os.path.exists(sys.argv[2]):
    print("ERROR: " + sys.argv[2] + " already exists")
    exit(1)
else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()