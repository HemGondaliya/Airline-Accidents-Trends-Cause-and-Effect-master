# Airline-Accidents-Trends-Cause-and-Effect
Finding the trends of the past accidents and visualizing it geographically using heat-map and identifying the major causes by clustering based on the phases of flight, climate condition, country and other attributes.

## Instruction to execute the Application:

1.	Extract the .zip file and Install the required packages for the backend server file.
	-	pip install -U flask –user
	-	pip install -U flask-cors –user
	-	pip install -U numpy –user
	-	pip install -U pandas –user
	-   pip install -U scikit-learn --user
	
2. Copy all the json files - aviation_data_event_count.json, aviation_data_heat_map_count.json, cluster_data.json, layout.html, d3.v4.min.js, d3-scale-chromatic.v1.min.js, project.js, simpleheat.js, topojson.v1.min and world-50m.json  to the same folder as server.py
	
3.	Execute the server file ‘server.py’ using the command “python server.py” from command-line. This will read the 3 json files and display data.

4.	Host the file 'layout.html' present in the folder “Frontend” using live server .
	Use browser to view the visualization using http://localhost:8080/Frontend/layout.html (assusming default port is 8080)

5. Click on three different tabs in bottom to view Trend Data, Heat Map and Bubble chart using clustering.

6.	(Optional) Execute the file “Project.ipynb” using google Colaboratory / Jupiter Notebook to get the .json files which is used in the Frontend for visualisation.(since it is already attached)
