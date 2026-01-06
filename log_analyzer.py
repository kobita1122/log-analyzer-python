logs = [
    "INFO User login",
    "ERROR Database failed",
    "INFO Data fetched",
    "ERROR Timeout"
]

errors = [l for l in logs if l.startswith("ERROR")]

print("Total logs:", len(logs))
print("Error logs:", len(errors))

for e in errors:
    print(e)
