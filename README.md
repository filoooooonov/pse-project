# Air Pollution and Health Outcomes in US Cities: A Correlation Analysis

## Project Overview
This project investigates the relationship between ambient air quality and various health outcomes across approximately 400 cities in the United States. By combining global air quality data from the World Health Organization (WHO) with national health statistics from the CDC, we aimed to determine if higher concentrations of particulate matter correlate with the prevalence of chronic diseases.

## The Datasets
* **Main Dataset**: US Air quality data for 2020 focusing on PM10 and PM2.5 concentrations.
* **Health Dataset**: US health data from over 3000 cities (2020), utilizing age-adjusted prevalence to mitigate demographic differences.
* **Scope**: The analysis was restricted to 2020 and focused on urban centers with populations exceeding 100,000.

## Technical Methodology
To ensure statistical validity, the following data processing pipeline was implemented:

### 1. Data Cleaning and Merging
* We utilized the `rapidfuzz` library to handle formatting discrepancies in city names, ensuring a high-integrity merge between WHO and CDC data.
* Non-relevant columns (e.g., station types, web links, and references) were dropped to focus strictly on health and pollutant metrics.

### 2. Normality Testing
* A Shapiro-Wilk test was performed on the disease columns.
* The results confirmed that the data was not normally distributed, necessitating a non-parametric approach to correlation.

### 3. Statistical Analysis
* **Spearman Correlation**: We chose this test because it does not require the normality of the data.
* **Weighted Statistics**: A weighted test was implemented to represent the difference in significance of various cities based on their population size.
* **Significance Threshold**: Results were filtered to retain only those with a p-value < 0.05.



## Key Findings
The analysis yielded several significant correlations that provide a nuanced view of urban health:

* **Quality of Life**: Fair or poor self-rated health status and bad physical health showed significant positive correlations with air pollution levels.
* **Respiratory Conditions**: Interestingly, neither asthma nor chronic obstructive pulmonary disease (COPD) showed significant correlation with pollution levels in this dataset.
* **The Cancer Paradox**: Cancer prevalence (excluding skin cancer) was negatively correlated with air pollution.
* **Hidden Variables**: The study found that smoking prevalence also negatively correlated with air pollutants in this dataset, suggesting it acts as a confounding variable for the cancer results.

## Conclusions
The project confirms that while correlation is not causation, air pollution is a significant indicator for overall quality of life metrics. The study demonstrates the importance of considering hidden variables and population movement in environmental health studies.

## Project Contributors (Group 9)
| Member | Primary Responsibilities |
| :--- | :--- |
| **Aleksei Filonov** | Cleaning/merging data, correlation plotting, and presentation. |
| **Anssi Lampinen** | Statistical weighting, visualization, and analysis. |
| **Daniel Tiessalo** | Dataset discovery, cleaning/merging data, and presentation. |
| **Antoni Kajrys** | Method research, statistics, and significance checking. |
| **Ignacio Wąsowicz-Peinado** | Statistics, significance checking, and presentation. |