from auth import get_token
from strava import get_activities
import pandas as pd

#From the browser page, authorise, then grab the code and replace it in below line
token_data = get_token("8b8fbdce6957e4e7fe4c4d945f0a85e9081496bf")

print(token_data)

access_token = token_data["access_token"]

print(access_token)

activities = get_activities(access_token)

for act in activities:
    print(act["name"]," ", round(act["distance"]/1000,1),"km")

df = pd.DataFrame(activities)
print(df)

import polyline

# Example: last activity
#poly = activities[0]['map']['summary_polyline']
#points = polyline.decode(poly)  # returns list of (lat, lon) tuples

#print(points)

import folium

# center map at first point
#m = folium.Map(location=points[0], zoom_start=13)
# add route
#folium.PolyLine(points, color="red", weight=4).add_to(m)
# save to HTML
#m.save("activity1_map.html")

maps_html = []

for act in activities:

    poly = act["map"]["summary_polyline"]
    points = polyline.decode(poly)

    # distance conversion
    distance_km = round(act["distance"] / 1000, 2)
    title = act["name"]

    # bounding box
    lats = [p[0] for p in points]
    lons = [p[1] for p in points]
    bounds = [[min(lats), min(lons)], [max(lats), max(lons)]]

    # create map
    m = folium.Map(width=350, height=350)

    folium.PolyLine(
        points,
        color="#FC4C02",
        weight=5,
        opacity=0.9
    ).add_to(m)

    m.fit_bounds(bounds)

    # title block
    title_html = f"""
    <div style="text-align:center; font-family:Arial;">
        <h3 style="margin-bottom:2px; color:#FC4C02;">{title}</h3>
        <p style="margin-top:0px; color:gray;">{distance_km} km</p>
    </div>
    """

    maps_html.append(title_html + m.get_root().render())


# build page
html_page = f"""
<html>

<head>

<style>

body {{
    font-family: Arial;
}}

.container {{
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 20px;
}}

.mapbox {{
    text-align: center;
}}

</style>

</head>

<body>

<h2 style="text-align:center;">My Last 3 Activities</h2>

<div class="container">

<div class="mapbox">
{maps_html[0]}
</div>

<div class="mapbox">
{maps_html[1]}
</div>

<div class="mapbox">
{maps_html[2]}
</div>

</div>

</body>

</html>
"""

with open("last3_activities.html", "w", encoding="utf-8") as f:
    f.write(html_page)