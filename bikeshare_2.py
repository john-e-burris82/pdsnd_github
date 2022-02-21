import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Utilize while True: loops
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Select City: Chicago, New York City, Washington: ").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Your selection is invalid, please try again!")
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Select month: All, January, February, March, April, May, or June: ").lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('Month is invalid, please try again.')
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Select Day: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ").lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print("Your day is invalid, please try again.")
            continue
        else:
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
#Retrieve and load correct city
    df = pd.read_csv(CITY_DATA[city])
#Converts DTG
    df['Start Time'] =pd.to_datetime(df['Start Time'])
#Creates new columns for analysis
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour
#Filter by month
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

#Filter by weekday
    if day != 'all':
        df = df[df['week_day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    busy_month = df['month'].mode()[0]
    print("The busiest month: ", busy_month)

    # TO DO: display the most common day of week
    print("The busiest day:", df['week_day'].mode()[0])

    # TO DO: display the most common start hour
    print("The busiest starting hour:", df['start_hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The busiest start station:", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The busiest end station:", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['common_trip'] = df['Start Station'] + " to " + df['End Station']
    print("The busiest route is:", df['common_trip'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time in hours for your selection:", int(sum((df['Trip Duration']) / 60) / 60))

    # display mean travel time
    print("The average travel time in minutes:", int(df['Trip Duration'].mean() % 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count by usertype:\n", df.groupby(['User Type'])['User Type'].count())

    # Display counts of gender
    try:
        print("Usage by gender:\n", df.groupby(['Gender'])['Gender'].count())
    # Display earliest, most recent, and most common year of birth
        print("Subscriber birth year stats:\n")
        print("Oldest Subscriber Birth Year:\n", int(df['Birth Year'].min()))
        print("Youngest Suscriber Birth Year:\n", int(df['Birth Year'].max()))
        print("Most Common Birth Year:\n", int(df['Birth Year'].mode()[0]))
    except KeyError:
        print("Washington does not have additional information!")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw(df):
    """Displays raw data if the users wishes to see it."""
    x = 1
    while True:
        raw = input("Do you want to view the raw data? Yes or No:  ")
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()