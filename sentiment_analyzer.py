# -- code :UTF-8 --

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

# Scores :
#
# The Positive, Negative and Neutral scores represent the proportion of text that falls in these categories. This
# means our sentence was rated as 67% Positive, 33% Neutral and 0% Negative. Hence all these should add up to
#
# The Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between
# -1(most extreme negative) and +1 (most extreme positive). In the case above, lexicon ratings for and supercool are 2.9
# and respectively 1.3. The compound score turns out to be 0.75 , denoting a very high positive sentiment.
#
# Compound matrix score
# 1. Positive sentiment : `compund score >= 0.05`
# 2. Neutral sentiment : (`compund score >  -0.05`) and (`compund score <  0.05`)
# 3. Negative sentiment : (`compund score <= -0.05`)


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))


if __name__== '__main__':
    sentiment_analyzer_scores("The phone is super cool.")
    sentiment_analyzer_scores("The phone is cool.")
    sentiment_analyzer_scores("The phone is somewhat cool.")

    # Baseline sentence
    print('\n baseline sentence')
    sentiment_analyzer_scores("The food here is good")

    """ VADER analyses sentiments primarily based on certain key points:"""

    # 1. Punctuation: The use of an exclamation mark(!),
    # increases the magnitude of the intensity without modifying the semantic orientation.
    print('\n Punctuation:  using more increases the magnitude of the intensity')
    sentiment_analyzer_scores("The food here is good!")
    sentiment_analyzer_scores("The food here is good!!")
    sentiment_analyzer_scores("The food here is good!!!")

    # 2. Capitalization: Using upper case letters to emphasize a sentiment-relevant word in the presence of other
    # non-capitalized words, increases the magnitude of the sentiment intensity.
    # For example, “The food here is GREAT!” conveys more intensity than “The food here is great!”
    print('\n Capitalization:  emphasize a sentiment-relevant word increases the magnitude of the intensity')
    sentiment_analyzer_scores("The food here is good!")
    sentiment_analyzer_scores("The food here is GOOD!")

    # 3.Degree modifiers: Also called intensifiers, they impact the sentiment intensity by either increasing or
    # decreasing the intensity.
    # For example, “The service here is extremely good” is more intense than “The service here is good”,
    # whereas “The service here is marginally good” reduces the intensity.
    print('\n Intensifiers:  impact the sentiment intensity by either increasing or decreasing the intensity')
    sentiment_analyzer_scores("The food here is good")
    sentiment_analyzer_scores("The food here is extremely good")
    sentiment_analyzer_scores("The food here is moderately good")

    # 4. Conjunctions: Use of conjunctions like “but” signals a shift in sentiment polarity, with the sentiment of the
    # text following the conjunction being dominant. “The food here is great, but the service is horrible”
    # has mixed sentiment, with the latter half dictating the overall rating.
    print('\n Conjunctions:  Use of conjunctions, the sentiment of the text following the conjunction being dominant')
    sentiment_analyzer_scores("The food here is great, but the service is horrible")
    sentiment_analyzer_scores("The service is horrible but the food here is great")

    # 5. Preceding Tri-gram: By examining the tri-gram preceding a sentiment-laden lexical feature, we catch nearly 90%
    # of cases where negation flips the polarity of the text.
    # A negated sentence would be “The food here isn’t really all that great”.
    print('\n Preceding Tri-gram:  examining the tri-gram preceding a sentiment-laden lexical feature')
    sentiment_analyzer_scores("The food here isn’t really all that great")
    sentiment_analyzer_scores("The food here isn’t really not that great")

    """ Handling Emojis, Slangs and Emoticons. """
    # Emojis
    print("\n Emoji")
    sentiment_analyzer_scores('I am 😄 today')
    sentiment_analyzer_scores('😊')
    sentiment_analyzer_scores('😥')
    sentiment_analyzer_scores('☹️')
    sentiment_analyzer_scores('lol')

    # Slangs
    print("\n Slangs")
    sentiment_analyzer_scores("Today SUX!")
    sentiment_analyzer_scores("Today only kinda sux! But I'll get by, lol")

    # Emoticons
    print("\n Emoticons")
    sentiment_analyzer_scores("Make sure you :) or :D today!")
    sentiment_analyzer_scores("Make sure you 😊 or 😄 today!")
