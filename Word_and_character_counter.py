# Word and Character Counter
print("=== Word and Character Counter ===")
paragraph = input("Enter a paragraph: ")
# Calculate statistics
characters = len(paragraph)
words = len(paragraph.split())
spaces = paragraph.count(" ")
sentences = sum(paragraph.count(mark) for mark in ".!?")
# Display results
print("\n--- Text Analysis Results ---")
print("Characters:", characters)
print("Words:", words)
print("Sentences:", sentences)
print("Spaces:", spaces)
