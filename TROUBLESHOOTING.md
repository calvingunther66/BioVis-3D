## BioVis-3D Troubleshooting Guide

### Issue: Application Crashes on Launch / GLSL Errors

**Symptoms:**
- The application terminates unexpectedly shortly after launching.
- The terminal output shows repeated error messages similar to:
  ```
  vtkShaderProgram.cxx:1145   ERR| vtkShaderProgram (0x...): 0:1(10): error: GLSL 1.50 is not supported. Supported versions are: 1.10, 1.20, and 1.00 ES
  vtkOpenGLPolyDataMapper:2662   ERR| vtkOpenGLPolyDataMapper (0x...): Could not set shader program
  ```
- The `biovis_log.txt` file (located in the application's root directory) also contains these GLSL errors.

**Root Cause:**
This issue indicates a compatibility problem with your system's graphics drivers or its OpenGL version. The `pyvista` library, which BioVis-3D uses for 3D rendering, relies on OpenGL. The errors suggest that your current OpenGL version or drivers do not support GLSL (OpenGL Shading Language) version 1.50, which is required by `pyvista`.

**Solution Steps:**
Since this is an environmental issue and not a bug within the BioVis-3D application code, you will need to address your system's graphics configuration. Please try the following steps:

1.  **Update Graphics Drivers:**
    Ensure your system's graphics drivers are up to date. Outdated drivers are a common cause of OpenGL compatibility issues.
    -   **For NVIDIA/AMD users:** Visit the official website of your graphics card manufacturer to download and install the latest drivers.
    -   **For Linux users (general):** You might use your distribution's package manager to update graphics-related packages. For example, on Ubuntu/Debian-based systems, you can try:
        ```bash
        sudo apt update
        sudo apt upgrade
        sudo apt install --reinstall libgl1-mesa-glx libglu1-mesa mesa-utils
        ```

2.  **Verify OpenGL Version:**
    Check your current OpenGL version. `pyvista` typically requires OpenGL 3.2 or higher. You can check your OpenGL version using `glxinfo` (on Linux):
    ```bash
    glxinfo | grep "OpenGL version"
    ```
    If `glxinfo` is not installed, you might need to install `mesa-utils`:
    ```bash
    sudo apt install mesa-utils
    ```

3.  **Install OpenGL Development Libraries (Linux Specific):**
    On some Linux distributions, you might need to explicitly install OpenGL development libraries. These provide the necessary headers and shared libraries for applications to compile and run against OpenGL.
    ```bash
    sudo apt install build-essential libgl1-mesa-dev
    ```

4.  **Consider Virtual Machine Graphics Settings:**
    If you are running BioVis-3D within a virtual machine (e.g., VirtualBox, VMware), ensure that 3D acceleration is enabled in the VM settings and that the guest additions/tools are installed and up to date. Virtual machines often have limited or older OpenGL support by default.

5.  **Consult PyVista/VTK Documentation:**
    For more in-depth troubleshooting related to `pyvista` or `VTK` (which `pyvista` is built upon) and OpenGL compatibility, refer to their official documentation or community forums.

If you continue to experience issues after trying these steps, please provide detailed information about your operating system, graphics card, and the output of the commands mentioned above when seeking further assistance.