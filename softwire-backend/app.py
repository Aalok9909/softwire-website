from flask import Flask, jsonify, request
from flask_cors import CORS
from config import get_db_connection   
app = Flask(__name__)
CORS(app)

# API: Company Info
@app.route("/api/company-info", methods=["GET"])

@app.route("/")
def home():
    return jsonify({"message": "Softwire Backend is Running Successfully!"})

def company_info():
    data = {
        "name": "Softwire Technologies",
        "email": "contact@softwire.com",
        "phone": "+44 123 456 7890",
        "address": "London, UK",
        "services": [
            "Custom Software Development",
            "AI & ML Solutions",
            "Web & Mobile Applications",
            "Cloud Solutions & DevOps"
        ]
    }
    return jsonify(data)

# API: Contact Form (Saves in MySQL)
@app.route("/api/contact", methods=["POST"])
def contact_form():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, message))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
            "message": f"Thank you {name}! Your message has been saved to the database.",
            "status": "success"
        })

    except Exception as e:
        print("DB Error:", e)
        return jsonify({
            "message": "Error saving message.",
            "status": "error"
        }), 500


# API: Services
@app.route("/api/services", methods=["GET"])
def get_services():
    services = [
        {"title": "Custom Software Development", "desc": "Tailor-made solutions for your business."},
        {"title": "AI & ML Solutions", "desc": "Intelligent systems to optimize operations."},
        {"title": "Web & Mobile Applications", "desc": "Beautiful, responsive, and fast applications."},
        {"title": "Cloud Solutions & DevOps", "desc": "Seamless cloud integration and deployment."}
    ]
    return jsonify(services)

if __name__ == "__main__":
    app.run(debug=True)
