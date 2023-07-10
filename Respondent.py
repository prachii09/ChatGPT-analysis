class Respondent:
    timestamp: str = ""
    '''Timestamp'''
    
    age: int = 18
    '''Q1 What is your age?'''

    program: str = ""
    '''Q2 What Occupation (Program) are you in?'''

    studyYear: int = 1
    '''Q3 Year of study?'''

    gender: str = ""
    '''Q4 To which gender do you most identify? (Optional)'''

    culturalBackground: str = ""
    '''Q5 What is your cultural background? (Optional)'''

    knewChatGPT: bool = False
    '''Q6 Did you know what ChatGPT was before this survey?'''

    triedChatGPT: bool = False
    '''Q7 Have you ever tried using ChatGPT before?'''

    chatGPTUses: list[str] = []
    '''Q8 What do use ChatGPT for? (Select all that Apply)'''

    chatGPTUsageFrequency: int = 0
    '''Q9 How often have you used ChatGPT?'''

    trustsAccuracy: bool = False
    '''Q10 Do you believe that ChatGPT provides accurate and reliable information?'''

    believesChatGptIsCheating: bool = False
    '''Q11 Do you think using ChatGPT to complete academic assignments is a form of cheating?'''

    wantsUniversityGuidelines: bool = False
    '''Q12 Would you like your university to provide guidelines on the appropriate use of ChatGPT in academic work?'''

    believesChatGptIsBeneficial: bool = False
    '''Q13 Do you think the use of ChatGPT in academic work is beneficial to students' learning?'''

    wantsLegalForResearchOnly: bool = False
    '''Q14 Should universities allow the use of ChatGPT for research purposes only?'''

    wantsLegalForAcademicWriting: bool = False
    '''Q15 Should universities allow the use of ChatGPT for academic writing assignments?'''

    wantsRegulationOrMonitoring: bool = False
    '''Q16 Do you believe that the use of ChatGPT should be regulated or monitored by universities?'''

    recommendsChatGpt: bool = False
    '''Q17 Would you recommend the use of ChatGPT to other students for academic purposes?'''

    
    def __init__(self, row: list[str]):
        ''' Create a new respondent from csv row '''
        self.timestamp = row[0]
        self.age = int(row[1])
        self.program = row[2]
        self.studyYear = int(row[3])
        self.gender = row[4]
        self.culturalBackground = row[5]
        self.knewChatGPT = row[6] == "Yes"
        self.triedChatGPT = row[7] == "Yes"
        self.chatGPTUses = row[8].split(", ")
        self.chatGPTUsageFrequency = int(row[9])
        self.trustsAccuracy = row[10] == "Yes"
        self.believesChatGptIsCheating = row[11] == "Yes"
        self.wantsUniversityGuidelines = row[12] == "Yes"
        self.believesChatGptIsBeneficial = row[13] == "Yes"
        self.wantsLegalForResearchOnly = row[14] == "Yes"
        self.wantsLegalForAcademicWriting = row[15] == "Yes"
        self.wantsRegulationOrMonitoring = row[16] == "Yes"
        self.recommendsChatGpt = row[17] == "Yes"


