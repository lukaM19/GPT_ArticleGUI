from newspaper import Article
import openai

def extract_article_text(url):
    # Create an Article object from the URL
    article = Article(url)

    # Download and parse the article
    article.download()
    article.parse()

    # Extract the main text from the article
    article_text = article.text

    return article_text

# Replace 'your_url_here' with the URL of the article you want to extract
#article_text = extract_article_text(url)

#print("Extracted Article Text:")
#print(article_text)

def chat_gpt_api(question):
    # Replace 'your_api_key_here' with your actual API key
    openai.api_key = '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'

    # Set up the API request parameters
    model = 'gpt-3.5-turbo'  # You can use other GPT models like 'text-curie-002' or 'text-babbage-002'
    prompt = f"{question}"
    max_tokens = 100
    n = 1
    stop = None
    temperature = 0.7
    # Make the API call
    response = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
         messages=[
        {"role": "user", "content": question}
    ]
    )
    print(response)
    # Extract the answer from the API response
    answer =str( response.choices[0].message.content)
    print(answer)
    return answer

# Replace 'your_question_here' with the question you want to ask
#question = article_text
#answer = chat_gpt_api(question)

#print("Answer:")
#print(answer)