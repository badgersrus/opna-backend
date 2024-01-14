class Project:
    def __init__(self, project_type, carbon_reduction_potential, cost_effectiveness, financial_returns, risk_profile, project_lifespan, environmental_impact, management_team_expertise, mrv_transaparency):
        self.project_type = project_type 
        self.carbon_reduction_potential = carbon_reduction_potential  # float (tons of CO2 equivalent)
        self.cost_effectiveness = cost_effectiveness  # float (cost per ton of carbon reduced/removed)
        self.financial_returns = financial_returns  # float (expected ROI percentage)
        self.risk_profile = risk_profile  # String (low/med/high rating)
        self.project_lifespan = project_lifespan  # Integer (years)
        self.environmental_impact = environmental_impact  # String (low/med/high rating)
        self.management_team_expertise = management_team_expertise  # String (low/med/high/expert rating)
        self.mrv_transaparency = mrv_transaparency  # String (low/med/high quality of transparnecy rating)
    
        def serialize(self, score=0):
            serialized_data = {self._to_camel_case(key): value for key, value in vars(self).items()}
            if score > 0 :
                serialized_data['score'] = score
            return serialized_data

        @staticmethod
        def _to_camel_case(snake_str):
            components = snake_str.split('_')
            return components[0] + ''.join(x.title() for x in components[1:])



# example projects
project1 = Project(
    project_type="Reforestation",
    carbon_reduction_potential=60000.0,
    cost_effectiveness=200.0,
    financial_returns=1.2,
    risk_profile="Low",
    project_lifespan=30,
    environmental_impact="Medium",
    management_team_expertise="Expert",
    mrv_transaparency="High"
)

project2 = Project(
    project_type="Renewable Energy",
    carbon_reduction_potential=35000.0,
    cost_effectiveness=400.0,
    financial_returns=3.1,
    risk_profile="High",
    project_lifespan=25,
    environmental_impact="Medium",
    management_team_expertise="High",
    mrv_transaparency="High"
)

project3 = Project(
    project_type="Direct Air Capture",
    carbon_reduction_potential=10000.0,
    cost_effectiveness=350.0,
    project_lifespan=25,
    financial_returns=2.5,
    risk_profile="High",
    environmental_impact="High",
    management_team_expertise="Expert",
    mrv_transaparency="High"
)

project4 = Project(
    project_type="Renewable Energy",
    carbon_reduction_potential=20000.0,
    cost_effectiveness=350.0,
    financial_returns=1.4,
    risk_profile="Medium",
    project_lifespan=20,
    environmental_impact="High",
    management_team_expertise="Medium",
    mrv_transaparency="Low"
)

project5 = Project(
    project_type="EV Infrastructure",
    carbon_reduction_potential=14000.0,
    cost_effectiveness=450.0,
    financial_returns=1.9,
    risk_profile="Low",
    project_lifespan=10,
    environmental_impact="Low",
    management_team_expertise="Low",
    mrv_transaparency="Medium"
)

project6 = Project(
    project_type="Methane Capture",
    carbon_reduction_potential=9000.0,
    cost_effectiveness=250.0,
    financial_returns=2.2,
    risk_profile="Medium",
    project_lifespan=12,
    environmental_impact="High",
    management_team_expertise="Medium",
    mrv_transaparency="Low"
)

project7 = Project(
    project_type="Carbon Farming",
    carbon_reduction_potential=45000.0,
    cost_effectiveness=300.0,
    financial_returns=1.5,
    risk_profile="Low",
    project_lifespan=15,
    environmental_impact="Medium",
    management_team_expertise="High",
    mrv_transaparency="Medium"
)

project8 = Project(
    project_type="EV Infrastructure",
    carbon_reduction_potential=56000.0,
    cost_effectiveness=500.0,
    financial_returns=2.0,
    risk_profile="Medium",
    project_lifespan=20,
    environmental_impact="Low",
    management_team_expertise="Expert",
    mrv_transaparency="High"
)

project9 = Project(
    project_type="Carbon Farming",
    carbon_reduction_potential=35000.0,
    cost_effectiveness=400.0,
    financial_returns=3.0,
    risk_profile="High",
    project_lifespan=30,
    environmental_impact="High",
    management_team_expertise="Medium",
    mrv_transaparency="Low"
)

project10 = Project(
    project_type="Direct Air Capture",
    carbon_reduction_potential=9000.0,
    cost_effectiveness=45.0,
    financial_returns=2.3,
    risk_profile="Medium",
    project_lifespan=25,
    environmental_impact="Medium",
    management_team_expertise="Low",
    mrv_transaparency="Low"
)

project11 = Project(
    project_type="Reforestation",
    carbon_reduction_potential=75000.0,
    cost_effectiveness=150.0,
    financial_returns=1.7,
    risk_profile="Low",
    project_lifespan=35,
    environmental_impact="Low",
    management_team_expertise="High",
    mrv_transaparency="Low"
)

project12 = Project(
    project_type="Methane Capture",
    carbon_reduction_potential=12000.0,
    cost_effectiveness=30.0,
    financial_returns=2.1,
    risk_profile="Low",
    project_lifespan=20,
    environmental_impact="Medium",
    management_team_expertise="Expert",
    mrv_transaparency="High"
)

project13 = Project(
    project_type="Carbon Farming",
    carbon_reduction_potential=12000.0,
    cost_effectiveness=350.0,
    financial_returns=1.8,
    risk_profile="Medium",
    project_lifespan=25,
    environmental_impact="High",
    management_team_expertise="Medium",
    mrv_transaparency="High"
)

project14 = Project(
    project_type="Renewable Energy",
    carbon_reduction_potential=24000.0,
    cost_effectiveness=200.0,
    financial_returns=2.4,
    risk_profile="High",
    project_lifespan=30,
    environmental_impact="Medium",
    management_team_expertise="Low",
    mrv_transaparency="Medium"
)

project15 = Project(
    project_type="Carbon Farming",
    carbon_reduction_potential=6000.0,
    cost_effectiveness=250.0,
    financial_returns=1.6,
    risk_profile="Low",
    project_lifespan=18,
    environmental_impact="Low",
    management_team_expertise="High",
    mrv_transaparency="Low"
)

project16 = Project(
    project_type="Renewable Energy",
    carbon_reduction_potential=95000.0,
    cost_effectiveness=700.0,
    financial_returns=3.5,
    risk_profile="High",
    project_lifespan=40,
    environmental_impact="High",
    management_team_expertise="Expert",
    mrv_transaparency="Low"
)

projects=[project1, project2, project3, project4, project5, project6, project7, project8, project9, project10, project11, project12, project13, project14, project15, project16]
