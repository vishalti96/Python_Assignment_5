L = [i for i in range(1,11)]
print(f"Original List: {L}")
Extracted_list = L[:5]
print(f"Extracted first five elements: {Extracted_list}")
Extracted_list.sort(reverse=True)
print(f"Reversed extracted elements: {Extracted_list}")
