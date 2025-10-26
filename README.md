# 🐾 CS-340 Project Two — Grazioso Salvare Search & Rescue Dashboard

### Student: Brianna Reed  
### Course: CS-340 – Client/Server Development  
### Institution: Southern New Hampshire University  

---

## 1️⃣ Project Overview

This project implements a fully functional MongoDB-based Search and Rescue Dashboard for Grazioso Salvare, an international animal training organization.  
The purpose of this dashboard is to identify animals that are the best candidates for specialized rescue missions — such as water rescue, mountain/wilderness rescue, and disaster/individual tracking.

The application connects to a MongoDB database containing real animal shelter data from the Austin Animal Center, and visualizes the data interactively using Python, Dash, and Plotly.

### Key Features

- 📊 Interactive table of animals with sortable and searchable data  
- 🧭 Filter buttons for rescue type selection (Water, Mountain/Wilderness, Disaster, Reset)  
- 🗺️ Dynamic geolocation map that updates based on the selected animal  
- 🧬 Breed distribution chart displaying top 10 breeds in the current view  
- 📁 Export filtered data to CSV  
- 🎨 Intuitive, branded interface with Grazioso Salvare logo  

---

## 2️⃣ Required Functionality

### Proof of Functionality
All requirements for interactivity, design, and responsiveness were successfully met.

| Evidence | Description |
|-----------|--------------|
| `1 reset all view.png` | Default unfiltered dataset view |
| `2 water rescue.png` | Water rescue filter applied |
| `3 mountain wilderness.png` | Mountain/Wilderness rescue applied |
| `4 disaster rescue.png` | Disaster/Individual tracking filter applied |
| `filters.gif | Video demo showing selection of each animal and dynamic map updates |

---

## 3️⃣ Tools and Technologies Used

| Tool | Purpose |
|------|----------|
| MongoDB | Non-relational database to store and query animal data |
| Python | Core logic and CRUD integration |
| Pandas | Converts MongoDB query results into DataFrames |
| Dash / Plotly Express | Interactive UI and data visualizations |
| dash_table.DataTable | Sortable, exportable data table |
| dash_leaflet | Interactive map rendering animal coordinates |
| JupyterDash | Integrates Dash inside JupyterLab for development |

---

## 4️⃣ Development Process

The project followed a Model-View-Controller (MVC) approach:

- Model: `CRUD_Python_Module.py` handled MongoDB CRUD operations  
- View: Dash components defined the interface layout  
- Controller: Callback functions handled filter logic and data updates  

### Build Steps

1. Connected to MongoDB via CRUD module  
2. Implemented `build_query()` for each rescue category  
3. Converted query results to Pandas DataFrames  
4. Built UI layout (logo, header, filters, table, chart, map)  
5. Linked callbacks for dynamic updates  
6. Applied consistent styling and responsiveness  
7. Tested and verified each rescue type  

---

## 5️⃣ Challenges and Solutions

| Challenge | Solution |
|------------|-----------|
| IndentationError: “unindent does not match any outer indentation level.” | Standardized indentation to 4 spaces |
| Missing `breed` column in chart | Normalized DataFrame before plotting |
| Map not centering with no selection | Added fallback coordinates for Austin, TX |
| Layout inconsistent between browsers | Used CSS flex containers and width constraints |
| Table overflow | Enabled pagination and horizontal scroll |

---

## 6️⃣ Reproduction Instructions

```bash
# Step 1 – Install dependencies
pip install dash dash_leaflet pandas numpy plotly jupyter-dash pymongo

# Step 2 – Verify MongoDB connection
# Load Austin Animal Center dataset and ensure authentication
username = "aacuser"
password = "SNHU1234"

# Step 3 – Launch Jupyter
jupyter lab

# Step 4 – Run project
Open ProjectTwoDashboard.ipynb → Run all cells

# Step 5 – Start Dash server
app.run_server(mode="jupyterlab")
````

---

## 7️⃣ Demonstration Media

All demo assets are located in `/screenshots`:

 1 reset all view.png
 2 water rescue.png
 3 mountain wilderness.png
 4 disaster rescue.png
 filters.gif

---

## 8️⃣ References

 Austin Animal Center Outcomes Dataset (2020). City of Austin, Texas Open Data Portal.
  [https://doi.org/10.26000/025.000001](https://doi.org/10.26000/025.000001)
 [Dash Documentation](https://dash.plotly.com/)
 [dash_leaflet Documentation](https://dash-leaflet.herokuapp.com/)
 [MongoDB Documentation](https://www.mongodb.com/docs/)
 Southern New Hampshire University (SNHU) CS-340 Course Materials

---

## 9️⃣ Conclusion

This project demonstrates a complete client/server dashboard that unites MongoDB and Python for data-driven insight.
It fulfills Grazioso Salvare’s goal of identifying ideal animal candidates for rescue training quickly and visually.

The dashboard’s interactivity and real-time mapping create a powerful yet intuitive decision-support tool.

---

# 🧠 Module Eight Journal Reflection

## 💡 How do you write programs that are maintainable, readable, and adaptable?

I focus on separation of concerns, clean function design, and meaningful naming conventions.
In Project Two, the CRUD module handled all database logic while Dash managed the interface.
This modular design allows me to make changes to one part without breaking another.
Consistent indentation, docstrings, and error handling make future maintenance easier.

---

## 🧩 How else could you use the CRUD Python module in the future?

The CRUD module’s reusable class architecture can serve as a foundation for any Python–MongoDB project.
It can power REST APIs, automation scripts, or backend services that interact with data collections.
Because it abstracts create/read/update/delete logic, it can be quickly adapted for analytics, dashboards, or cloud integrations.

---

## 🧮 How do you approach a problem as a computer scientist?

I begin by defining the problem in clear, testable terms and visualizing the data flow between components.
For Grazioso Salvare, I broke the challenge into smaller steps: connect to MongoDB, test CRUD operations, visualize data, then add interactivity.
I rely on iterative testing, debugging, and documentation to ensure accuracy and maintain progress visibility.

---

## 🔧 How did this project differ from previous assignments, and what techniques or strategies will you reuse?

This project bridged frontend interactivity and backend logic, unlike earlier tasks that focused solely on algorithms or static databases.
It taught me to integrate multiple technologies — Python, MongoDB, and Dash — in a cohesive product.
In the future, I’ll continue using modular programming, incremental testing, and data visualization strategies to streamline complex projects.

---

## 🌍 What do computer scientists do, and why does it matter?

Computer scientists analyze problems, design efficient systems, and automate solutions that make real-world processes faster and smarter.
This project shows how data visualization can help organizations like Grazioso Salvare save time and resources, ultimately improving rescue outcomes and animal welfare.
Our work matters because well-designed software empowers decision-makers and drives tangible positive impact.

---

## 🔗 Repository Contents

```
ProjectTwoDashboard.ipynb   → Dash dashboard with callbacks and charts  
CRUD_Python_Module.py       → MongoDB CRUD interface  
screenshots/                → Proof of functionality (images + gif)  
README.docx                 → Full report for submission  
README.md                   → This file (for GitHub portfolio)
```

---

## 🏁 Summary

This portfolio artifact showcases how database integration, modular design, and user interactivity can come together in one robust dashboard.
It reflects not only my technical skills but also my ability to design maintainable, adaptable, and human-centered software.

---

### 🔗 GitHub Repository Link

`https://github.com/<YOUR-USERNAME>/cs340-grazioso-dashboard`

---

> “Technology that saves time can also save lives.”
> — Brianna Reed
