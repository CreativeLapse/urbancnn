# Urban CNN Project

## Overview
Analysis of urban features using CNNs and census data heatmaps.

## Data Sources

### Heat Maps

#### Ethnic Diversity
- URL: https://censusmapper.ca/maps/3601
- Map ID: 3601#17
- Zoom: 17
- Coverage: Greater Toronto Area

#### Median Household Income
- URL: https://censusmapper.ca/maps/3348  
- Map ID: 3348#17
- Zoom: 17
- Coverage: Greater Toronto Area

### Coordinate Data
- Random points within GTA polygon
- Generated using `find_random_coordinates.py`
- Stored in `datasets/coordinates.csv`


## GeoJSON Data Sources

All data sourced from [Toronto Open Data](https://open.toronto.ca/catalogue/)

### Transportation
- [TTC Routes](https://open.toronto.ca/dataset/ttc-routes-and-schedules/) - Transit network coverage
- [Bike Share Stations](https://open.toronto.ca/dataset/bike-share-toronto-stations/) - Bicycle sharing infrastructure
- [Cycling Network](https://open.toronto.ca/dataset/cycling-network/) - Bike lanes and trails

### Education & Community
- [School Locations](https://open.toronto.ca/dataset/school-locations/) - Public and Catholic schools
- [Child Care Centres](https://open.toronto.ca/dataset/child-care-centres/) - Licensed childcare facilities
- [Community Recreation Centres](https://open.toronto.ca/dataset/recreation-centres/) - Community facilities

### Green Spaces
- [Parks](https://open.toronto.ca/dataset/parks/) - Public parks and green spaces
- [Urban Forestry](https://open.toronto.ca/dataset/street-tree-data/) - Street trees and urban canopy
- [Parkland Trails](https://open.toronto.ca/dataset/parks-trails/) - Walking and hiking trails

### Government & Services
- [Civic Centres](https://open.toronto.ca/dataset/civic-centres/) - Municipal buildings
- [Libraries](https://open.toronto.ca/dataset/toronto-public-library-branch-locations/) - Public library branches
- [Emergency Services](https://open.toronto.ca/dataset/emergency-services/) - Police, fire, ambulance


## Directory Structure