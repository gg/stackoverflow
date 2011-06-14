#!/bin/sh

USER_DATE=JUN-08-2011

# first day of the month
FIRST_DAY_OF_MONTH=$(date -d "$USER_DATE" +%b-01-%Y)

PREVIOUS_DAY=$(date -d "$USER_DATE -1 days" +%b-%d-%Y)

# last day of the month
FIRST_DAY_NEXT_MONTH=$(date -d "$USER_DATE +1 month" +%b-01-%Y)
LAST_DAY_OF_MONTH=$(date -d "$FIRST_DAY_NEXT_MONTH -1 day" +%b-%d-%Y)

echo "User date: $USER_DATE"
echo "1. First day of the month: $FIRST_DAY_OF_MONTH"
echo "2. Previous day: $PREVIOUS_DAY"
echo "3. Last day of the month: $LAST_DAY_OF_MONTH"
