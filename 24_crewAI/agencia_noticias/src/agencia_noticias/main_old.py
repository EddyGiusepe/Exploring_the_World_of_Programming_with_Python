#!/usr/bin/env python
import sys
#from agencia_noticias.crew import AgenciaNoticiasCrew
from crew import AgenciaNoticiasCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    AgenciaNoticiasCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        AgenciaNoticiasCrew().crew().train(n_iterations=int(sys.argv[1]))

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")



if __name__ == "__main__":
    run()