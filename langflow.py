from langflow import load_flow_from_json

flow_path = 'langflow_first.json'
flow = load_flow_from_json(flow_path, build=False)
