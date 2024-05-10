# 1. Project Start
'''44608-80/81 - Data Fundamentals - P1
This module provides a reusable byline for the author's services.
The goal of this module is to showcase the brand new company "Analytics America" 
skills in the world of consulting and analytics'''

# 2. Import Dependencies-Anything in the standard library is fair game.
import math
import statistics

# 7. Define Main Function-we can call to test our code and display all information.
def main():

  # 3. Define Variables of Different Types-at least one variable of each of these types
  # str, int, float, bool, list of strings, list of numbers.
  company_name: str = "Analytics America"
  company_founding_year: int = 1995
  company_employee_count: int = 44
  company_employee_options: list = ['Remote, Hybrid, or Onsite']
  company_hires_internationally: bool = False
  average_employee_time_worked: float = 10.5
  services_offered: list = [
      "Data Analytics",
      "ML Consulting",
      "BI Solutions",
      "Slides Full of Transition Effects"
  ]
  count_active_projects: int = 8
  average_contract: float = 4.3
  client_satisfaction_scores: list = [
      4.8, 3.8, 5.0, 3.5, 4.5, 4.9, 3.9, 4.8, 3.6
  ]
  accepts_international_clients: bool = True

  # 4. Define Formatted Strings-create formatted strings for non-string variables.
  company_year_string: str = f"Company Founded: {company_founding_year}"
  company_count_string: str = f"Employee Count: {company_employee_count}"
  company_options_string: str = f"Employee Options: {company_employee_options}"
  company_hires_string: str = f"Hires Internationally: {company_hires_internationally}"
  company_work_string: str = f"Average Employee Years: {average_employee_time_worked}"
  services_string: str = f"Services Offered: {services_offered}"
  active_projects_string: str = f"Active Projects: {count_active_projects}"
  average_contract_string: str = f"Average Client Satisfaction: {average_contract}"
  accepts_string: str = f"Accepts International Clients: {accepts_international_clients}"

  #5. Calculate Descriptive Statistics-min(), max(), len(), mean(), mode(), median(),
  # and stdev().
  smallest = min(client_satisfaction_scores)
  largest = max(client_satisfaction_scores)
  total = sum(client_satisfaction_scores)
  count = len(client_satisfaction_scores)
  mean = statistics.mean(client_satisfaction_scores)
  mode = statistics.mode(client_satisfaction_scores)
  median = statistics.median(client_satisfaction_scores)
  standard_deviation = statistics.stdev(client_satisfaction_scores)

  stats_string: str = f"""
  Statistics of Our Client Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total} out of 45!
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
  """

  # 6. Define Byline String ⭐ - display your formatted information. We'll use this 
  # byline in a future project.
  byline: str = f"""
  {company_name}
  {company_year_string}
  {company_count_string}
  {company_options_string}
  {company_hires_string}
  {company_work_string}
  {services_string}
  {active_projects_string}
  {average_contract_string}
  {accepts_string}
  {stats_string}
  """

  print(byline)

if __name__ == '__main__':
  main()
