import os   

base_directory = os.getcwd()

for i in range(1, 39):
    os.rename(os.path.join(base_directory, f"sequence({i}).fasta"), os.path.join(base_directory, f"CDS{i}.fasta"))