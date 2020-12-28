# Writing to an excel  
# sheet using Python 
import xlwt 
from xlwt import Workbook 
import xlsxwriter 



workbook = xlsxwriter.Workbook('dialogflowResults.xlsx')
worksheet = workbook.add_worksheet()


def detect_intent_texts(project_id, session_id, texts, language_code):

    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))
    row=1
    
    worksheet.write(0, 0, "CAT_ID") 
    worksheet.write(0, 1, "CAT_NAME") 
    worksheet.write(0, 2, "TRAINING_DATA") 
    worksheet.write(0, 3, "SCORE") 
    
    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
            
        
        worksheet.write(row, 0, response.query_result.intent.display_name) 
        worksheet.write(row, 1, response.query_result.fulfillment_text) 
        worksheet.write(row, 2,response.query_result.query_text) 
        worksheet.write(row, 3,response.query_result.intent_detection_confidence) 
        row+=1
        
    workbook.close()
        
import pandas as pd

project_id = "DIALOGFLOW PROJECT ID"

excelFile = pd.read_excel (r"TEST FILE LOCATION")

queries=[]
counter=0
for i in excelFile.iterrows():
    queries.append(i[1].testdata)
    counter=counter+1
    if counter== 186:
        detect_intent_texts(project_id, "123456789", queries, "tr-TR");
        queries.clear()
        counter=0
        break

   
    
   
