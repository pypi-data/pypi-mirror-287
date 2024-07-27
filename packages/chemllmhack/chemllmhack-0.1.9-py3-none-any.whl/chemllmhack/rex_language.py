# -*- coding: utf-8 -*-
"""
File name: rex_language.py
Author: Bowen
Date created: 15/7/2024
Description: Rex language SDK, providing help information and expressions for Rex language

Copyright information: © 2024 QDX
"""
import argparse
import json
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from google.cloud import storage
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(script_dir, 'rex_expressions.json')
try:
    with open(json_path, 'r') as f:
        rex_expressions = json.load(f)
except FileNotFoundError:
    print(f"Warning：cannot find file '{json_path}'.")
    rex_expressions = {}

class Classification(BaseModel):

    module_name: str = Field(
        ...,
        description="the module name or keyword extracted from the query.",
        enum=["auto3d", "prepare_protein", "gnina", "gmx", "comprehensive_example", "hackthon_task", 'gnina_parameter', 'auto3d_parameter']
    )

def query(inp):
    """
    Get the expression of Rex language for RUSH module with natural language
    :return:  the expression of Rex language for RUSH module
    """

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")

    tagging_prompt = ChatPromptTemplate.from_template(
        """
            Your task is to identify the module name or keyword from the query.
            
            for example:
            1. if query is "how to write rex language expression for prepare protein", the output should be 'prepare_protein'
            2. if the query is "can you provide a comprehensive example of rex language" or "how to write a comprehensive rex language expression", the output should be 'comprehensive_example'
            3. if the query is "what is the hackthon task", the output should be 'hackthon_task'
            4. if the query is "can you explain the parameter settings of gnina" the output should be 'gnina_parameter'
            
            note: gromacs is same as gmx.
            
            query:
            {input}
        """
    )

    llm = ChatOpenAI(temperature=0, model="gpt-4-turbo").with_structured_output(
        Classification
    )

    chain = tagging_prompt | llm

    res = chain.invoke({"input": inp})

    res = res.dict()

    expression = get_rex_expression(res["module_name"])

    print(expression)

    return expression

def get_rex_help():
    """
    Get the help information of Rex language
    :return: help information
    """
    return rex_expressions.get("help_info", "Cannot find the help information.")


def get_rex_expression(keyword):
    """
    Get the specific Rex expression for RUSH modules
    :param keyword: the module name of the Rex expression
    :return: the corresponding Rex expression
    """
    return rex_expressions.get(keyword, "Corresponding Rex expression not found, please use 'rex-help expression' to get the list of available expressions.")


def download_vector_db(credential_path="/Users/bowenzhang/.config/gcloud/application_default_credentials.json", destination_file_name="vector_db.zip"):
    """
    Download the vector database from Google Cloud Storage
    :param credential_path:
    :param destination_file_name:
    :return: None
    """

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    storage_client = storage.Client(project="qdx-chem-llm-hackthon")
    bucket_name = "hackthon_paper"
    source_blob_name = "paper_db_test.chroma"

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object to local file {}.".format(
            destination_file_name
        )
    )

def _get_project_id():
    """
    Get the project ID from the project_id.txt file, if the file does not exist, create a new project and save the project ID to the file
    :return:  project ID
    """
    project_id_dir = "./project"
    if not os.path.exists(project_id_dir):
        os.makedirs(project_id_dir)

    project_id_path = "./project/project_id.txt"
    if os.path.exists(project_id_path):
        with open(project_id_path, 'r') as f:
            project_id = f.read().strip()
        if not project_id:
            create_new_project = True
        else:
            project_id = "urn:uuid:" + project_id
            create_new_project = False
            print(f"Using Project ID: \n {project_id} \n")
    else:
        create_new_project = True

    if create_new_project:
        TENGU_TOKEN = os.getenv('TENGU_TOKEN')
        url = 'https://tengu-server-staging-edh4uref5a-as.a.run.app/'

        func_query = """
                mutation {
                  create_project(input: {
                    name: "AI Exp Test",
                    description: "Test for AI experiment",
                    tags: ["test"]
                  }) {
                    id
                    name
                    description
                    tags
                    created_at
                    deleted_at
                  }
                }
                """

        headers = {
            'Authorization': f'Bearer {TENGU_TOKEN}'
        }

        response = requests.post(url, json={'query': func_query}, headers=headers)
        res = response.json()
        project_id = res['data']['create_project']['id']
        print(f"Created Project ID: \n {project_id} \n")
        with open(project_id_path, 'w') as f:
            f.write(project_id)

        project_id = "urn:uuid:" + project_id



    return project_id

