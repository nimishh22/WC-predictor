# International Football Match Predictor

A machine-learning project for predicting international football match outcomes from historical match data.

## Overview

The project currently builds a baseline prediction pipeline using historical international matches from 2014 onward. It engineers pre-match team features and trains a Random Forest classifier to predict:

- **1** — Home win
- **0** — Draw
- **-1** — Away win

## Current Features

- Recent team form from previous matches
- Average goals scored in recent matches
- Average goals conceded in recent matches
- Neutral-venue indicator
- Tournament context using one-hot encoding

## Model

The current baseline uses a `RandomForestClassifier` from scikit-learn with 100 decision trees.

**Baseline accuracy:** 50.67%

This is an initial benchmark rather than the final model. Future versions will test additional football-specific features and probability-based predictions.

## Tech Stack

- Python
- Pandas
- scikit-learn

## Roadmap

- [ ] Improve early-match feature handling
- [ ] Add win/draw/loss probability predictions
- [ ] Add Elo/team-strength features
- [ ] Add head-to-head features
- [ ] Improve model evaluation with time-aware testing
- [ ] Build a prediction interface
- [ ] Deploy the application

## Project Status

**Version 1 — Baseline model**

The project is actively being developed, with model improvements and a user-facing interface planned for future versions.
