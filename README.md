# New Nation Generator

This project implements two functions to generate new nations based on the given population or number of states.   
The functions utilize data from the `usstates.csv` and `border_data.csv` files to determine contiguous states and their populations.

## Getting Started

To get started with using the functions, follow these steps:
- Download the `usstates.csv` and `border_data.csv` files.
- Place the files in the same directory as the Python scripts.
- Run the `new_nation_n_states.py` or `new_nation_with_pop.py` script and provide the required arguments to generate new nations.

## Usage

- `new_nation_n_states.py`: Accepts one argument (`n`) and returns the most populous new nation carved out from `n` US states.
- `new_nation_with_pop.py`: Accepts one argument (population in millions) and returns a list of all possible new nations with a minimum number of states, with at least the specified population.
