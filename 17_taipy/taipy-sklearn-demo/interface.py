from taipy.gui import Markdown

selected_scenario = None
figure = None
    
def on_change(state, var_name):
    if var_name == "selected_scenario":
        state.figure = state.selected_scenario.fig.read()

root_page = """
<|container|

# Decision region plots from Sklearn models 

<intro_card|card|

## A comparison of the decision region plots from different models on moons dataset.

Select a model below to visualize its decision boundary.

<br/>

Learn more in the <a href="https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_model_name.html#sphx-glr-auto-examples-neural-networks-plot-mlp-model_name-py" target="_blank">scikit-learn docs</a> 


<br/>

|intro_card>

<br/>

### Select a model:

<layout_scenario|layout|columns=1 2|

<|{selected_scenario}|scenario_selector|show_add_button=False|>

<scenario|part|render={selected_scenario}|

<|chart|figure={figure}|>

|scenario>

|layout_scenario>

|>
"""

interface = Markdown(root_page)
