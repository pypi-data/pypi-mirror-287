# -*- coding: utf-8 -*-
"""
File name: langchain_research_agent.py
Author: Bowen
Date created: 23/7/2024
Description: This Python file provides a demo showing how to use this SDK for AI research and experiment.

Copyright information: © 2024 QDX
"""

import os
import time

from langchain import hub
from langchain.agents import create_tool_calling_agent, create_react_agent
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_community.chat_message_histories import ChatMessageHistory
from chemllmhack import get_rex_expression
from chemllmhack import submit_rex_expression
from chemllmhack import query
from chemllmhack import affinity_benchmark
from chemllmhack import rmsd_benchmark
from chemllmhack import decompose_query_rag
from chemllmhack import multi_query_rag
from chemllmhack import step_back_query_rag
import chemllmhack

#TODO delete this
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

@tool
def reflection(experiment_result: str) -> str:
    """generate reflection on the experiment result"""
    module_name = "gnina"
    vectordb_path = "./paper_db/chroma_db"

    gnina_parameters_explain = chemllmhack.query("what is the gnina parameters explanation?")

    query = f"the experiment result is as follow, {experiment_result}, the gnina parapmeters explaination is as follow {gnina_parameters_explain}, how to set parameters in gnina to improve the result?"

    ans1 = decompose_query_rag(module_name=module_name, vectordb_path=vectordb_path, question=query)

    #you could enable the following two lines to see the result of multi_query_rag and step_back_query_rag
    # ans2 = multi_query_rag(module_name=module_name, vectordb_path=vectordb_path, question=query)
    # ans3 = step_back_query_rag(module_name=module_name, vectordb_path=vectordb_path, question=query)

    return ans1

@tool
def benchmark() -> list | str:
    """benchmark the performance of Rex language expression"""
    affinity_result_path = "./project/test_benchmark.json"
    benchmark_result_affinity = affinity_benchmark(affinity_result_path, benchmark_name="BTK")

    #TODO delete the simulated pdb because it is actually the benchmark protein
    rmsd_result_path = "./project/simulated.pdb"
    benchmark_rmsd = rmsd_benchmark(rmsd_result_path)

    return[benchmark_result_affinity, benchmark_rmsd]

@tool
def submit_rex(rex_expression: str) -> str:
    """input the rex expression, then this function submit rex expression to RUSH platform, return result"""
    res_submit = submit_rex_expression(rex_expression)
    run_id = res_submit["run_id"]
    # run_id = "7f6dce96-f99a-43dd-a47f-1b4fe112d6c3"
    res_query = chemllmhack.query_run_status(run_id)
    status = res_query["status"]

    #polling query until the status is DONE
    while status != "DONE":
        status = chemllmhack.query_run_status(run_id)["status"]
        print(f"status: {status}")

        time.sleep(5)

    save_dir = "./result_dir"

    path_id = chemllmhack.query_run_status(run_id)["paths"]

    chemllmhack.get_rex_result(path_id, save_dir)

    return "rex expression results have been saved, now you can run benchmark function"

@tool
def read_hackthon_instruction() -> str:
    """This function returns hackthon instruction, including how to generate Rex expression."""

    rex_language_explaination_prepare_protein = get_rex_expression("prepare_protein")
    rex_language_explaination_auto3d = get_rex_expression("auto3d")
    rex_language_explaination_gnina = get_rex_expression("gnina")

    hackthon_task = chemllmhack.query("what is the hackthon task")

    instruction_template = f"""
    Your task is {hackthon_task}
    
    Here is rex language explanation for modules on RUSH
    {rex_language_explaination_prepare_protein}
    {rex_language_explaination_auto3d}
    {rex_language_explaination_gnina}
    
    
    just like the above example, to complete the first task, you can run the {rex_language_explaination_auto3d} on RUSH platform.
    
    """

    return instruction_template

def ai_research():
    model = ChatOpenAI(model="gpt-4")
    tools = [read_hackthon_instruction, reflection, benchmark, submit_rex]

    memory = SqliteSaver.from_conn_string(":memory:")

    prompt = hub.pull("hwchase17/openai-functions-agent")

    agent = create_tool_calling_agent(model, tools, prompt)

    #you could easily extend this agent with memory if needed
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, checkpointer=memory)

    input = """
    You are a AI computational chemist research from QDX company. You are required to compelete automatic research task. 
    
    You need to read the hackthon instruction first to understand how to generate Rex language, which is designed to run in-silico protocol on RUSH.
    
    Then submit the Rex language expression to the RUSH system. run benchmark function to examine the performance of the Rex language expression.
    
    if the result is not good enough, you need to use reflection tool and condsider to improve.
    
    Then you might need to submit the improved Rex language expression to the RUSH system again.  
    """

    agent_executor.invoke({"input": input})


if __name__ == "__main__":
    ai_research()