from functions import collatz_df
from plotly import express as px
n = 256
collatz_convergence = px.bar(collatz_df(n),title=f"Collatz process for number {n}",x='steps',y='number')
collatz_convergence.show()

