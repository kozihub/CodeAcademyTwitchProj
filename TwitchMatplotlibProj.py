
from matplotlib import pyplot as plt

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]


ax = plt.subplot()
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation = 45)
plt.bar(range(len(games)), viewers, color='blue')
plt.title('Game vs Number of Viewers')
plt.xlabel('Game')
plt.ylabel('Number of Viewers')
plt.legend(['Twitch'])
plt.show()
plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'paleturquoise', 'sienna', 'khaki', 'gold', 'violet', 'lightseagreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


plt.pie(countries, explode = explode, colors = colors, shadow = True, startangle = 345, autopct='%1.0f%%', pctdistance=1.15)
plt.title('League of Legends Viewers Country')
plt.legend(labels, loc='right')
plt.show()

plt.clf()
# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

y_lower = [i - (i*.15) for i in viewers_hour]
y_upper = [i + (i*.15) for i in viewers_hour]

plt.fill_between(hour, y_lower, y_upper, alpha=.2)
plt.plot(hour, viewers_hour)
ax3 = plt.subplot()
ax3.set_xticks(hour)
ax3.set_xticklabels(['12am', '1am','2am','3am','4am','5am','6am','7am','8am','9am','10am','11am','12pm','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm','10pm','11pm'], rotation = 60)
plt.title('Number of Viewers per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Viewers')
plt.legend(['2015-01-01'])

plt.show()