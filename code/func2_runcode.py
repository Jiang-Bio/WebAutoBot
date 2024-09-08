import sys
sys.path.append(r"E:\test_python")
import func1_get_pwm as func1
import pandas as pd
import os

df=pd.read_excel(r"E:\test_python\all_wrky_selex_seed\wrky_selex_seed.xlsx",sheet_name="Sheet1")
num_rows=df.shape[0] 
for i in range(num_rows):
    print(i)
    line=df.iloc[i].tolist()
    cleaned_line = [x for x in line if not pd.isna(x)]

    pattern=list(cleaned_line[4:])
    well=[cleaned_line[2]]
    batch=cleaned_line[3]
    os.makedirs("all_wrky_selex_seed", exist_ok=True)
    print(well)
    print(batch)
    with open(r"E:\test_python\all_wrky_selex_seed\WRKY_SELEX.log", "a") as f:
        sys.stdout = f
        print(well)
        print(batch)
        
        func1.func( wells=well,webpath=batch,patterns=pattern,directory=r"E:\test_python\all_wrky_selex_seed")
    sys.stdout = sys.__stdout__
    print("#########<<<<done>>>>#########") 