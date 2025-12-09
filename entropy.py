import pandas as pd
import numpy as np
from collections import Counter

def calculate_entropy(pos_counts):
    """
    Calculate entropy for a given POS distribution of a word.
    
    Parameters
    ----------
    pos_counts : Counter
        A Counter object containing POS tags as keys and their frequency counts as values.
    
    Returns
    -------
    float
        The entropy value computed using base-2 logarithm. 
        Returns 0 if the word has only one POS tag (no inconsistency potential).
    """
    
    # Total occurrences of the word across all POS tags
    total = sum(pos_counts.values())
    
    # Compute probabilities for each POS tag
    probabilities = [count / total for count in pos_counts.values()]
    
    # Compute entropy using Shannon's formula: H = -Σ p * log2(p)
    entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
    
    # Entropy is only meaningful when there is more than one POS tag
    return entropy if len(pos_counts) > 1 else 0


def process_pos_entropy(file_path, sheet_name=0):
    """
    Process an Excel file containing words and their POS tags, then calculate
    entropy for each word to detect potential labeling inconsistency.
    
    Parameters
    ----------
    file_path : str
        Path to the Excel file containing columns 'Word' and 'POS'.
    
    sheet_name : int or str, optional
        The sheet name or index in the Excel file (default is 0).
    
    Returns
    -------
    pandas.DataFrame
        A DataFrame containing each word and its computed entropy score.
    """

    # Read Excel file containing word–POS pairs
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Ensure the required columns exist
    if not {'Word', 'POS'}.issubset(df.columns):
        raise ValueError("Input file must contain 'Word' and 'POS' columns.")
    
    # Dictionary to store POS frequency counts for each word
    # Case sensitivity is preserved intentionally
    word_pos_counts = {}
    
    # Iterate through each row and accumulate POS counts
    for _, row in df.iterrows():
        word = str(row['Word']).strip()   # Keep original case
        pos = str(row['POS']).strip()
        
        # Initialize Counter for new words
        if word not in word_pos_counts:
            word_pos_counts[word] = Counter()
        
        # Increment POS count
        word_pos_counts[word][pos] += 1
    
    # Calculate entropy for every word
    entropy_results = {
        word: calculate_entropy(pos_counts)
        for word, pos_counts in word_pos_counts.items()
    }
    
    # Convert result to DataFrame
    entropy_df = pd.DataFrame(list(entropy_results.items()), 
                              columns=['Word', 'Entropy'])
    
    # Save the results into an Excel file
    output_file = 'data/entropy_results.xlsx'
    entropy_df.to_excel(output_file, index=False)
    print(f"Entropy results have been saved to: {output_file}")
    
    return entropy_df


# Example usage
process_pos_entropy("data/revised.xlsx")
