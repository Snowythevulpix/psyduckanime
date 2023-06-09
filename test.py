# Make a GET request to fetch the JSON data
response = requests.get("https://consumet-api-production-0afb.up.railway.app/meta/anilist/watch/pokemon-2019-episode-1")

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data from the response
    json_data = response.json()

    # Filter the sources based on quality
    filtered_sources = list(filter(lambda source: source['quality'] == '720p', json_data['sources']))

    # Print the filtered sources
    for source in filtered_sources:
        print(source)
else:
    print("Failed to retrieve the JSON data.")

