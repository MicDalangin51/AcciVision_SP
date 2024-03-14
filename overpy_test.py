import overpy

# Initialize the Overpass API
api = overpy.Overpass()

# Define a query to fetch major roads in Metro Manila
# You can adjust the query based on your specific needs
query = """
area["name"="Metro Manila"]->.searchArea;
(
  way["highway"](area.searchArea);
);
out body;
>;
out skel qt;
"""

# Execute the query
result = api.query(query)

# Process the result
for way in result.ways:
    print("Name: {}, Road Type: {}".format(way.tags.get("name", "n/a"), way.tags.get("highway")))
    break
    # Calculate road length here if needed
