!pip install pgmpy pandas

import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

from pgmpy.models import DiscreteBayesianNetwork

model = DiscreteBayesianNetwork([
    ('Rain', 'WetGrass'),
    ('Sprinkler', 'WetGrass')
])

model.fit(data)

for cpd in model.get_cpds():
    print(cpd)
    print()

inference = VariableElimination(model)

# P(Rain, Sprinkler | WetGrass = 1)
result = inference.query(variables=['Rain', 'Sprinkler'], evidence={'WetGrass': 1})
print(result)