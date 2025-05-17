# restaurant-idea

# How to Run the App

1. In a Visual Studio workspace, add the "Restaurant Idea" folder to your workspace.
2. Make sure you have python installed.
3. Open a PowerShell terminal.
    
    1. Change your directory to your folder

        Example: `cd C:\{PATH}\restaurant-idea\`

    2. Set up a virtual environment
    
        Example: `python venv .venv`
    
    3. Activate your virtual environment.
        
        Example `.\.venv\Scripts\activate`

    4. Install UV, then install the contents in UV.

        Example:
        ```
        pip install uv
        uv pip install .
        ```
    
    5. Run the App. This should open in a browser.

        Example: `uv run streamlit run .\src\WorkWise.py`