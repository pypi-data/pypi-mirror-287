# cli/label.py

import json
import requests
from .auth import get_headers
from .utils import handle_response, API_ENDPOINT

def get_labels():
    try:
        headers = get_headers()
        response = requests.get(f"{API_ENDPOINT}/label", headers=headers)
        response.raise_for_status()
        return handle_response(response)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error getting labels: {e}")
        return {"error": str(e)}

def delete_label(label):
    try:
        headers = get_headers()
        response = requests.delete(f"{API_ENDPOINT}/label/{label}", headers=headers)
        response.raise_for_status()
        return handle_response(response)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return {"error": str(e)}
    except Exception as e:
        print(f"Error deleting label: {e}")
        return {"error": str(e)}

def handle_label_command(args):
    if args.label_command == "list":
        result = get_labels()
        if 'error' not in result:
            print("Labels:")
            for label in result:
                print(f"  {label}")
        else:
            print(f"Error listing labels: {result['error']}")
    elif args.label_command == "delete":
        result = delete_label(args.label)
        if 'error' not in result:
            print(f"Successfully deleted label: {args.label}")
        else:
            print(f"Error deleting label: {result['error']}")