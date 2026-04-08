import requests
def get_cat_image(api_key):
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        "x-api-key": api_key
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            print("No cat image found.")
            return None
        return data[0]['url']
    except requests.exceptions.RequestException as e:
        print(f"API or network error:{e}")
        return None
def save_to_file(url, filename="mycats.txt"):
    try:
        with open(filename, "w") as f:
            f.write(url)
            f.write("\n")
        print(f"Image URL saved to :{filename}.")
    except Exception as e:
        print(f"Error saved to :{e}")
        
def main():
    print("=== CAT IMAGE EXPLORER ===")
    api_key = input("Enter your API key: ")
    cat_url = get_cat_image(api_key)
    if cat_url:
        print("Found cat image URL:")
        print(cat_url)
        save_to_file(cat_url)
main()




