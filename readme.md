# Sentiment Analyser using VADER Library

[VADER](https://github.com/cjhutto/vaderSentiment) (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. VADER uses a combination of A sentiment lexicon is a list of lexical features (e.g., words) which are generally labelled according to their semantic orientation as either positive or negative.

## Advantages of using VADER
VADER has a lot of advantages over traditional methods of Sentiment Analysis, including:

* It works exceedingly well on *social media type text*, yet readily generalizes to multiple domains

* It doesn’t require any *training data* but is constructed from a generalizable, valence-based, human-curated gold standard sentiment lexicon

* It is fast enough to be *used online with streaming data*, and

* It does not severely suffer from a speed-performance tradeoff.

## Citation Info
- Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

    For more and detailed info: check the main repository
   https://github.com/cjhutto/vaderSentiment/

## Installation
mainly two lib: `vaderSentiment` and `requests`
```python
pip install -r requirement.txt
```

## Usage
Run and check the example data sentiment: 
```python
python sentiment_analyzer.py
```

### Meaning of Scores
* The Positive, Negative and Neutral scores represent the proportion of text that falls in these categories. This
 means our sentence was rated as 67% Positive, 33% Neutral and 0% Negative. Hence all these should add up to 1.

* The Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between
-1(most extreme negative) and +1 (most extreme positive). In the case above, lexicon ratings for and supercool are 2.9
 and respectively 1.3. The compound score turns out to be 0.75 , denoting a very high positive sentiment.

    Compound matrix score
    1. Positive sentiment : `compund score >= 0.05`
    2. Neutral sentiment : `compund score >  -0.05` and `compund score <  0.05`
    3. Negative sentiment : `compund score <= -0.05`