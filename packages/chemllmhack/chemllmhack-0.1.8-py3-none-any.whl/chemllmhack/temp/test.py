
from chemllmhack import submit_rex_expression
from chemllmhack import query_run_status
from chemllmhack import get_rex_result

rex_expression = """
(get "Ok" (get 0 (await (get 1 
    ( auto3d_rex
      (json '{"resources":{"gpus":1,"storage":10,"storage_units":"MB"},"target":"Bullet"}')
      (arg (json '{"k":1}'))
      (arg ["CCCC"])
    )
  ))))
"""
res = submit_rex_expression(rex_expression)
run_id= res["run_id"]
res1 = query_run_status(run_id)
print(res1)
save_dir = "./result_dir"
result_path = res1["paths"]
res2 = get_rex_result(result_path, save_dir)

i = 1