from flask import Flask, request, render_template_string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Stream and course data
streams = {
    "Science": ["maths", "logic", "scientist", "science", "analytical", "experiments", "structure", "universe", "experimenting", "analyzing"],
    "Commerce": ["business", "market-analysis", "business", "business-economy", "financial", "case-studies", "strategizing", "planning", "strategizing"],
    "Arts": ["history", "creative", "artist", "creativity", "creative-writing", "discussion", "brainstorming", "society", "creating", "improvising"]
}

courses = {
    "Science": [
        {"name": " Introduction to Forensic Science (Coursera)", "link": "https://www.coursera.org/learn/forensic-science"},
        {"name": " Introduction to Genetics and Evolution (Coursera)", "link": "https://www.coursera.org/learn/genetics-evolution"},
        {"name": " Data Analytics (Google Garage)", "link": "https://www.coursera.org/google-certificates/advanced-data-analytics-certificate?"}
    ],
    "Commerce": [
        {"name": " Fundamentals of Digital Marketing (Google Garage)", "link": "https://learndigital.withgoogle.com/garage"},
        {"name": " Financial Markets (Coursera)", "link": "https://www.coursera.org/learn/understanding-financial-markets?"},
        {"name": " Business Foundations (Coursera)", "link": "https://www.coursera.org/specializations/wharton-business-foundations?"}
    ],
    "Arts": [
        {"name": " Creative Writing Specialization (Coursera)", "link": "https://www.coursera.org/specializations/creative-writing?"},
        {"name": " Art and Design Fundamentals (Google Garage)", "link": "https://learndigital.withgoogle.com/garage"},
        {"name": " Teaching with Arts (Coursera)", "link": "https://www.coursera.org/specializations/teaching-with-art"}
    ]
}

# HTML template for the result page
result_template = """

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Career Vision - Result</title>

  <!-- Font Awesome for stream icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

  <style>
    /* ---- Reset & Base ---- */
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      color: #333;
    }

    /* ---- Navbar ---- */
    .navbar {
      display: flex;
      align-items: center;
      background-color: #4a235a;
      padding: 15px 30px;
    }
    .navbar-brand {
      display: flex;
      align-items: center;
      text-decoration: none;
    }
    .navbar-brand .logo {
      height: 50px;
      width: auto;
      margin-right: 12px;
    }
    .navbar-brand .fancy-text {
      font-family: "Copperplate", "Papyrus", "Brush Script MT", cursive;
      font-size: 28px;
      font-weight: bold;
      color: #fff;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    /* ---- Container ---- */
    .container {
      max-width: 900px;
      margin: 50px auto;
      background: #fff;
      padding: 40px 20px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      text-align: center;
    }
    h1 { color: #7d3c98; margin-bottom: 30px; }

    /* ---- Stream Card ---- */
    .stream-card {
      background: #f4eaf5;
      padding: 30px;
      border-radius: 10px;
      text-align: left;
      margin-bottom: 40px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .stream-title {
      font-size: 1.8em;
      font-weight: bold;
      color: #7d3c98;
      margin-bottom: 15px;
    }

    /* ---- Lists ---- */
    ul {
      list-style: none;
      padding-left: 0;
      margin-bottom: 30px;
      text-align: left;
    }
    ul li {
      padding-left: 25px;
      margin: 10px 0;
      background: #f4eaf5;
      border-radius: 5px;
      font-size: 1.1em;
      line-height: 1.4;
    }

    /* ---- Course Links ---- */
    .course-list a {
      text-decoration: none;
      color: #4a235a;
      font-weight: bold;
    }
    .course-list a:hover {
      color: #7d3c98;
    }

    /* ---- Career Block ---- */
    .career-course-block {
      background: #f4eaf5;
      color: #4a235a;
      padding: 30px;
      border-radius: 10px;
      margin-bottom: 40px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      text-align: left;
    }
    .career-course-block h2 {
      margin-bottom: 20px;
      font-size: 1.8em;
    }
    .career-course-block ul {
      padding-left: 20px;
    }
    .career-course-block ul li {
      background: transparent;
      font-size: 1.2em;
      line-height: 1.4;
    }
  </style>
</head>

<body>

  <!-- NAVBAR -->
  <nav class="navbar">
    <a href="/" class="navbar-brand">
      <img src="{{ url_for('static', filename='logo.png') }}" alt="Career Vision Logo" class="logo">
      <span class="fancy-text">Career Vision</span>
    </a>
  </nav>

  <div class="container">
    <h1>High School Pathway Result</h1>

    <!-- 1. Stream Recommendation -->
    <div class="stream-card">
      <p class="stream-title">
        {% if stream == "Science" %}
          <i class="fas fa-microscope"></i> Science
        {% elif stream == "Commerce" %}
          <i class="fas fa-chart-line"></i> Commerce
        {% else %}
          <i class="fas fa-paint-brush"></i> Arts
        {% endif %}
      </p>
      <p><strong>Why this career stream?</strong></p>
      <ul>
        {% if stream == "Science" %}
          <li>Best for analytical thinkers, problem-solvers, and researchers.</li>
          <li>Opens careers in Engineering, Medicine, and Research.</li>
        {% elif stream == "Commerce" %}
          <li>Ideal for business-minded individuals and financial strategists.</li>
          <li>Leads to careers in Accounting, Banking, and Entrepreneurship.</li>
        {% else %}
          <li>Perfect for creative minds and expressive thinkers.</li>
          <li>Includes careers in Writing, Film, Design, and Journalism.</li>
        {% endif %}
      </ul>
    </div>

    <!-- 2. Suggested Careers -->
    <div class="career-course-block">
      <h2>Suggested Career Paths</h2>
      <ul>
        {% if stream == "Science" %}
          <li>👨‍🔬 Engineer</li>
          <li>🩺 Doctor</li>
          <li>🔬 Research Scientist</li>
        {% elif stream == "Commerce" %}
          <li>📊 Accountant</li>
          <li>🏦 Banker</li>
          <li>🚀 Entrepreneur</li>
        {% else %}
          <li>🎭 Filmmaker</li>
          <li>📖 Writer</li>
          <li>🎨 Graphic Designer</li>
        {% endif %}
      </ul>
    </div>

    <!-- 3. Recommended Courses -->
    <div class="career-course-block">
      <h2>Top Courses for You</h2>
      <ul class="course-list">
        {% for course in courses %}
          <li><a href="{{ course.link }}" target="_blank">{{ course.name }}</a></li>
        {% endfor %}
      </ul>
    </div>

  </div>

</body>
</html>

"""

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.form
    answers = []

    # Collect responses from form
    for key, value in data.items():
        answers.append(value)
        # Combine answers into a single string
    user_input = " ".join(answers)

    # Prepare stream keywords for similarity calculation
    stream_keywords = {stream: " ".join(keywords) for stream, keywords in streams.items()}

    # Calculate similarity using CountVectorizer
    vectorizer = CountVectorizer().fit_transform([user_input] + list(stream_keywords.values()))
    similarity_scores = cosine_similarity(vectorizer[0:1], vectorizer[1:]).flatten()

    # Find the most relevant stream
    max_index = similarity_scores.argmax()
    recommended_stream = list(streams.keys())[max_index]

    # Recommend courses for the stream
    recommended_courses = courses.get(recommended_stream, [])

    # Render the result page
    return render_template_string(result_template, stream=recommended_stream, courses=recommended_courses)

@app.route("/", methods=["GET"])
def home():
    return render_template("indexs.html")



if __name__ == "__main__":
 app.run(debug=True)


