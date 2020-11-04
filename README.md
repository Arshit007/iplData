# Ipl Data Crawler

The data is taken from https://www.iplt20.com/.

1. The allMatchDetail folder contain all the match details (some mentioned below) in a json file of all the seasons of ipl(2008-2019).
    * ScoreCards of each Team
    * Toss Details
    * Man of the Match
    * Venue Details
    * Detail of every over of the match
    * Match Key Points  

2. The allSeasonStats folder contain  season stats(mentioned below)  in a excel file of all the seasons of ipl(2008-2019).
    * most-runs-over
    * most-fours        
    * most-fours-innings
    * most-sixes        
    * most-sixes-innings
    * most-fifties      
    * most-centuries
    * fastest-fifties
    * fastest-centuries
    * highest-scores
    * highest-scores-innings
    * best-batting-strike-rate
    * best-batting-average
    * biggest-sixes
    * most-wickets
    * most-maidens
    * most-dot-balls
    * most-dot-balls-innings
    * best-bowling-average
    * best-bowling-economy
    * best-bowling-economy-innings
    * best-bowling-strike-rate
    * best-bowling-strike-rate-innings
    * best-bowling-innings
    * most-runs-conceded-innings
    * fastest-balls
    * most-hat-tricks
    * most-four-wickets
    * player-points

## Basic Requirement

1. Python 3.7.3
2. The crawler will work on Windows Operating System

## Installation

1. How to install requirement file.

```bash
pip install -r requirements.txt
```

2. To Run the python crawler use the below command to generate the dataset.

```bash
python ipl.py
```