
import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QFileDialog, 
    QInputDialog, QMessageBox, QListWidget, QPushButton, QHBoxLayout, QDockWidget
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
from pyvistaqt.qt_interactor import QtInteractor
import pyvista as pv
from Bio.PDB import PDBParser, PDBList

class Protein:
    def __init__(self, structure, name):
        self.structure = structure
        self.name = name
        self.atoms = pv.MultiBlock()
        self.actor = None
        self.surface = None

        for model in self.structure:
            for chain in model:
                for residue in chain:
                    for atom in residue:
                        sphere = pv.Sphere(center=atom.coord, radius=0.5)
                        self.atoms.append(sphere)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BioVis-3D")
        self.setGeometry(100, 100, 1600, 900)

        self.scene_objects = {}

        # Set up the menu bar
        self._setup_menus()

        # Main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Set up the PyVista plotter
        self.plotter = QtInteractor(self)
        main_layout.addWidget(self.plotter.interactor, 5)

        # Scene Manager
        self._setup_scene_manager()

        # Set up the status bar
        self.statusBar().showMessage("Ready")

        self.plotter.add_axes()
        self.plotter.camera_position = 'xy'

    def _setup_menus(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        tools_menu = menu_bar.addMenu("&Tools")

        open_action = QAction("&Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        fetch_action = QAction("&Fetch from PDB", self)
        fetch_action.triggered.connect(self.fetch_pdb)
        file_menu.addAction(fetch_action)

        surface_action = QAction("&Generate Surface", self)
        surface_action.triggered.connect(self.generate_surface)
        tools_menu.addAction(surface_action)

        export_surface_action = QAction("&Export Surface", self)
        export_surface_action.triggered.connect(self.export_surface)
        tools_menu.addAction(export_surface_action)

    def _setup_scene_manager(self):
        dock = QDockWidget("Scene Manager", self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)
        
        scene_manager_widget = QWidget()
        dock.setWidget(scene_manager_widget)
        scene_layout = QVBoxLayout(scene_manager_widget)

        self.scene_list = QListWidget()
        self.scene_list.itemClicked.connect(self.on_scene_item_click)
        scene_layout.addWidget(self.scene_list)

        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete_selected_object)
        scene_layout.addWidget(delete_button)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDB File", "", "PDB Files (*.pdb);;All Files (*)")
        if file_name:
            pdb_name = os.path.splitext(os.path.basename(file_name))[0]
            self.load_pdb(file_name, pdb_name)

    def fetch_pdb(self):
        pdb_id, ok = QInputDialog.getText(self, 'Fetch PDB', 'Enter PDB ID:')
        if ok and pdb_id:
            self.statusBar().showMessage(f"Downloading PDB ID: {pdb_id}...")
            pdbl = PDBList()
            try:
                file_path = pdbl.retrieve_pdb_file(pdb_id, pdir=".", file_format="pdb")
                if os.path.exists(file_path):
                    self.load_pdb(file_path, pdb_id)
                    self.statusBar().showMessage(f"Successfully loaded {pdb_id}", 5000)
                else:
                    QMessageBox.warning(self, "Download Failed", f"Could not retrieve PDB file for ID: {pdb_id}")
                    self.statusBar().showMessage("Download failed", 5000)
            except Exception as e:
                QMessageBox.warning(self, "Download Error", f"An error occurred: {e}")
                self.statusBar().showMessage("Download failed", 5000)

    def load_pdb(self, file_path, name):
        parser = PDBParser(QUIET=True)
        try:
            structure = parser.get_structure(name, file_path)
        except Exception as e:
            QMessageBox.warning(self, "File Error", f"Could not parse PDB file: {e}")
            return

        protein = Protein(structure, name)
        protein.actor = self.plotter.add_mesh(protein.atoms, smooth_shading=True)
        self.plotter.add_transform_widget(protein.actor)
        self.scene_objects[name] = protein
        self.scene_list.addItem(name)
        self.plotter.reset_camera()

    def generate_surface(self):
        selected_item = self.scene_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "No Selection", "Please select a protein in the Scene Manager.")
            return

        protein = self.scene_objects[selected_item.text()]
        self.statusBar().showMessage("Generating surface...")
        combined_atoms = protein.atoms.combine()
        surface = combined_atoms.delaunay_3d().extract_surface()
        protein.surface = self.plotter.add_mesh(surface, style='surface', color='grey', opacity=0.5)
        self.statusBar().showMessage("Surface generated.", 5000)

    def export_surface(self):
        selected_item = self.scene_list.currentItem()
        if not selected_item or self.scene_objects[selected_item.text()].surface is None:
            QMessageBox.warning(self, "No Surface", "Please generate a surface for the selected protein first.")
            return

        protein = self.scene_objects[selected_item.text()]
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Surface", f"{protein.name}_surface.stl", "STL Files (*.stl)")
        if file_name:
            protein.surface.save(file_name)
            self.statusBar().showMessage(f"Surface exported to {file_name}", 5000)

    def on_scene_item_click(self, item):
        # Optional: Add highlighting or other interaction here
        pass

    def delete_selected_object(self):
        selected_items = self.scene_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            name = item.text()
            protein = self.scene_objects.pop(name)
            self.plotter.remove_actor(protein.actor)
            if protein.surface:
                self.plotter.remove_actor(protein.surface)
            self.scene_list.takeItem(self.scene_list.row(item))

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
