import pandas as pd
import os
import quandl as Quandl
import time

auth_tok = "4p918nYkAPj-_7fYFEaf"

data = Quandl.get("WIKI/KO", authtoken=auth_tok)

print(data)
