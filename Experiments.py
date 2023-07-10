import Respondent
import matplotlib.pyplot as plt

def experiment1(respondants: list[Respondent.Respondent]):
    '''Do you believe that ChatGPT provides accurate and reliable information? - Frequent vs Infrequent Users'''
    controlGroup: list[Respondent.Respondent] = []
    testGroup: list[Respondent.Respondent] = []

    for respondent in respondants:
        if respondent.chatGPTUsageFrequency <= 2:
            controlGroup.append(respondent)
        else:
            testGroup.append(respondent)
    
    # CONTROL GROUP
    controlGroupTrustsAccuracy: int = sum(respondent.trustsAccuracy for respondent in controlGroup)
    controlGroupTrustsAccuracyPercentage: float = (controlGroupTrustsAccuracy / len(controlGroup)) * 100
    controlGroupDoesNotTrustAccuracyPercentage: float = 100 - controlGroupTrustsAccuracyPercentage

    # Create Pie Chart
    labels = ['Trusts Accuracy', 'Does Not Trust Accuracy']
    title = 'Trust in ChatGPT Accuracy and Reliability Among Less Frequent Users'
    sizes = [controlGroupTrustsAccuracyPercentage, controlGroupDoesNotTrustAccuracyPercentage]
    explode = (0, 0.05)


    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.set_title(title)



    plt.show()

    # TEST GROUP
    testGroupTrustsAccuracy: int = sum(respondent.trustsAccuracy for respondent in testGroup)
    testGroupTrustsAccuracyPercentage: float = (testGroupTrustsAccuracy / len(testGroup)) * 100
    testGroupDoesNotTrustAccuracyPercentage: float = 100 - testGroupTrustsAccuracyPercentage

    # Create Pie Chart
    labels = ['Trusts Accuracy', 'Does Not Trust Accuracy']
    title = 'Trust in ChatGPT Accuracy and Reliability Among Frequent Users'
    sizes = [testGroupTrustsAccuracyPercentage, testGroupDoesNotTrustAccuracyPercentage]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()

def experiment2(respondants: list[Respondent.Respondent]):
    '''Do you think the use of ChatGPT in academic work is beneficial to students' learning? - Frequent vs Infrequent Users'''
    controlGroup: list[Respondent.Respondent] = []
    testGroup: list[Respondent.Respondent] = []

    for respondent in respondants:
        if respondent.chatGPTUsageFrequency <= 2:
            controlGroup.append(respondent)
        else:
            testGroup.append(respondent)

    # CONTROL GROUP
    controlGroupBelievesChatGptIsBeneficial: int = sum(respondent.believesChatGptIsBeneficial for respondent in controlGroup)
    controlGroupBelievesChatGptIsBeneficialPercentage: float = (controlGroupBelievesChatGptIsBeneficial / len(controlGroup)) * 100
    controlGroupDoesNotBelieveChatGptIsBeneficialPercentage: float = 100 - controlGroupBelievesChatGptIsBeneficialPercentage

    # Create Pie Chart
    labels = ['ChatGPT is Beneficial for Learning', 'ChatGPT is not Beneficial for Learning']
    title = 'Is ChatGPT Beneficial for Learning (Non-Frequent Users)'
    sizes = [controlGroupBelievesChatGptIsBeneficialPercentage, controlGroupDoesNotBelieveChatGptIsBeneficialPercentage]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()

    # TEST GROUP
    testGroupBelievesChatGptIsBeneficial: int = sum(respondent.believesChatGptIsBeneficial for respondent in testGroup)
    testGroupBelievesChatGptIsBeneficialPercentage: float = (testGroupBelievesChatGptIsBeneficial / len(testGroup)) * 100
    testGroupDoesNotBelieveChatGptIsBeneficialPercentage: float = 100 - testGroupBelievesChatGptIsBeneficialPercentage

    # Create Pie Chart
    labels = ['ChatGPT is Beneficial for Learning', 'ChatGPT is not Beneficial for Learning']
    title = 'Is ChatGPT Beneficial for Learning (Frequent Users)'
    sizes = [testGroupBelievesChatGptIsBeneficialPercentage, testGroupDoesNotBelieveChatGptIsBeneficialPercentage]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()

def experiment3(respondants: list[Respondent.Respondent]):
    '''
    Do you believe that the use of ChatGPT should be regulated or monitored by universities? - Frequent vs Infrequent Users
    '''

    controlGroup: list[Respondent.Respondent] = []
    testGroup: list[Respondent.Respondent] = []

    for respondent in respondants:
        if respondent.chatGPTUsageFrequency <= 2:
            controlGroup.append(respondent)
        else:
            testGroup.append(respondent)

    # CONTROL GROUP
    controlGroupBelievesChatGptShouldBeRegulated: int = sum(respondent.wantsRegulationOrMonitoring for respondent in controlGroup)
    controlGroupBelievesChatGptShouldBeRegulatedPercentage: float = (controlGroupBelievesChatGptShouldBeRegulated / len(controlGroup)) * 100
    controlGroupDoesNotBelieveChatGptShouldBeRegulatedPercentage: float = 100 - controlGroupBelievesChatGptShouldBeRegulatedPercentage

    # Create Pie Chart
    labels = ['Believes ChatGPT Should be Regulated', 'Does Not Believe ChatGPT Should be Regulated']
    title = 'Do you believe that the use of ChatGPT should be regulated or monitored by universities? \n Infrequent Users'
    sizes = [controlGroupBelievesChatGptShouldBeRegulatedPercentage, controlGroupDoesNotBelieveChatGptShouldBeRegulatedPercentage]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()

    # TEST GROUP
    testGroupBelievesChatGptShouldBeRegulated: int = sum(respondent.wantsRegulationOrMonitoring for respondent in testGroup)
    testGroupBelievesChatGptShouldBeRegulatedPercentage: float = (testGroupBelievesChatGptShouldBeRegulated / len(testGroup)) * 100
    testGroupDoesNotBelieveChatGptShouldBeRegulatedPercentage: float = 100 - testGroupBelievesChatGptShouldBeRegulatedPercentage

    # Create Pie Chart
    labels = ['Believes ChatGPT Should be Regulated', 'Does Not Believe ChatGPT Should be Regulated']
    title = 'Do you believe that the use of ChatGPT should be regulated or monitored by universities? \n Frequent Users'
    sizes = [testGroupBelievesChatGptShouldBeRegulatedPercentage, testGroupDoesNotBelieveChatGptShouldBeRegulatedPercentage]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()

