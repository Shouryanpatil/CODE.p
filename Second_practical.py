from Bio import ExPASy, SwissProt
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# List of UniProt IDs
uniprot_ids = ["P04406", "P02768", "P98073", "Q3SYW2", "Q867B7", "P23604", "Q04962", "H2QKV6"]

# Output header
print(f"{'Gene Name (UniProt ID)':<35}{'Theoretical pI':<20}{'Molecular Weight'}")

# Fetch and process data for each protein
for uniprot_id in uniprot_ids:
    try:
        # Fetch SwissProt record
        handle = ExPASy.get_sprot_raw(uniprot_id)
        record = SwissProt.read(handle)
        gene_name = record.entry_name  # Get gene name
        sequence = record.sequence     # Get protein sequence

        # Analyze sequence properties
        analysed_seq = ProteinAnalysis(sequence)
        molecular_weight = analysed_seq.molecular_weight()
        theoretical_pI = analysed_seq.isoelectric_point()

        # Print result with proper formatting
        print(f"{gene_name} ({uniprot_id}):".ljust(35) + f"{theoretical_pI:<20.2f}{molecular_weight:.2f}")
    except Exception as e:
        print(f"Error fetching data for {uniprot_id}: {e}")
