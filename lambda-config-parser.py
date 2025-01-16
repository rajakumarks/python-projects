'''
Problem: Lambda output was saved as output.json file. The output.json file contains a JSON object with a key 'body' which contains a JSON string. The JSON string contains a list of dictionaries. Each dictionary contains a key 'Id'. The task is to write a python script that reads the output.json file, extracts the 'Id' from each dictionary and writes them to a new file 'Id.json'. The script should accept a list of Id as command line arguments. If the list is provided, the script should only write the 'Id' that are present in the list to the new file. If the list is not provided, the script should write all the 'Id' to the new file. If the list contains any 'Id' that are not present in the JSON data, the script should print an error message and exit with status code 1.
set -e
aws lambda invoke \
  --function-name <function-name> \
  --payload "$(echo '{"httpMethod": "GET"}' | base64)" --region <>} \
    output.json || { echo 'Lambda invocation failed'; exit 1; }

{
  "statusCode": 200,
  "body": "[]"
}
Using this script from GH Workflow: Ids=$(python3 IdConfig.py <input>)

'''
import json, sys
def find_clientIds(clientIds=None):
    try:
        with open('output.json', encoding='utf-8') as f:
            data = json.load(f)
            data = json.loads(data['body'])  
            if clientIds:
                for clientId in clientIds:
                    if clientId not in [x['Id'] for x in data]:
                        print(f"Error: {clientId} was not found in json data")
                        exit(1)
                filtered_data = [x for x in data if x['Id'] in clientIds]
                if not filtered_data:
                    print("Error: None of the Id were found in json data")
                    exit(1)
            else:
                filtered_data = data
            with open('Id.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(filtered_data, ensure_ascii=False, indent=4))
            return ','.join([x['Id'] for x in filtered_data])

    except FileNotFoundError:
        print("Error: The file 'output.json' was not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        exit(1)
    except KeyError as e:
        print(f"Error: Missing key in JSON data - {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

clientIds = sys.argv[1].split(',') if len(sys.argv) > 1 else None
Ids = find_clientIds(clientIds) 
print(Ids)
