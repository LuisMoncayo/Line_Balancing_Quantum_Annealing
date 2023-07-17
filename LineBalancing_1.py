#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:28:36 2023

@author: luismoncayo
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 14:11:53 2023

@author: luismoncayo
"""
#######################
### FINAL VERSION 
### DO NOT MODIFY IT
#######################

from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel

tA = 2
tB = 3
tC = 4
tD = 1
tE = 2
tF = 3
tG = 2
C = 10#min

bqm = BinaryQuadraticModel('BINARY')

y1 = bqm.add_variable('y1',1)
y2 = bqm.add_variable('y2',1)

xA1 = bqm.add_variable('xA1', 1)
xB1 = bqm.add_variable('xB1', 1)
xC1 = bqm.add_variable('xC1', 1)
xD1 = bqm.add_variable('xD1', 1)
xE1 = bqm.add_variable('xE1', 1)
xF1 = bqm.add_variable('xF1', 1)
xG1 = bqm.add_variable('xG1', 1)

xA2 = bqm.add_variable('xA2', 1)
xB2 = bqm.add_variable('xB2', 1)
xC2 = bqm.add_variable('xC2', 1)
xD2 = bqm.add_variable('xD2', 1)
xE2 = bqm.add_variable('xE2', 1)
xF2 = bqm.add_variable('xF2', 1)
xG2 = bqm.add_variable('xG2', 1)

zero = 1
one = 100
two = 200
three = 85
bqm.add_linear_equality_constraint([(y1,1),(y2,1)],
                                   lagrange_multiplier = zero,
                                   constant=-2)

bqm.add_linear_inequality_constraint([(xA1,tA),(xB1,tB),(xC1,tC),(xD1,tD),(xE1,tE),(xF1,tF),(xG1,tG),(y1,-C)], 
                                     #lb = 0, 
                                     #ub = 7,
                                     constant = 0,
                                     lagrange_multiplier = one, 
                                     label = 'c1')
bqm.add_linear_inequality_constraint([(xA2,tA),(xB2,tB),(xC2,tC),(xD2,tD),(xE2,tE),(xF2,tF),(xG2,tG),(y2,-C)], 
                                     #lb = 0, 
                                     #ub = 7,
                                     constant = 0,
                                     lagrange_multiplier = one, 
                                     label = 'c2')

bqm.add_linear_equality_constraint([(xA1,1),(xA2,1)], 
                                     lagrange_multiplier = two,
                                     constant=-1)#A
bqm.add_linear_equality_constraint([(xB1,1),(xB2,1)], 
                                     lagrange_multiplier = two,
                                     constant=-1)#B
bqm.add_linear_equality_constraint([(xC1,1),(xC2,1)], 
                                     lagrange_multiplier = two,
                                     constant=-1)#C
bqm.add_linear_equality_constraint([(xD1,1),(xD2,1)], 
                                     lagrange_multiplier = two,
                                     constant=-1)#D
bqm.add_linear_equality_constraint([(xE1,1),(xE2,1)], 
                                     lagrange_multiplier = two,
                                     constant=-1)#E
bqm.add_linear_equality_constraint([(xF1,1),(xF2,1)], 
                                     lagrange_multiplier = two,
                                     constant=-1)#F
bqm.add_linear_equality_constraint([(xG1,1),(xG2,1)], 
                                     lagrange_multiplier = two,
                                     constant=-1)#G

bqm.add_linear_inequality_constraint([(xA1,1),(xA2,2),(xB1,-1),(xB2,-2)], 
                                     constant = 0,
                                     lagrange_multiplier = three, 
                                     label = 'A-B')
bqm.add_linear_inequality_constraint([(xA1,1),(xA2,2),(xC1,-1),(xC2,-2)], 
                                     constant = 0,
                                     lagrange_multiplier = three, 
                                     label = 'A-C')
bqm.add_linear_inequality_constraint([(xA1,1),(xA2,2),(xD1,-1),(xD2,-2)], 
                                     constant = 0,
                                     lagrange_multiplier = three, 
                                     label = 'A-D')
bqm.add_linear_inequality_constraint([(xB1,1),(xB2,2),(xE1,-1),(xE2,-2)], 
                                     constant = 0,
                                     lagrange_multiplier = three, 
                                     label = 'B-E')
bqm.add_linear_inequality_constraint([(xC1,1),(xC2,2),(xE1,-1),(xE2,-2)], 
                                     constant = 0,
                                     lagrange_multiplier = three, 
                                     label = 'C-E')
bqm.add_linear_inequality_constraint([(xD1,1),(xD2,2),(xF1,-1),(xF2,-2)], 
                                     constant = 0,
                                     lagrange_multiplier = three, 
                                     label = 'D-F')
bqm.add_linear_inequality_constraint([(xE1,1),(xE2,2),(xF1,-1),(xF2,-2)], 
                                     constant = 0,
                                     lagrange_multiplier = three, 
                                     label = 'E-F')
bqm.add_linear_inequality_constraint([(xF1,1),(xF2,2),(xG1,-1),(xG2,-2)], 
                                     constant = 0,
                                     lagrange_multiplier = three, 
                                     label = 'F-G')

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample(bqm, num_reads=4500)

sample = sampleset.first.sample