def query_run_status(run_id, project_id=None):
    """
    Query the status of the run
    :param run_id: the run ID
    :return: the status of the run and the path id
    """
    if project_id is None:
        project_id = _get_project_id()

    TENGU_TOKEN = os.getenv('TENGU_TOKEN')
    url = 'https://tengu-server-staging-edh4uref5a-as.a.run.app/'

    func_query = """query RunInfoQuery {
                      me {
                        id
                        account {
                          id
                          project(id: "<project_id>") {
                            id
                            run(id: "<run_id>") {
                              id
                              name
                              description
                              tags
                              result
                              status
                              created_at
                              updated_at
                            }
                          }
                        }
                      }
                    }
                """


    headers = {
        'Authorization': f'Bearer {TENGU_TOKEN}'
    }

    func_query = func_query.replace("<project_id>", project_id)
    func_query = func_query.replace("<run_id>", run_id)

    response = requests.post(url, json={'query': func_query}, headers=headers)
    res = response.json()
    if 'errors' in res:
        error = res['errors'][0]['message']
        return error
    try:
        status = res['data']['me']['account']['project']['run']['status']
        if status == "RUNNING" or status == "PENDING":
            return {"status": status, "paths": None}
        paths = res['data']['me']['account']['project']['run']['result'].get("list")[0].get("list")

        if paths is not None:
            paths = [item['record']['path'] for item in paths]

        return {"status": status, "paths": paths}
    except KeyError:
        return "Key not found in response."
    except TypeError:
        return "Response format error or NoneType encountered."

def get_rex_result(path_id_list, save_dir):
    """
    save the result of the Rex expression to the local path
    :param path_id: path ID
    :param save_path:  the local path to save the result
    :return:  None
    """

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    TENGU_TOKEN = os.getenv('TENGU_TOKEN')
    url = 'https://tengu-server-staging-edh4uref5a-as.a.run.app/'

    for path_id in path_id_list:

        func_query = """query object_path_query{
                          object_path (path: "<path_id>") {
                            contents
                          }
                        }
                    """

        headers = {
            'Authorization': f'Bearer {TENGU_TOKEN}'
        }

        func_query = func_query.replace("<path_id>", path_id)

        response = requests.post(url, json={'query': func_query}, headers=headers)
        res = response.json()

        if 'errors' in res:
            error = res['errors'][0]['message']
            return error
        try:
            contents = res['data']['object_path']['contents']
            save_path = os.path.join(save_dir, f"{path_id}.json")
            with open(save_path, 'w') as f:
                json.dump(contents, f, indent=4)
        except KeyError:
            return "Key not found in response."
        except TypeError:
            return "Response format error or NoneType encountered."
    print(f"Result saved to {save_dir}")

def submit_rex_expression(rex_expression):
    project_id = _get_project_id()
    TENGU_TOKEN = os.getenv('TENGU_TOKEN')
    url = 'https://tengu-server-staging-edh4uref5a-as.a.run.app/'

    func_query = """mutation test {
        eval(
            input: {
                project_id: "p_id",
                rex: \"""{rex_expression}\"""
                name: "AI Experiment Run"
                }){
                status
                name
                run_id
                id
                result
                    }
                }
                    """

    func_query = func_query.replace("{rex_expression}", rex_expression)
    func_query = func_query.replace("p_id", project_id)

    headers = {
        'Authorization': f'Bearer {TENGU_TOKEN}'
    }

    response = requests.post(url, json={'query': func_query}, headers=headers)
    res = response.json()
    if 'errors' in res:
        error = res['errors'][0]['message']
        return error
    try:
        status = res['data']['eval']['status']
        run_id = res['data']['eval']['id']
        return {"status": status, "run_id": run_id}
    except KeyError:
        return "Key not found in response."
    except TypeError:
        return "Response format error or NoneType encountered."

def main():
    parser = argparse.ArgumentParser(description='chemllmhack: Rex Language SDK')
    parser.add_argument('--rex-help', choices=['language', 'expression'], help='Get Rex language instructions')
    parser.add_argument('-rex', help='Get a specific Rex expression for a module')

    args = parser.parse_args()

    if args.rex_help == 'language':
        print(get_rex_help())
    elif args.rex_help == 'expression' and args.rex:
        print(get_rex_expression(args.rex))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()