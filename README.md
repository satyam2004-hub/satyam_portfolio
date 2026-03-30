# Satyam Sapkota — Portfolio

A personal portfolio website built with **Python (Flask)**.

## Project Structure

```
satyam_portfolio/
├── app.py                    # Flask app & portfolio data
├── requirements.txt          # Python dependencies
├── templates/
│   ├── index.html            # Main HTML template
│   └── icons.html            # SVG social media icons (macros)
└── static/
    ├── css/
    │   └── style.css         # All styles
    └── js/
        └── main.js           # Scroll animations & nav
```

## Setup in VS Code

1. Open VS Code and open this folder:
   ```
   File > Open Folder > select satyam_portfolio
   ```

2. Open the terminal in VS Code (`Ctrl + \``) and run:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open your browser at: **http://localhost:5000**

## Customize

- Edit your info, social links, projects in `app.py` under `portfolio_data`
- Change colors/fonts in `static/css/style.css`
- Update social media URLs in `app.py` under the `"social"` key
