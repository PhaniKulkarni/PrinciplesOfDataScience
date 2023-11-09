from chatf import QASystem
def chatbot(input):
    qa = QASystem('data.csv')
    qa_response = qa.get_response(input)
    return qa_response
