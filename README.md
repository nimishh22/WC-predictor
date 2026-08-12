# Predictive Intelligence Engine

A machine-learning system for probabilistic outcome prediction using historical data, statistical feature engineering, and ensemble learning.

> **Current application:** International football match prediction.

## Overview

The project builds a predictive pipeline from historical international match data. It engineers pre-match features and trains a Random Forest classifier to estimate match outcomes.

Current target classes:

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

This is an initial benchmark, not the final model. Future versions will introduce additional statistical and team-strength features, probability-based predictions, and improved evaluation methodology.

## Tech Stack

- Python
- Pandas
- scikit-learn

## Roadmap

- [ ] Improve early-match feature handling
- [ ] Add win/draw/loss probability predictions
- [ ] Add Elo/team-strength features
- [ ] Add head-to-head features
- [ ] Add goal-difference and streak features
- [ ] Improve model evaluation with time-aware testing
- [ ] Build a user-facing prediction interface
- [ ] Deploy the application

## Project Status

**Version 1 — Baseline predictive model**

The system is actively being developed. The long-term goal is to build a robust, interpretable prediction engine with a polished user-facing interface.
