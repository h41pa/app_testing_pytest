"""
Pentru a scoate rapoartele hmtl

# pentru pytest :
- ruleaza din interfata din pycharm dupa rulare in stranga jos la test results
     cauti export results buton si alegi formatul html sa salvezi
-install  -  pip install pytest-html  si ruleaza rap cu :
            - pytest NAME.py --html=name.html




"""


"""
pip install pytest
pip install pytest-xdist ( pentru a rula test in paralel

Pytest este un framework de testare care poate fi folosit atat in UniteTesting cat si in Integration Testing,
System Testing, etc. Functional testing in general

### Teste rulate in mod secvential ( unul dupa celalalt ):
pytest nume.py

### Teste rulate in paralel ( mai multe deodata ):
pytest nume.py -n x ( unde x este nr-ul de teste care merg in paralel )
daca dau 3 o sa apara 3 workeri care inseamna 1 worker pe fiecare test , 1worker = 1 cpu
sau daca vrei toate
-pytes -n NUMAR ( numarul de procesaore pentru teste)

python -m pytest -v
v = verbose.
"""