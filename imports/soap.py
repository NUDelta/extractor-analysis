class SoapNote:
    def __init__(self, date):
        self.date = date
        self.content = {
            'subjective': '',
            'objective': '',
            'assessment': '',
            'plan': ''
        }

    def set_soap_content(self, subjective, objective, assessment, plan):
        self.content['subjective'] = subjective
        self.content['objective'] = objective
        self.content['assessment'] = assessment
        self.content['plan'] = plan

    def get_subjective(self):
        return self.content['subjective']

    def get_objective(self):
        return self.content['objective']

    def get_assessment(self):
        return self.content['assessment']

    def get_plan(self):
        return self.content['plan']