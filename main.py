import streamlit as st
import random
import pandas as pd

# Title of the app
st.title("Random Count Generator")

# Input fields for c1 and c2
obj1 = st.text_input("Enter the first object name (obj1):" )
c1 = st.number_input("Enter the object 1's count (c1):", min_value=0, step=1)

obj2 = st.text_input("Enter the second object name (obj2):" )
c2 = st.number_input("Enter the object 2's count (c2):", min_value=0, step=1)

# Button to generate random numbers
if st.button("Generate Random Numbers"):
    if c1 > 0 and c2 > 0:
        # Generate 10 random numbers in the specified ranges
        random_numbers_c1 = [int(c1 - random.uniform(0.05, 0.1) * c1)]
        random_numbers_c2 = [int(c2 - random.uniform(0.05, 0.1) * c2)]
        for i in range(4):
            random_numbers_c1.append(int(random_numbers_c1[-1] - random.uniform(0.1, 0.2) * c1))
            random_numbers_c2.append(int(random_numbers_c2[-1] - random.uniform(0.1, 0.2) * c2))
        
        random_numbers_c1 = sorted(random_numbers_c1, reverse=True)
        random_numbers_c2 = sorted(random_numbers_c2, reverse=True)

        # Generate 5 pairs of random numbers
        pairs = [(random_numbers_c1[i], random_numbers_c2[i]) for i in range(5)]
        
        # Generate a random number different from 0.5 to 2.5 for each pair
        possible_values = [0.5, 1, 1.5, 2, 2.5]
        random_pairs = []
        for x, y in pairs:
            diff_1 = random.choice(possible_values)
            diff_2 = random.choice(possible_values)
            random_pairs.append([int(x + diff_1), int(y + diff_2)])
            random_pairs.append([int(x - diff_1), int(y - diff_2)])
        
        # Display the generated pairs
        table_data = []
        for i in range(10):
            table_data.append([f"Video {2*i+1}+{2*i+2}", random_pairs[i][0], random_pairs[i][1]])

        # Display the table
        st.table(pd.DataFrame(table_data, columns=["Video", obj1, obj2]))
        csv = pd.DataFrame(table_data, columns=["Video", obj1, obj2]).to_csv(index=False)
        st.download_button(
            label="Download table as CSV",
            data=csv,
            file_name='random_count_table.csv',
            mime='text/csv',
        )
    else:
        st.error("Please enter positive numbers for c1 and c2.")