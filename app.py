import json
import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from projects import projects

app = Flask(__name__) 
CORS(app)


@app.route("/match", methods=['POST'])
def match_projects():
    customer_preferences = request.json

    if not customer_preferences or not isinstance(customer_preferences, dict):
        return jsonify({"error": "Invalid input, preferences must be a dictionary"}), 400
    
    # projects = Project.query.all()

    matched_projects = match_projects_to_preferences(projects, customer_preferences)

    formatted_results_short = [project.serialize(score=score) for project, score in matched_projects]

    return jsonify(formatted_results_short)

@app.route("/projects")
def get_projects():
    projects_dict = [project.to_dict(score=0) for project in projects]
    return jsonify(projects_dict)

def match_projects_to_preferences(projects, preferences):

    scored_projects = [(project, calculate_score(project, preferences)) for project in projects]
    
    filtered_projects = [project for project in scored_projects if project[1] > 0]

    return sorted(filtered_projects, key=lambda x: x[1], reverse=True)


# def calculate_score(project, preferences, weights):
def calculate_score(project, preferences):
    weight_value = 1 / len(preferences)
    score = 0
    hierarchy_functions = {
        'riskProfile': risk_profile_hierarchy,
        'managementTeamExpertise': management_profile_hierarchy,
        'mrvTransparency': mrv_transparency
    }

    for key, value in preferences.items():
        camel_key = get_camel_key(key)
        project_value = getattr(project, camel_key, None)

        if project_value is None:
            continue

        # range params
        if isinstance(value, dict):
           min_val = value.get('min')
           max_val = value.get('max')   
           if min_val is not None and max_val is not None and min_val <= project_value <= max_val:
                   score += weight_value
           elif min_val is not None and project_value >= min_val:
                   score += weight_value
           elif max_val is not None and project_value <= max_val:
                   score += weight_value

        # support if we want to allow multi select
        elif isinstance(value, list) and project_value in value:
            score += weight_value

        # any of the low/ medium/ high comparisons
        elif key in hierarchy_functions:
            project_level, preferred_level = calculate_hierarchy_score(project_value, value, hierarchy_functions[key])

            is_risk_profile_satisfied = key == 'riskProfile' and project_level <= preferred_level
            is_other_hierarchy_satisfied = key in ['managementTeamExpertise', 'mrvTransparency'] and project_level >= preferred_level

            if is_risk_profile_satisfied or is_other_hierarchy_satisfied:
                score += weight_value
        
        # project type
        elif project_value == value:
            score += weight_value

    return round(score * 100, 0)

risk_profile_hierarchy = {
    'Low': 1,
    'Medium': 2,
    'High': 3
}

management_profile_hierarchy = {
    'Low': 1,
    'Medium': 2,
    'High': 3,
    'Expert': 4
}

mrv_transparency = {
    'Low': 1,
    'Medium': 2,
    'High': 3,
}

def calculate_hierarchy_score(project_value, preference_value, hierarchy):
    project_level = hierarchy.get(project_value, 0)
    preferred_level = hierarchy.get(preference_value, 0)
    return project_level, preferred_level

def get_camel_key(key):
    return re.compile(r'([A-Z])').sub(lambda x: '_' + x.group(1).lower(), key)

if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True)
