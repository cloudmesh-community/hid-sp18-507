import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


ratios = pd.read_csv('ratios.csv', names=['screen_name', 'friends_per_follows'])
#print(ratios[0:10])

history = pd.read_csv('history.csv', names=['screen_name', 'account_age','posts_per_day', 'faves_per_day'])
#print(history[0:10])

combo = pd.merge(ratios, history, on='screen_name', how='outer')


def topten(data, col):
    d = data.sort_values(col, ascending=False)
    return d[['screen_name', col]][0:10]


def flags(data):
    daily_post_flag = [data[['screen_name', 'posts_per_day']].loc[data['posts_per_day'] >= post_threashold].values]
    daily_fave_flag = [data[['screen_name', 'faves_per_day']].loc[data['faves_per_day'] >= faves_threashold].values]
    friend_ratio_flag = [data[['screen_name', 'friends_per_follows']].loc[data['friends_per_follows'] >= ratio_threashold].values]
    return daily_post_flag, daily_fave_flag, friend_ratio_flag


def histograms(data, title, xlab, ylab, color, bins=10):
    fig1 = plt.figure()
    posts = fig1.add_subplot(1,1,1)
    posts.set_title(title)
    posts.set_xlabel(xlab)
    posts.set_ylabel(ylab)
    posts.hist(data, bins=bins, color=color)
    plt.show()


## Produces histograms for three analysis points
print("\n ## PRODUCING HISTOGRAMS ## ")
histograms(combo['posts_per_day'].values.tolist(), 'Posts Per Day', 'Distribution', 'Daily Posts', 'r', 50)
histograms(combo['faves_per_day'].values.tolist(), 'Favorites Per Day', 'Distribution', 'Daily Faves', 'b', 50)
histograms(combo['friends_per_follows'].values.tolist(), 'Friends per Followers', 'Distribution', 'Ratio', 'g', 50)

## Summary data for the combined data-set
print("\n ## SUMMARY DATA ## ")
post_summary = combo['posts_per_day'].describe()
faves_summary = combo['faves_per_day'].describe()
ratio_summary = combo['friends_per_follows'].describe()
print(post_summary)
print(faves_summary)
print(ratio_summary)

## Threasholds for organic users, used to filter out potential spam accounts
post_threashold = (24-8)*(60/10)  # hoursless sleep, times minutes per hour divided by 'posting once ever 10 minutes'
faves_threashold = post_threashold*1.25  # Assumes similar activity frequency as posting; however favouring is easier
ratio_threashold = combo['friends_per_follows'].std()*2

## Dataframes created that weed out potential spam accounts
post_adj = combo[combo['posts_per_day'] <= post_threashold]
faves_adj = combo[combo['faves_per_day'] <= faves_threashold]
ratio_adj = combo[combo['friends_per_follows'] <= ratio_threashold]

## Calculates the delta when filtering out the potential spam accounts
print("\n ## SUMMARY DELTAS ## ")
post_delta = combo['posts_per_day'].describe() - post_adj['posts_per_day'].describe()
faves_delta = combo['faves_per_day'].describe() - faves_adj['faves_per_day'].describe()
ratio_delta = combo['friends_per_follows'].describe() - ratio_adj['friends_per_follows'].describe()
print(post_delta)
print(faves_delta)
print(ratio_delta)

## Produces lists of users and the values that flagged them
post_flag, fave_flag, ratio_flag = flags(combo)

## Print the top 10 users in the analytical categories
print("\n ## TOP 10 POTENTIAL BOTS ## ")
print(topten(combo, 'posts_per_day'))
print(topten(combo, 'faves_per_day'))
print(topten(combo, 'friends_per_follows'))


## Prints the final list of Organic Users
organic = post_adj
organic = organic[organic['faves_per_day'] <= faves_threashold]
organic = organic[organic['friends_per_follows'] <= ratio_threashold]
print(organic.describe())


## Prints the DB summary of Bots
bots = combo.append(organic)
bots = bots[~bots.duplicated(keep=False)]
print(bots.describe())

## Creates a DB of the top10s
bad = pd.merge(topten(combo, 'posts_per_day'), topten(combo, 'faves_per_day'), on='screen_name', how='outer')
bad = pd.merge(bad, topten(combo, 'friends_per_follows'), on='screen_name', how='outer')
# print(bad)
