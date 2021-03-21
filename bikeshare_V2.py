
    
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 12:04:50 2021

@author: Ahmed.Senam
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': r'D:\Ahmed_Senam\Data_Analytics_udacity\Project_1\chicago.csv',
              'new york city': r'D:\Ahmed_Senam\Data_Analytics_udacity\Project_1\new_york_city.csv',
              'washington': r'D:\Ahmed_Senam\Data_Analytics_udacity\Project_1\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Enter city name from (chicago, new york city, washington): ').lower(
        ))
        if city in ['chicago', 'new york city', 'washington']:
            break
        print('Please enter one of above cities only')

        print(city)
   

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Enter month name from (january, february, march, april, may, june or all): ').lower())
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        print('Please enter one of above mothes only')

    print(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Enter day name from (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all: ').title(
        ))
        if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday', 'All']:
            break
        print('Please enter one of above days only')

    print(day)
   

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df
####################################################################

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most Common day of week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    
#########################################################################

#########################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    print('Most Common start station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Common End station:', popular_end_station)

 # TO DO: display most frequent combination of start station and end station trip

    frequent_combination = (df['Start Station'] + ' _AND_ ' + df['End Station']).mode()[0]
    print('most frequent combination of start station _AND_ end station trip: ', str(frequent_combination))
                                                    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

########################################################################

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    travel_time= df['Trip Duration'].sum()
    print('Total travel time: ', travel_time)

    # TO DO: display mean travel time
    travel_time_mean= df['Trip Duration'].mean()
    print('mean travel time: ', travel_time_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#################################################################
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('counts of user types \n', user_types)

    # TO DO: Display counts of gender
    if city == 'chicago' or city == 'new_york_city':    
        gender = df['Gender'].value_counts()
        print('counts of gender: \n', gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_birth = df['Birth Year'].min()
        print('earliest birth year: ',earliest_year_birth)
        
        most_recent_year_birth = df['Birth Year'].max()
        print('most recent birth year: ', most_recent_year_birth)
        most_common_year_birth = df['Birth Year'].mode()[0]
        print('most common birth year: ', most_common_year_birth)    
        
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
###############################################################

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        x=0
        
        while True:
       
            view_5_line = input('Do you want to view 1st five lines of data?\n Enter yes or no\n').lower()
            if view_5_line.lower() == 'yes':
            
                print(df.head())
        
                while True:
                    view_more_line = input('Do you want to view five more lines of data?\n Enter yes or no\n').lower()
                    if view_more_line.lower() != 'yes':
                        break
                
                    x = x+5
                    print(df.iloc[x:x+5])
                    
            break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
