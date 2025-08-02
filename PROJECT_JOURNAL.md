
# Project Journal: BioVis-3D

This document chronicles the development of the BioVis-3D application, an interactive tool for visualizing and manipulating macromolecular structures.

## Phase 1: Foundation & Core Visualization

**Objective:** Establish the basic application structure and a 3D rendering environment.

- **Actions Taken:**
    - Created the project directory `BioVis-3D`.
    - Set up a Python virtual environment to manage dependencies.
    - Created the main application file `src/main.py` using PyQt6 to establish the main window.
    - Integrated a PyVista `QtInteractor` widget into the main window to serve as the 3D canvas.
- **Outcome:** A functional application window with an embedded, interactive 3D view.

## Phase 2: Local Model Import

**Objective:** Enable the loading of 3D models from local files.

- **Actions Taken:**
    - Added `biopython` to the project dependencies for parsing PDB files.
    - Implemented a "File" -> "Open" menu action.
    - Added logic to use a `QFileDialog` to allow users to select a `.pdb` file.
    - Used BioPython's `PDBParser` to read the atomic data from the selected file.
    - Rendered the molecule in the 3D view by creating a sphere for each atom.
- **Outcome:** Users can load and visualize local PDB files.

## Phase 3: Online Database Integration

**Objective:** Fetch 3D models directly from the RCSB Protein Data Bank.

- **Actions Taken:**
    - Added a "File" -> "Fetch from PDB" menu action.
    - Implemented a `QInputDialog` to prompt the user for a 4-character PDB ID.
    - Used BioPython's `PDBList` to automatically download the specified PDB file.
    - Added a status bar to provide feedback on the download progress.
    - Loaded the downloaded file into the 3D viewer.
- **Outcome:** Users can seamlessly import models from the PDB without leaving the application.

## Phase 4: User Interaction

**Objective:** Allow users to manipulate the loaded 3D models.

- **Actions Taken:**
    - Implemented a picking mechanism to allow users to select individual atoms by clicking on them. Selected atoms are highlighted.
    - Added a 3D transformation widget (gizmo) that appears when a model is loaded.
    - The transformation widget allows for intuitive translation, rotation, and scaling of the entire molecule.
- **Outcome:** A dynamic and interactive environment where models can be directly manipulated.

## Phase 5: Advanced Tools - Surface Generation & Export

**Objective:** Provide advanced tools for analyzing and exporting molecular data.

- **Actions Taken:**
    - Added a "Tools" menu.
    - Implemented a "Generate Surface" feature that calculates and displays the molecular surface of the loaded protein.
    - Implemented an "Export Surface" feature that allows the user to save the generated surface as an `.stl` file, suitable for use in other 3D software or for 3D printing.
- **Outcome:** Users can perform basic molecular analysis and export the results for external use.

## Phase 6: Scene & Data Management

**Objective:** Enable the management of multiple objects within the 3D scene.

- **Actions Taken:**
    - Added a "Scene Manager" panel to the right side of the application window.
    - Refactored the code to use a `Protein` class, encapsulating all data related to a single model.
    - Implemented a `scene_objects` dictionary to store and manage all loaded proteins and surfaces.
    - The Scene Manager lists all loaded objects. Users can select an object from the list to interact with it.
    - Added a "Delete Selected" button to remove objects from the scene.
- **Outcome:** The application is now a multi-object environment, allowing for the creation of complex scenes with multiple interacting molecules.
