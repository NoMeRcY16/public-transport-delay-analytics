# Public Transport Delay Analytics

A machine-learning project that explores public transport delays, travel time, passenger demand, traffic conditions, and weather using simulated data.

## Project Overview

Public transport delays can affect passenger waiting time, journey duration, and route planning. This project builds an initial machine-learning workflow to estimate delay minutes from journey and operating conditions.

> **Note:** The current dataset is synthetic (dummy data) created for learning and demonstration. Predictions are not real-world forecasts and should not be used for actual travel decisions.

## Objectives

- Generate sample public transport journey data.
- Explore factors such as route, departure hour, passenger count, traffic, weather, and scheduled travel time.
- Train a regression model to estimate delay in minutes.
- Evaluate predictions and compare actual versus predicted delay values.
- Establish a foundation for future visual analytics and a dashboard.

## Tools and Technologies

- **Python**
- **Google Colab** for browser-based development
- **Pandas and NumPy** for data preparation and synthetic data generation
- **Matplotlib** for visualization
- **Scikit-learn** for preprocessing, model training, and evaluation
- **GitHub** for version control and project sharing

## Machine-Learning Workflow

1. Generate synthetic journey data.
2. Separate input features from the target (`delay_minutes`).
3. Encode categorical features and pass through numeric features.
4. Split the dataset into training and testing sets.
5. Train a `RandomForestRegressor`.
6. Evaluate model predictions using regression metrics.
7. Visualize actual versus predicted delay values.
8. Test the model with a sample journey.

## Example Input Features

| Feature | Description |
|---|---|
| `route` | Sample route identifier |
| `hour` | Departure hour |
| `passenger_count` | Simulated passenger count |
| `traffic_level` | Low, Medium, or High |
| `weather` | Clear, Cloudy, or Rainy |
| `scheduled_travel_minutes` | Scheduled journey duration |
| `delay_minutes` | Target value the model estimates |

## How to Run

1. Open the notebook in this repository.
2. Choose **Open in Colab** if the option is available, or upload the `.ipynb` file to [Google Colab](https://colab.research.google.com/).
3. Run the cells from top to bottom.
4. Review the generated dataset, evaluation metrics, visualizations, and sample prediction.

No local Python installation is required to run the notebook in Google Colab.

## Current Status

- [x] Synthetic dataset generation
- [x] Initial Random Forest regression model
- [x] Actual-versus-predicted visualization
- [ ] Document model evaluation results
- [ ] Add route- and time-based exploratory analysis
- [ ] Build an interactive dashboard
- [ ] Validate using a real, suitable public transport dataset

## Future Improvements

- Use real historical arrival and departure data.
- Analyze delay patterns by route, stop, and time of day.
- Compare multiple regression models and report MAE, RMSE, and R².
- Build an interactive dashboard for route-level insights.
- Clearly document data sources, limitations, and model performance.

## Disclaimer

This is an educational prototype using simulated data. Since the data is synthetic, strong model performance would not prove that the model can accurately predict delays in a real transport network.
