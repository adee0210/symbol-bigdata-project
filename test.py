import glob

file = glob.glob(f"**/symbol_bigdata_project_config.json", recursive=True)
print(file)
