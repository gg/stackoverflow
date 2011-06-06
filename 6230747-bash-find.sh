#!/bin/sh

for line in $(find $1 -type f); do
  echo $line
  echo good morning
done
