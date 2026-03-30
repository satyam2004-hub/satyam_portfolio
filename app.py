from flask import Flask, render_template

app = Flask(__name__)

portfolio_data = {
    "name": "Satyam Sapkota",
    "tagline": "IT Graduate · Game Developer · Full Stack Developer",
    "location": "Bhaktapur, Kathmandu, Nepal",
    "email": "satyam1sapkota@gmail.com",
    "phone": "9742870682",
    "social": {
        "instagram": "https://www.instagram.com/satyam__sapkota/?hl=en",
        "facebook": "https://www.facebook.com/satyam.sapkota.92",
        "linkedin": "https://www.linkedin.com/in/satyam-sapkota-259022358/",
        "github": "https://github.com/satyam2004-hub",
    },
    "about": (
        "Motivated and results-driven IT graduate with hands-on experience in "
        "game development, web development, and IoT systems. Passionate about "
        "building innovative software solutions and committed to continuous learning "
        "and delivering high-quality digital products in a collaborative team environment."
    ),
    "education": {
        "degree": "Bachelor of Information Technology (BIT)",
        "duration": "2022 – 2027/28 (Expected)",
        "institution": "Texas College of Management & IT",
        "affiliation": "Affiliated to Lincoln University",
        "location": "Kathmandu, Nepal",
        "cgpa_current": "3.39 / 4.0",
        "cgpa_expected": "3.5 / 4.0",
    },
    "experience": [
        {
            "role": "Game Development Intern",
            "company": "Zuktitech",
            "location": "Kathmandu, Nepal",
            "year": "2023",
            "icon": "🎮",
            "points": [
                "Developed 2D/3D game mechanics and interactive gameplay features using Unity Engine.",
                "Collaborated with the team on game design, scripting in C#, and debugging.",
                "Gained practical experience in game physics, animation, and scene management.",
                "Participated in sprint planning, code reviews, and iterative development cycles.",
            ],
        },
        {
            "role": "PHP Developer Intern",
            "company": "Texas Imagionology",
            "location": "Kathmandu, Nepal",
            "year": "2024",
            "icon": "💻",
            "points": [
                "Developed and maintained PHP-based web applications including a college news portal.",
                "Designed and managed MySQL databases for dynamic content management.",
                "Built responsive front-end interfaces using HTML, CSS, and JavaScript.",
                "Contributed to the full software development lifecycle from planning to deployment.",
            ],
        },
    ],
    "projects": [
        {
            "name": "Online Book Delivery System",
            "tech": "Django / Python",
            "emoji": "📚",
            "desc": "Full-stack web application enabling users to browse, order, and track book deliveries online. Built with Django framework, SQLite database, and responsive HTML/CSS front-end.",
        },
        {
            "name": "Smart Parking System",
            "tech": "Arduino / IoT",
            "emoji": "🅿️",
            "desc": "IoT-based automated smart parking system using ultrasonic sensors and Arduino microcontroller. Real-time parking slot detection and LED indicator system.",
        },
        {
            "name": "Texas News Portal",
            "tech": "PHP / MySQL",
            "emoji": "📰",
            "desc": "College news portal with an admin panel for content management, user authentication, dynamic news categories, and a responsive UI layout.",
        },
        {
            "name": "Portfolio Website",
            "tech": "WordPress",
            "emoji": "🌐",
            "desc": "Designed and deployed a personal portfolio website using WordPress with custom theme customization.",
        },
    ],
    "skills": {
        "Languages & Frameworks": ["Python & Django", "PHP & MySQL", "Flutter", "Unity (C#)", "HTML5 / CSS3 / JS"],
        "Tools & Platforms": ["WordPress CMS", "Git & GitHub", "IoT / Arduino", "MySQL", "SQLite", "REST APIs"],
    },
    "soft_skills": [
        "Effective Communication",
        "Team Collaboration",
        "Problem-Solving",
        "Time Management",
        "Adaptability",
        "Attention to Detail",
    ],
    "languages": [
        {"lang": "Nepali", "level": "Native"},
        {"lang": "English", "level": "Professional"},
    ],
}


@app.route("/")
def index():
    return render_template("index.html", data=portfolio_data)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
