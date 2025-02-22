# Recipe Browser

A Streamlit application that allows users to browse recipes for breakfast, lunch, and dinner while filtering out recipes containing specific allergens.

## Features
- Browse recipes by meal type (breakfast, lunch, dinner)
- Filter recipes by 7 common allergens
- Expandable recipe cards with ingredients and instructions
- Clear allergen labeling

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate  # On Unix or MacOS
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Installation

1. Run the application:
```bash
streamlit run app.py
```

## Usage
1. Select a meal type from the dropdown menu
2. Use the sidebar to filter out recipes containing specific allergens
3. Click on recipe cards to view details
