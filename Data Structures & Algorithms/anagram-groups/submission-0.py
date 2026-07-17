class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for word in strs:
            key=''.join(sorted(word))

            if key in h:
                h[key].append(word)
            else:
                h[key]=[word]

        return list(h.values())

# Take one word
#         │
#         ▼
# Sort it
#         │
#         ▼
# Convert it to a string (key)
#         │
#         ▼
# Is the key already in the dictionary?

# YES → Append the word

# NO → Create a new list

# Repeat for every word

# Return all dictionary values


