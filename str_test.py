def count_word_occurrences(file_path, target_word):
    """
    Count the occurrences of a specific word in a text file.
    
    Args:
        file_path (str): Path to the text file
        target_word (str): The word to count
    
    Returns:
        int: Number of occurrences of the word
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Convert to lowercase for case-insensitive matching
            content_lower = content.lower()
            target_word_lower = target_word.lower()
            # Count occurrences
            count = content_lower.count(target_word_lower)
            return count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

def count_word_occurrences_advanced(file_path, target_word):
    """
    Count the occurrences of a specific word in a text file (advanced version).
    This version considers word boundaries to avoid partial matches.
    
    Args:
        file_path (str): Path to the text file
        target_word (str): The word to count
    
    Returns:
        int: Number of occurrences of the word
    """
    import re
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Use regex with word boundaries for exact matches
            pattern = r'\b' + re.escape(target_word) + r'\b'
            matches = re.findall(pattern, content, re.IGNORECASE)
            return len(matches)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0

# Example usage
if __name__ == "__main__":
    # Example with a sample text file
    file_path = "mydata.txt"  # You can change this to any text file
    word_to_count = "better"  # Change this to the word you want to count
    
    # Simple counting method
    count = count_word_occurrences(file_path, word_to_count)
    print(f"The word '{word_to_count}' appears {count} times in '{file_path}' (simple method)")
    
    # Advanced counting method (with word boundaries)
    count_advanced = count_word_occurrences_advanced(file_path, word_to_count)
    print(f"The word '{word_to_count}' appears {count_advanced} times in '{file_path}' (advanced method)")