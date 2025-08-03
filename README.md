# BioVis-3D

BioVis-3D is an interactive tool for visualizing and manipulating macromolecular structures. It allows users to load 3D models from local files or fetch them directly from the RCSB Protein Data Bank.

## Features

-   Load 3D models from local `.pdb` files.
-   Fetch 3D models directly from the RCSB Protein Data Bank using a PDB ID.
-   Interactive 3D view with picking mechanism to select individual atoms.
-   3D transformation widget (gizmo) for intuitive translation, rotation, and scaling of molecules.
-   Generate and display the molecular surface of a protein.
-   Export the generated surface as an `.stl` file.
-   Scene manager to handle multiple objects in the 3D scene.
-   Optimized rendering for large molecules.

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd BioVis-3D
    ```
3.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
4.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application with the following command:

```bash
python src/main.py
```

## Dependencies

-   `pyvista`
-   `biopython`
-   `pyvistaqt`
-   `PyQt6`