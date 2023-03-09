import numpy as np
import pandas as pd

import jpype
import jpype.imports
from jpype.types import *

# os.system('echo export "JAVA_HOME=\\$(/usr/libexec/java_home)" >> ~/.zshrc')
jpype.startJVM(classpath=["/Users/bryanandrews/Desktop/tetrad-gui-7.2.2-launch.jar"])

import java.util as util

import edu.cmu.tetrad.data as td
import edu.cmu.tetrad.graph as tg
import edu.cmu.tetrad.search as ts


df = pd.read_csv("/Users/bryanandrews/Desktop/airfoil-self-noise.continuous.txt", sep="\t")
# df = pd.read_csv("/Users/bryanandrews/Desktop/ruben_data/bold_data/bold_data_0.txt")
cols = df.columns
values = df.values
n, p = df.shape

databox = td.DoubleDataBox(n, p) 
variables = util.ArrayList();
for col, var in enumerate(values.T):
	variables.add(td.ContinuousVariable(cols[col]))
	for row, val in enumerate(var):
		databox.set(row, col, val)

data = td.BoxDataSet(databox, variables)
score = ts.SemBicScore(data)
score.setPenaltyDiscount(2);
score.setStructurePrior(0);

print("\nfGES\n")
fges = ts.Fges(score)
print(fges.search())

print("\nBOSS\n")
boss = ts.Boss(score)
boss.setUseDataOrder(False)
boss.setNumStarts(5)
boss.bestOrder(variables)
print(boss.getGraph(True))

print("\nGRaSP\n")
grasp = ts.Grasp(score)
grasp.setOrdered(False)
grasp.setUseDataOrder(False)
grasp.setNumStarts(5)
grasp.bestOrder(variables)
print(grasp.getGraph(True))

jpype.shutdownJVM()
