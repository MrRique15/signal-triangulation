#!/usr/bin/env python

from utils.classes.receptor import Receptor
from utils import utils

def first_step(receptors, **kwargs):
    
    list_receptor = []
    
    for i in receptors:
        list_receptor.append(
            Receptor(
                coordinates=receptors[i]["coordinates"], 
                p0k=receptors[i]["p0k"], 
                lk=receptors[i]["lk"], 
                color=receptors[i]["color"], 
                radius=receptors[i]["radius"], 
                name=i
            )
        )
        
    utils.create_plot(receptors=list_receptor, case=kwargs['case1_pk'], emissor=kwargs['emissor'], caseName="Case 1")
    utils.create_plot(receptors=list_receptor, case=kwargs['case2_pk'], emissor=kwargs['emissor'], caseName="Case 2")
        
def main():
    emissor = [0.00, 9.00]
    case1_pk = {"R1": -48.4, "R2": -50.6, "R3": -32.2, "R4": -47.4, "R5": -46.3}
    case2_pk = {"R1": -46.9, "R2": -46.4, "R3": -41.2, "R4": -45.8, "R5": -48.7}
    receptors = {
        "R1": {"coordinates": [1.55,17.63], "p0k": -26.0, "lk": 2.1, "color": "red", "radius": 0},
        "R2": {"coordinates": [-4.02,0.00], "p0k": -33.8, "lk": 1.8, "color": "orange", "radius": 0},
        "R3": {"coordinates": [-4.40,9.60], "p0k": -29.8, "lk": 1.3, "color": "blue", "radius": 0},
        "R4": {"coordinates": [9.27,4.64 ], "p0k": -31.2, "lk": 1.4, "color": "violet", "radius": 0},
        "R5": {"coordinates": [9.15,12.00], "p0k": -33.0, "lk": 1.5, "color": "black", "radius": 0}
    }
    
    try:
        first_step(
            receptors=receptors, 
            case1_pk=case1_pk, 
            case2_pk=case2_pk,
            emissor=emissor
        )
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()