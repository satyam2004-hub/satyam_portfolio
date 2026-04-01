# Satyam Sapkota — Portfolio

A modern, responsive personal portfolio website built with **Python (Flask)** featuring a dark theme design with smooth animations and mobile-first approach.

🌐 **Live Demo:** [View Portfolio](#) *(Update with your Render URL)*

## ✨ Features

- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **Mobile Hamburger Menu** - Full-screen navigation for mobile devices
- **Loading Screen** - Smooth loading animation on page load
- **Scroll-to-Top Button** - Easy navigation back to top
- **SEO Optimized** - Meta tags for better search engine visibility
- **Social Media Integration** - Links to Instagram, Facebook, LinkedIn, GitHub
- **Project Links** - Live demo and source code links for each project
- **Download Resume** - Direct link to download/view resume
- **Smooth Animations** - Fade-in effects and hover animations
- **Dark Theme** - Modern dark color scheme with gradient accents

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Fonts:** Syne, Space Mono (Google Fonts)
- **Deployment:** Render

## 📁 Project Structure

```
satyam_portfolio/
├── app.py                    # Flask app & portfolio data
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── templates/
│   ├── index.html            # Main HTML template
│   └── icons.html            # SVG icons (macros)
└── static/
    ├── css/
    │   └── style.css         # All styles
    └── js/
        └── main.js           # Interactions & animations
```

## 🚀 Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/satyam2004-hub/satyam_portfolio.git
   cd satyam_portfolio
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On Mac/Linux: source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   - Navigate to: `http://localhost:8000`

## 📝 Customization Guide

### 1. Update Personal Information

Edit `app.py` and modify the `portfolio_data` dictionary:

```python
portfolio_data = {
    "name": "Your Name",
    "tagline": "Your Tagline",
    "location": "Your Location",
    "email": "your.email@example.com",
    "phone": "Your Phone Number",
    "resume_url": "https://your-resume-link.com",  # Google Drive or direct link
    "social": {
        "instagram": "https://instagram.com/yourprofile",
        "facebook": "https://facebook.com/yourprofile",
        "linkedin": "https://linkedin.com/in/yourprofile",
        "github": "https://github.com/yourusername",
    },
    # ... rest of the data
}
```

### 2. Add Project Links

Update each project in `app.py` with live demo and repository URLs:

```python
{
    "name": "Project Name",
    "tech": "Tech Stack",
    "emoji": "🚀",
    "desc": "Project description...",
    "demo_url": "https://your-project-demo.com",  # Live demo URL
    "repo_url": "https://github.com/yourusername/project",  # GitHub repo
},
```

### 3. Upload Your Resume

1. Upload your resume to Google Drive or any file hosting service
2. Get the shareable link
3. Update `resume_url` in `app.py`

### 4. Customize Colors & Styles

Edit `static/css/style.css` and modify the CSS variables in `:root`:

```css
:root {
  --bg: #0b0e13;        /* Background color */
  --accent: #00e5c0;    /* Primary accent (teal) */
  --accent2: #7c6bff;   /* Secondary accent (purple) */
  --accent3: #ff6b6b;   /* Tertiary accent (coral) */
  /* ... */
}
```

## 🌐 Deployment to Render

1. **Push your code to GitHub** (already connected)
2. **Create a new Web Service on Render:**
   - Connect your GitHub repository
   - Set Build Command: `pip install -r requirements.txt`
   - Set Start Command: `gunicorn app:app`
3. **Deploy!** Render will automatically deploy your site

### Environment Variables (if needed)
- `FLASK_ENV`: Set to `production` for production mode

## 📱 Mobile Navigation

The site includes a full-screen mobile navigation menu that:
- Activates on screens smaller than 768px
- Features a hamburger icon that animates to an X
- Closes when clicking outside the menu or selecting a link
- Prevents body scroll when open

## 🎨 Design Features

- **Grid Background** - Subtle grid pattern in hero section
- **Gradient Glows** - Animated gradient orbs for depth
- **Card Hover Effects** - Cards lift and glow on hover
- **Active Nav Highlight** - Current section highlighted in navigation
- **Scroll Animations** - Elements fade in as you scroll
- **Staggered Delays** - Sequential animation timing for visual flow

## 📄 License

This project is open source and available for personal use. Feel free to fork and customize for your own portfolio!

## 🤝 Contributing

Found a bug or have a feature request? Feel free to open an issue or submit a pull request.

## 📧 Contact

- **Email:** satyam1sapkota@gmail.com
- **LinkedIn:** [linkedin.com/in/satyam-sapkota-259022358](https://www.linkedin.com/in/satyam-sapkota-259022358/)
- **GitHub:** [github.com/satyam2004-hub](https://github.com/satyam2004-hub)

---

Built with ❤️ using Python & Flask