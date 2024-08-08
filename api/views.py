from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# Replace these with your actual URL and headers
#url = 'https://your-graphql-endpoint.com/graphql'
#headers = {
 #   'Content-Type': 'application/json',
  #  'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # If you need authorization
#}

def get_question_of_the_day():
    query = """
    query questionOfToday {
      activeDailyCodingChallengeQuestion {
        question {
          title
          titleSlug
        }
      }
    }
    """
    payload = {
        "query": query,
        "variables": {},
        "operationName": "questionOfToday"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        question = data['data']['activeDailyCodingChallengeQuestion']['question']
        return question
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')
        return None

@api_view(['GET'])
def question_of_the_day(request):
    question = get_question_of_the_day()
    if question:
        return Response(question)
    else:
        return Response({'error': 'Failed to retrieve question'}, status=500)
