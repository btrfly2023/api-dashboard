import requests
import json
from datetime import datetime

def query_api():
    # Replace with your actual API endpoint

    try:
        data = {}
        data["data"] = {} 
        api_map = {
            "c2tp_fxs_balance": "https://api.etherscan.io/v2/api?chainid=1&module=account&action=tokenbalance&contractaddress=0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0&address=0xAAc0aa431c237C2C0B5f041c8e59B3f1a43aC78F&tag=latest&apikey=9VJBZTCTTQVCZNGDWTIP995JQQ1XKGN9KY",
            "c2tp_fxs_balance_1": "https://api.etherscan.io/v2/api?chainid=1&module=account&action=tokenbalance&contractaddress=0x3432B6A60D23Ca0dFCa7761B7ab56459D9C964D0&address=0xAAc0aa431c237C2C0B5f041c8e59B3f1a43aC78F&tag=latest&apikey=9VJBZTCTTQVCZNGDWTIP995JQQ1XKGN9KY"
        }
        for api_id, api in api_map.items():
            response = requests.get(api)
            result = response.json()
            data["data"][api_id] = result
            # {'status': '1', 'message': 'OK', 'result': '0'}
        print(data)

        # For demonstration, we'll simulate API data
        # Remove this and uncomment the above in production
        # data = {
        #     "data": [
        #         {"name": "Item 1", "value": 42},
        #         {"name": "Item 2", "value": 73},
        #         {"name": "Item 3", "value": 128}
        #     ]
        # }
        #
        # Add timestamp
        data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return data

    except Exception as e:
        print(f"Error querying API: {e}")
        # Return fallback data in case of error
        return {
            "data": [{"name": "Error", "value": "Failed to fetch data"}],
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

def generate_html(data):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>API Data Dashboard</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background-color: #f2f2f2; }}
        .updated {{ color: #666; font-size: 0.8em; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>API Data Dashboard</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Value</th>
            </tr>
"""

    # Add rows for each data item
    for k,v in data["data"].items():
        html += f"""
                <tr>
                <td>{k}</td>
                <td>{v["result"]}</td>
                </tr>"""

    # Close the table and add last updated timestamp
    html += f"""
        </table>
        <p class="updated">Last updated: {data["last_updated"]}</p>
    </div>
</body>
</html>
"""
    return html

def main():
    # Query the API
    api_data = query_api()

    # Generate HTML
    html_content = generate_html(api_data)

    # Write to file
    with open("index.html", "w") as f:
        f.write(html_content)

    print("HTML file generated successfully!")

if __name__ == "__main__":
    main()
