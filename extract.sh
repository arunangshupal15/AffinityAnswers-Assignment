#!/bin/sh

#Fetch the data and extract Scheme Name and Net Asset Value into a TSV
curl -s "https://www.amfiindia.com/spages/NAVAll.txt" | \
awk -F ';' -v OFS='\t' '{print $4, $5}' > nav_data.tsv

# Utilizing JSON format for data storage presents a range of benefits:
# Structured Representation: JSON inherently offers a hierarchical configuration, which simplifies the portrayal of intricate data relationships.
# Interoperability: JSON enjoys extensive adoption and support among numerous programming languages and platforms, thereby facilitating seamless data exchange.
# Readability: The format is designed to be human-readable and self-descriptive, enhancing comprehension of the data structure.
# Nonetheless, the decision to opt for either TSV or JSON is contingent upon the specific application scenario. If the data is predominantly tabular and will be 
# processed using tools optimized for TSV or CSV formats, then TSV could be the more fitting choice. Conversely, if the data will be utilized by applications that 
# specifically leverage structured formats, or if it involves nested relationships, JSON may prove to be the more advantageous option.