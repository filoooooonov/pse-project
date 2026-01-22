# Air Pollution and Health Outcomes in US Cities: A Correlation Analysis

## Project Overview
[cite_start]This project investigates the relationship between ambient air quality and various health outcomes across approximately 400 cities in the United States[cite: 18]. [cite_start]By combining global air quality data from the World Health Organization (WHO) with national health statistics from the CDC, we aimed to determine if higher concentrations of particulate matter correlate with the prevalence of chronic diseases[cite: 17, 54, 55].

## The Datasets
* [cite_start]**Main Dataset**: US Air quality data for 2020 focusing on PM10 and PM2.5 concentrations[cite: 18, 25, 26].
* **Health Dataset**: US health data from over 3000 cities (2020), utilizing age-adjusted prevalence to mitigate demographic differences.
* **Scope**: The analysis was restricted to 2020 and focused on urban centers with populations exceeding 100,000.

## Technical Methodology
To ensure statistical validity, the following data processing pipeline was implemented:

### 1. Data Cleaning and Merging
* We utilized the `rapidfuzz` library to handle formatting discrepancies in city names, ensuring a high-integrity merge between WHO and CDC data.
* [cite_start]Non-relevant columns (e.g., station types, web links, and references) were dropped to focus strictly on health and pollutant metrics[cite: 39, 77].

### 2. Normality Testing
* [cite_start]A Shapiro-Wilk test was performed on the disease columns[cite: 161].
* [cite_start]The results confirmed that the data was not normally distributed, necessitating a non-parametric approach to correlation[cite: 161, 162].

### 3. Statistical Analysis
* [cite_start]**Spearman Correlation**: We chose this test because it does not require the normality of the data[cite: 162].
* [cite_start]**Weighted Statistics**: A weighted test was implemented to represent the difference in significance of various cities based on their population size[cite: 163].
* [cite_start]**Significance Threshold**: Results were filtered to retain only those with a p-value < 0.05[cite: 165].



## Key Findings
The analysis yielded several significant correlations that provide a nuanced view of urban health:

* [cite_start]**Quality of Life**: Fair or poor self-rated health status and bad physical health showed significant positive correlations with air pollution levels[cite: 325, 326].
* [cite_start]**Respiratory Conditions**: Interestingly, neither asthma nor chronic obstructive pulmonary disease (COPD) showed significant correlation with pollution levels in this dataset[cite: 327, 328].
* [cite_start]**The Cancer Paradox**: Cancer prevalence (excluding skin cancer) was negatively correlated with air pollution[cite: 323].
* [cite_start]**Hidden Variables**: The study found that smoking prevalence also negatively correlated with air pollutants in this dataset, suggesting it acts as a confounding variable for the cancer results[cite: 538].

## Conclusions
[cite_start]The project confirms that while correlation is not causation, air pollution is a significant indicator for overall quality of life metrics[cite: 518, 519, 529]. [cite_start]The study demonstrates the importance of considering hidden variables and population movement in environmental health studies[cite: 538, 540].

## Project Contributors (Group 9)
| Member | Primary Responsibilities |
| :--- | :--- |
| **Aleksei Filonov** | [cite_start]Cleaning/merging data, correlation plotting, and presentation[cite: 567, 568, 569, 570, 571]. |
| **Anssi Lampinen** | [cite_start]Statistical weighting, visualization, and analysis[cite: 5, 572, 573, 574]. |
| **Daniel Tiessalo** | [cite_start]Dataset discovery, cleaning/merging data, and presentation[cite: 3, 575, 576, 577]. |
| **Antoni Kajrys** | [cite_start]Method research, statistics, and significance checking[cite: 4, 578, 579, 580]. |
| **Ignacio Wąsowicz-Peinado** | [cite_start]Statistics, significance checking, and presentation[cite: 6, 581, 582, 583]. |