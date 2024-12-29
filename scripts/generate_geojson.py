import json
import folium
from folium.plugins import HeatMap

def create_heatmap_with_search(geojson_file, output_html="heatmap.html"):
    """
    Creates a heatmap from GeoJSON data using Folium with a lat/lon search bar.

    Args:
        geojson_file: Path to the GeoJSON file.
        output_html: Path to save the output HTML file.
    """
    try:
        with open(geojson_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{geojson_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{geojson_file}'.")
        return

    heat_data = [[feature['geometry']['coordinates'][0][1], feature['geometry']['coordinates'][0][0]] for feature in data['features']]

    if heat_data:
        center_lat = sum(coord[0] for coord in heat_data) / len(heat_data)
        center_lon = sum(coord[1] for coord in heat_data) / len(heat_data)
        m = folium.Map(location=[center_lat, center_lon], zoom_start=10)
    else:
        print("No coordinate data found in the GeoJSON. Creating a default map.")
        m = folium.Map(location=[43.7, -79.38], zoom_start=10)

    HeatMap(heat_data, radius=25).add_to(m)

    # Add search bar
    m.add_child(folium.LatLngPopup())  # Needed for right-click coordinates

    # Custom JavaScript for the search functionality
    js = """
    <div style="position: absolute; top: 10px; left: 10px; z-index: 9999; background-color: white; padding: 5px; border-radius: 5px;">
        Latitude: <input type="number" id="lat" step="0.000001" value="" style="width: 100px;"><br>
        Longitude: <input type="number" id="lon" step="0.000001" value="" style="width: 100px;"><br>
        <button onclick="goToLocation()">Go</button>
    </div>
    <script>
        function goToLocation() {
            var lat = document.getElementById("lat").value;
            var lon = document.getElementById("lon").value;
            if (lat && lon && !isNaN(lat) && !isNaN(lon)) {
                map.setView([lat, lon], 15); // Zoom level 15
            } else {
                alert("Please enter valid latitude and longitude.");
            }
        }
    </script>
    """
    m.get_root().html.add_child(folium.Element(js))

    m.save(output_html)
    print(f"Heatmap with search saved to {output_html}")


create_heatmap_with_search("datasets\json.txt")