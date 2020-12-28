def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    """Create an intent of the given intent type."""
    import dialogflow_v2 as dialogflow
    intents_client = dialogflow.IntentsClient()

    parent = intents_client.project_agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    response = intents_client.create_intent(parent, intent)

    print('Intent created: {}'.format(response))
    
 
import pandas as pd

project_id = "DIALOGFLOW PROJECT ID"

excelFile = pd.read_excel (r"TRAIN FILE LOCATION")


index=1#index value for excel
#arrays for storing values in order to create intent
training_phrases_parts=[]
display_name=['5'] #initial value for id
message_texts=[]

counter=0
nameCount=0


#iterate untill the end of excel file
for i in excelFile.iterrows():
    #add training phrase to array
    training_phrases_parts.append(i[index].TRAINING_DATA)
    # assign index value from excel
    display_name[0]=i[index].CAT_ID
    #add message texts to array
    message_texts.append(i[index].CAT_NAME)
    #counter for repeating operations
    counter=counter+1
    #create intents in every 300 iteration    
    if counter== 300:
        display_name[0]=str(display_name[0])+"_"+str(nameCount)
        nameCount=nameCount+1
        
        #assign array value to another variable
        dp=display_name[0]
        #create intents
        create_intent(project_id, dp, training_phrases_parts, message_texts)
        
        #reset arrays for other iterations
        training_phrases_parts.clear()
        message_texts.clear()
        counter=0
        
        #remove last character which is _name counter
        if nameCount<=9:
            dp=dp[:-2] 
        elif nameCount<=99:
            dp=dp[:-3]    
        elif nameCount<=999:
            dp=dp[:-4]
        elif nameCount<=9999:
            dp=dp[:-5]
            
        display_name[0]=dp
        
        
    

"""
#control for resetting display name counter
    if display_name[0]!=i[index].CAT_ID:
        nameCount=0
"""
     
    
