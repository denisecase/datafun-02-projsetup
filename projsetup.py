''' Example of importing from another custom module '''

# 2. Import Dependencies (At the Top, After the Introduction)
import time
import pathlib
import Dowdle_utils # import your custom module

# 5. Define Main Function
def main():
    ## print some things from the from imported module
    ## most of these are variables - not functions, so don't use () when requesting them
    print(Dowdle_utils)
    print(Dowdle_utils.accepts_international_clients)
    print(Dowdle_utils.average_contract)
    print(Dowdle_utils.client_satisfaction_scores)
    print(Dowdle_utils.accepts_international_clients)
    print(Dowdle_utils.byline)
    print(f"Byline: {Dowdle_utils.byline}")

# Conditional Script Execution (at the end of the file)
if __name__ == '__main__':
    print("Starting project setup program.")
    main()
    print("Done.")