def experiment4(respondants: list[Respondent.Respondent]):
    '''
    Do you think the use of ChatGPT in academic work is beneficial to students' learning? 
    Select only students who have used ChatGPT for "To Learn New Things"
    '''
    controlGroup: list[Respondent.Respondent] = []

    for respondent in respondants:
        if "To Learn New Things" in respondent.chatGPTUses:
            controlGroup.append(respondent)
    

    # CONTROL GROUP
    controlGroupBelievesChatGptIsBeneficial: int = sum(respondent.believesChatGptIsBeneficial for respondent in controlGroup)
    controlGroupBelievesChatGptIsBeneficialPercentage: float = (controlGroupBelievesChatGptIsBeneficial / len(controlGroup)) * 100
    controlGroupDoesNotBelieveChatGptIsBeneficialPercentage: float = 100 - controlGroupBelievesChatGptIsBeneficialPercentage

    # Create Pie Chart
    labels = ['Believes ChatGPT is Beneficial', 'Does Not Believe ChatGPT is Beneficial']
    title = 'Students who use ChatGPT to Learn New Things Opinion of ChatGPT'
    sizes = [controlGroupBelievesChatGptIsBeneficialPercentage, controlGroupDoesNotBelieveChatGptIsBeneficialPercentage]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()


def experiment5(respondants: list[Respondent.Respondent]):
    '''What do you use chatGPT for?'''

    # Create bar graph (Use VS Number of Respondents)
    uses: dict[str, int] = {}
    for respondent in respondants:
        for use in respondent.chatGPTUses:
            if use != "":
                if use in uses:
                    uses[use] += 1
                else:
                    uses[use] = 1

    # Create Bar Graph
    labels = list(uses.keys())
    title = 'Uses of ChatGPT'
    sizes = list(uses.values())

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.bar(labels, sizes)

    # Shrink x-axis text font size 8
    plt.xticks(rotation=0, fontsize=8)

    plt.show()

def experiment6(respondants: list[Respondent.Respondent]):
    "Do you believe that the use of ChatGPT should be regulated or monitored by universities?"

    # Create bar graph (Yes VS No)
    yes: int = 0
    no: int = 0

    for respondent in respondants:
        if respondent.wantsRegulationOrMonitoring:
            yes += 1
        else:
            no += 1

    # Create Bar Graph
    labels = ['Yes', 'No']
    title = 'Do you believe that the use of ChatGPT should be regulated or monitored by universities?'
    sizes = [yes, no]

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.bar(labels, sizes)

    plt.show()

def experiment7(respondants: list[Respondent.Respondent]):
    '''Did you know what ChatGPT was before this survey?'''

    # Create pie graph (Yes VS No)
    yes: int = 0
    no: int = 0

    for respondent in respondants:
        if respondent.knewChatGPT:
            yes += 1
        else:
            no += 1

    # Create Pie Chart
    labels = ['Yes', 'No']
    title = 'Did you know what ChatGPT was before this survey?'
    
    sizes = [yes, no]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()

def experiment8(list: list[Respondent.Respondent]):
    '''Percentage of students in Computer Science who used ChatGPT'''

    # Create pie graph (Yes VS No)
    yes: int = 0
    no: int = 0

    for respondent in list:
        if respondent.program == "Computer Science":
            if respondent.triedChatGPT:
                yes += 1
            else:
                no += 1

    # Create Pie Chart
    labels = ['Yes', 'No']
    title = 'Percentage of students in Computer Science who used ChatGPT'

    sizes = [yes, no]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()

def experiment9(list: list[Respondent.Respondent]):
    '''Should universities allow use of ChatGPT for research purposes only'''

    # Create pie graph (Yes VS No)
    yes: int = 0
    no: int = 0

    for respondent in list:
        if respondent.wantsLegalForResearchOnly:
            yes += 1
        else:
            no += 1

    # Create Pie Chart
    labels = ['Yes', 'No']
    title = 'Should universities allow use of ChatGPT for research purposes only'

    sizes = [yes, no]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    
    plt.show()

def experiment10(list: list[Respondent.Respondent]):
    '''Should universities allow for ChatGPT for academic writing purposes'''

    # Create pie graph (Yes VS No)
    yes: int = 0
    no: int = 0

    for respondent in list:
        if respondent.wantsLegalForAcademicWriting:
            yes += 1
        else:
            no += 1
    
    # Create Pie Chart
    labels = ['Yes', 'No']
    title = 'Should universities allow for ChatGPT for academic writing purposes'

    sizes = [yes, no]
    explode = (0, 0.05)

    fig1, ax1 = plt.subplots()
    ax1.set_title(title)

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()