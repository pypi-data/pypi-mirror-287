import pandas as pd
import json

def handle_BTK_wT_101():
    data = pd.read_excel('./BTKbindingData.xlsx', sheet_name='BTK_wT_101')
    data = data[['Ligand SMILES', 'Ki (nM)']]
    data = data.drop_duplicates(subset=['Ligand SMILES'])
    data['Ki (nM)'] = pd.to_numeric(data['Ki (nM)'], errors='coerce')  # 确保是数字格式
    json_data = data.set_index('Ligand SMILES')['Ki (nM)'].to_dict()  # 直接转换为字典

    with open('./benchmark_affinity_wT.json', 'w') as f:
        json.dump(json_data, f, indent=4)

    print("JSON data has been saved to file.")

def handle_BTK_M_343():
    data = pd.read_excel('./BTKbindingData.xlsx', sheet_name='BTK_M_343')
    data = data[['Ligand SMILES', 'IC50 (nM)']]
    data = data.drop_duplicates(subset=['Ligand SMILES'])
    data['IC50 (nM)'] = pd.to_numeric(data['IC50 (nM)'], errors='coerce')  # 确保是数字格式
    json_data = data.set_index('Ligand SMILES')['IC50 (nM)'].to_dict()  # 直接转换为字典

    with open('./benchmark_affinity_M.json', 'w') as f:
        json.dump(json_data, f, indent=4)

    print("JSON data has been saved to file.")


if __name__ == "__main__":
    handle_BTK_wT_101()
    handle_BTK_M_343()
