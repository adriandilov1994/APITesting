import requests

head = {
    'X-API-Key': 'f3e6e93a3265e45410a20252c742c589d8a32b26',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json'
}

url = "https://rest.cryptoapis.io/blockchain-data/bitcoin/testnet/addresses/mho4jHBcrNCncKt38trJahXakuaBnS7LK5/transactions?context=&limit=1&offset=0"

# Sending the request
response = requests.get(url, headers=head)

# This is the the response as the provided documentation
expected_response = {
    "apiVersion": str,
    "requestId": str,
    "context": str,
    "data": {
        "limit": int,
        "offset": int,
        "total": int,
        "items": [
            {
                "transactionId": str,
                "index": int,
                "minedInBlockHash": str,
                "minedInBlockHeight": int,
                "recipients": list,
                "senders": [
                    {
                        "address": str,
                        "amount": str
                    }
                ],
                "timestamp": int,
                "transactionHash": str,
                "blockchainSpecific": {
                    "locktime": int,
                    "size": int,
                    "vSize": int,
                    "version": int,
                    "vin": list,
                    "vout": list
                },
                "fee": {
                    "amount": str,
                    "unit": str
                }
            }
        ]
    }
}


if response.status_code == 200:

    api_response = response.json()

    # Check if the response matches the expected types
    def check_types(actual, expected):
        if isinstance(expected, dict):
            return all(key in actual and check_types(actual[key], expected[key]) for key in expected)
        elif isinstance(expected, list):
            return all(check_types(a, expected[0]) for a in actual)
        else:
            return isinstance(actual, expected)

    if not check_types(api_response, expected_response):
        print("Mismatch in the response.")
    else:
        print("The response matches the expected format!")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)
