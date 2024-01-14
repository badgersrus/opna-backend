from flask_sqlalchemy import SQLAlchemy
from app import risk_profile_hierarchy

db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    project_type = db.Column(db.String)
    carbon_reduction_potential = db.Column(db.Float)
    cost_effectiveness = db.Column(db.Float)
    financial_returns = db.Column(db.Float)
    risk_profile = db.Column(db.String)
    project_lifespan = db.Column(db.Integer)
    environmental_impact = db.Column(db.String)
    management_team_expertise = db.Column(db.String)
    mrv_transaparency = db.Column(db.String)



def find_projects_by_preferences(preferences):
    query = Project.query

    # range filter
    if 'carbonReductionPotential' in preferences:
        range_prefs = preferences['carbonReductionPotential']
        if 'min' in range_prefs:
            query = query.filter(Project.carbon_reduction_potential >= range_prefs['min'])
        if 'max' in range_prefs:
            query = query.filter(Project.carbon_reduction_potential <= range_prefs['max'])

    # filtering based on exact match 
    if 'projectType' in preferences:
        query = query.filter(Project.project_type == preferences['projectType'])

    # filtering based on hierarchy
    if 'riskProfile' in preferences:
        acceptable_risks = [risk for risk, level in risk_profile_hierarchy.items() if level <= risk_profile_hierarchy[preferences['riskProfile']]]
        query = query.filter(Project.risk_profile.in_(acceptable_risks))

    if 'costEffectiveness' in preferences:
        query = query.filter(Project.cost_effectiveness >= preferences['costEffectiveness'])
        
    # blah blah blah

    projects = query.all()

    return projects