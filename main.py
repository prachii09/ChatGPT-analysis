import csv
import Respondent
import Experiments

FILEPATH: str = "CPS 412 - Assignment 1 - Form Responses.csv"

def processResponseInformation() -> list[Respondent.Respondent]:
    ''' Reads the cvs file and returns a list of Response objects '''
    responses: list[Respondent.Respondent] = []
    with open(FILEPATH, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        # Skip the header
        next(reader)

        for row in reader:
            responses.append(Respondent.Respondent(row))

    return responses

if __name__ == "__main__":
    responses: list[Respondent.Respondent] = processResponseInformation()

    # Uncomment the experiment you want to run

    Experiments.experiment1(responses)
    # Experiments.experiment2(responses)
    # Experiments.experiment3(responses)
    # Experiments.experiment4(responses)
    # Experiments.experiment5(responses)
    # Experiments.experiment6(responses)
    # Experiments.experiment7(responses)
    # Experiments.experiment8(responses)
    # Experiments.experiment9(responses)
    # Experiments.experiment10(responses)