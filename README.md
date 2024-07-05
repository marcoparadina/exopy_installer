# Requirements

Python 3.4 or later.

# Installation

To install exopy using this installer follow these steps: 

1. Create a virtual environment

    In the directory where you want to install exopy run this command in the teminal:

     ```bash
     python -m venv exopy_env
     ```

1. Activate the virtual environment

    In the same directory as above, in the terminal, run this command:

    - On Windows
        ```bash
        .\exopy_env\Scripts\activate
        ```
    - On Mac\Linux
        ```bash
        source exopy_env\bin\activate
        ```

1. Run the installer

    In the terminal move into the installer repository, and then run the exopy installer.

    ```bash
    cd exopy_installer
    python exopy_installer.py
    ```
    Exopy is now installed. 

1. Launch exopy
    
    Run this command in the terminal to launch exopy

    ```bash
    exopy
    ```

    The first time you launch exopy, a banner will ask you where you want to save the application settings file. Do not close this banner without choosing a diretory, you might break everything and  have to restart the install from the beginning.

----------------------------------GOOD VERSION--------------------------------------

1. Clone the installer repo

    In the directory where you want to install exopy, run this command in the terminal:

    ```bash
        git clone "https://github.com/marcoparadina/exopy_installer.git"
    ```

1. Install exopy

    ```bash
    cd exopy_installer
    python install_exopy.py

1. Launch exopy
    
    Run this command in the terminal to launch exopy

    ```bash
    exopy
    ```

    The first time you launch exopy, a banner will ask you where you want to save the application settings file. Do not close this banner without choosing a diretory, you might break everything and  have to restart the install from the beginning.
-----------------------------------------------------------------

## Using exopy

After you've installed exopy using the instructions above, to use it do the following: 

1. Activate the virtual environment

    Navigate to the directory that contains your "exopy_env" directory. Then open a terminal in that directory and activate the exopy virtual environment with this terminl command:

    - On Windows
        ```bash
        .\exopy_env\Scripts\activate
        ```
    - On Mac\Linux
        ```bash
        source exopy_env\bin\activate
        ```
1. Launch exopy

    In the same terminal, once the virtual environment is activated, run this command to launch exopy:

    ```bash
    exopy
    ```
