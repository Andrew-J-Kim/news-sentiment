while(True):
    while(True):
        region = input("\nEnter which region you want to analyze:\n"
                       "[0] USA\n[1] Africa\n[2] Asia Pacific\n[3] Australia\n"
                       "[4] Europe\n[5] Latin America\n[6] Middle East\n")
        match region:
            case '0':
                url = 'https://apnews.com/hub/us-news?utm_source=apnewsnav&utm_medium=sections'
                break
            case '1':
                url = 'https://apnews.com/hub/africa?utm_source=apnewsnav&utm_medium=sections'
                break
            case '2':
                url = 'https://apnews.com/hub/asia-pacific?utm_source=apnewsnav&utm_medium=sections'
                break
            case '3':
                url = 'https://apnews.com/hub/australia?utm_source=apnewsnav&utm_medium=sections'
                break
            case '4':
                url = 'https://apnews.com/hub/europe?utm_source=apnewsnav&utm_medium=sections'
                break
            case '5':
                url = 'https://apnews.com/hub/latin-america?utm_source=apnewsnav&utm_medium=sections'
                break
            case '6':
                url = 'https://apnews.com/hub/middle-east?utm_source=apnewsnav&utm_medium=sections'
                break
            case _:
                print("\nSomething is wrong with your input.")

    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h2')

    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sentiment = 0
    for headline in headlines:
        sia = SentimentIntensityAnalyzer()
        ps = sia.polarity_scores(headline.text.strip())
        sentiment = sentiment + ps['compound']
        print('\n' + headline.text.strip())
        print('pos: ' + str(ps['pos']) + ' neg: ' + str(ps['neg']) +
              ' neu: ' + str(ps['neu']) + ' com: ' + str(ps['compound']))

    sentiment = sentiment/len(headlines)
    if (sentiment > 0):
        print("\nNews sentiment is " +
              str(round((sentiment)*100, 2)) + "% positive.")
    else:
        print("\nNews sentiment is " +
              str(round((sentiment)*-100, 2)) + "% negative.")

    while (True):
        repeat = input("\nTry again? (Y/N) ")
        if (repeat == "Y"):
            break
        elif (repeat == "N"):
            quit()
        else:
            print("\nSomething is wrong with your input.")
