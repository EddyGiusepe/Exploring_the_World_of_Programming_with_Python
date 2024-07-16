#!/usr/bin/env python3
"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import sys

#from agencia_clipping.crew import AgenciaNoticiasCrew
from crew import AgenciaNoticiasCrew
input_cmd = sys.argv[1]

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': input_cmd
    }
    AgenciaNoticiasCrew().crew().kickoff(inputs=inputs)



if __name__ == "__main__":
    run() 