from flask import Flask, request, render_template_string

app = Flask(__name__)

# RESULT TEMPLATE (your HTML + CSS goes here)
result_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Career Vision - Result</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .navbar {
            background-color: #4a235a;
            padding: 10px 20px;
            display: flex;
            align-items: center;
        }
        .navbar img {
            height: 40px;
            margin-right: 15px;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            font-size: 1.8em;
            font-weight: bold;
            font-family: "Copperplate", "Papyrus", "Brush Script MT", cursive;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .container {
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: white;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            text-align: center;
        }
        h1 {
            color: #7d3c98;
        }
        .stream-card {
            background: #f4eaf5;
            padding: 20px;
            border-radius: 10px;
            text-align: left;
            margin-top: 20px;
        }
        .stream-title {
            font-size: 1.5em;
            font-weight: bold;
            color: #7d3c98;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        ul li {
            margin: 10px 0;
            padding: 10px;
            background: #f4eaf5;
            border-radius: 5px;
            font-size: 1.1em;
        }
        ul li::before {
            content: "→ ";
            font-weight: bold;
            color: #7d3c98;
        }
        a {
            text-decoration: none;
            color: #4a235a;
            font-weight: bold;
        }
        a:hover {
            color: #7d3c98;
        }
        .back-button {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 25px;
            background-color: #7d3c98;
            color: white;
            text-decoration: none;
            font-size: 1.1em;
            border-radius: 5px;
        }
        .back-button:hover {
            background-color: #4a235a;
        }
    </style>
</head>
<body>

    <div class="navbar">
        <img src="{{ url_for('static', filename='logo.png') }}" alt="logo">
        <a href="/" class="fancy-text">Career Vision</a>
    </div>

    <div class="container">
        <h1>Undergraduate Pathway Result</h1>

        <div class="stream-card">
            <p class="stream-title">🎓 Careers/Degrees You Can Pursue:</p>
            <ul>
                {% for career in careers %}
                    <li>{{ career }}</li>
                {% endfor %}
            </ul>
        </div>

        <div class="stream-card">
            <p class="stream-title">📝 Why is this the correct path for you?</p>
            <p>{{ reason }}</p>
        </div>

        <div class="stream-card">
            <p class="stream-title">📚 Online Courses You Can Take:</p>
            <ul>
                {% for course in courses %}
                    <li><a href="{{ course.link }}" target="_blank">{{ course.name }}</a></li>
                {% endfor %}
            </ul>
        </div>

    </div>

</body>
</html>

"""

@app.route('/')
def home():
    return "<h2>Career Recommendation Backend is Running!</h2>"

@app.route('/recommend', methods=['POST'])
def recommend():
    stream = request.form.get('stream')
    careers = []
    courses = []
    reasons = []

    if stream == 'science':
        math_bio = request.form.get('mathBio')
        tech_prog = request.form.get('techProg')
        healthcare = request.form.get('healthcare')

        if tech_prog == 'yes':
            careers.append("Software Developer (B.Sc. IT, B.Tech in Computer Science)")
            courses.extend([
                {"name": "Complete Python Bootcamp (Udemy)", "link": "https://www.udemy.com/course/complete-python-bootcamp/"},
                {"name": "IBM Data Science Professional Certificate (Coursera)", "link": "https://www.coursera.org/professional-certificates/ibm-data-science"}
            ])
            reasons.append("Engineering in IT because you are interested in technology and programming.")
        
        if math_bio == 'yes':
            careers.append("Bioinformatician,Epidemiologist (B.Sc. Biostatistics,B.Sc. Bioinformatics)")
            courses.extend([
                {"name": "Biostatistics in Public Health(Coursera)", "link": "https://www.coursera.org/specializations/biostatistics-public-health"},
           {"name": "Introduction to Epidemiology(Udemy)", "link":"https://www.udemy.com/course/introduction-to-epidemiology/"}] )
            reasons.append("You are interested in Maths and Bio.") 

        if healthcare == 'yes':
            careers.append("Medical Lab Technician (B.Sc. Medical Laboratory Technology)")
            courses.extend([
                {"name": "Essentials of Medical Laboratory Science (Udemy)", "link": "https://www.udemy.com/course/medical-laboratory-technician/"},
           {"name": "Human Physiology(Coursera)", "link":"https://www.coursera.org/learn/physiology"}] )
            reasons.append("You are interested in healthcare and helping people.")

        if not careers:
            careers.append("General Science Graduate")
            courses.append({"name": "Introduction to Data Science (Coursera)", "link": "https://www.coursera.org/specializations/jhu-data-science"})
            reasons.append("You can explore a variety of science-related fields.")

    elif stream == 'commerce':
        business_interest = request.form.get('businessInterest')
        finance = request.form.get('finance')
        marketing = request.form.get('marketing')

        if business_interest == 'yes':
            careers.append("Entrepreneur (BMS, BBA, MBA)")
            courses.extend([
                {"name": "Entrepreneurship Specialization (Coursera)", "link": "https://www.coursera.org/specializations/wharton-entrepreneurship"},
                {"name": "How to Build a Startup (Udemy)", "link": "https://www.udemy.com/course/buildstartup/"}
            ])
            reasons.append("You can pursue an entrepreneurial career, managing your own business.")

        if finance == 'yes':
            careers.append("Financial Analyst (B.Com, BAF, MBA in Finance)")
            courses.extend([
                {"name": "Financial Analysis for Startups (Udemy)", "link": "https://www.udemy.com/course/the-complete-financial-analyst-course"},
                {"name": "Financial Market (Coursera)", "link": "https://www.coursera.org/learn/financial-markets-global"}
            ])
            reasons.append("Finance careers like Financial Analyst match your interest in numbers and finance.")

        if marketing == 'yes':
            careers.append("Marketing Manager (BMS, MBA in Marketing)")
            courses.extend([
                {"name": "Digital Marketing Masterclass (Udemy)", "link": "https://www.udemy.com/course/digital-marketing-masterclass/"},
                {"name": "Marketing Analytics (Coursera)", "link": "https://www.coursera.org/specializations/marketing-analytics"}
            ])
            reasons.append("You can pursue a career in marketing, utilizing your interest in marketing and advertising.")

        if not careers:
            careers.append("General Commerce Professional")
            courses.append({"name": "Introduction to Business (Coursera)", "link": "https://www.coursera.org/learn/wharton-business-foundations"})
            reasons.append("General commerce degrees such as B.Com or BAF are flexible for various career paths.")

    elif stream == 'arts':
        arts_culture = request.form.get('artsCulture')
        media_entertainment = request.form.get('mediaEntertainment')
        creative_industries = request.form.get('creativeIndustries')

        if arts_culture == 'yes':
            careers.append("Artist / Cultural Manager (BA in Arts, BA in Cultural Studies)")
            courses.append({"name": "Art & Heritage Management (Udemy)", "link": "https://www.udemy.com/course/art-gallery-exhibition-curating-and-artist-management/"})
            reasons.append("A career in art and culture fits well with your interests in cultural heritage.")

        if media_entertainment == 'yes':
            careers.append("Content Creator (BFA, BA in Media Studies)")
            courses.append({"name": "Social Media Content Strategy (Coursera)", "link": "https://www.coursera.org/learn/social-media-content-and-strategy"})
            reasons.append("You can pursue a career in media and entertainment, leveraging your creative skills.")

        if creative_industries == 'yes':
            careers.append("Graphic Designer (BFA, B.Des in Graphic Design)")
            courses.append({"name": "Graphic Design Masterclass (Udemy)", "link": "https://www.udemy.com/course/graphic-design-masterclass/"})
            reasons.append("You can pursue a career in design, fitting your creative interests.")

        if not careers:
            careers.append("General Arts Professional")
            courses.append({"name": "Introduction to Communication (Coursera)", "link": "https://www.coursera.org/learn/communication-skills"})
            reasons.append("Arts professionals can explore various fields like teaching, writing, or cultural management.")

    else:
        return "Invalid stream selected!"

    final_reason = " ".join(reasons) if reasons else "Explore a variety of fields based on your broad interests."

    return render_template_string(result_template, careers=careers, courses=courses, reason=final_reason)

if __name__ == '__main__':
    app.run(debug=True)
