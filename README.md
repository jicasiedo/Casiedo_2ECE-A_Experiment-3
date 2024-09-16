### ECE 2112: Advanced Computer Programming and Algorithms
---
# **Experiment 3: Python Data Analysis (Pandas)**
### Submitted by: **Jihan Harvey C. Casiedo**
#### Section: 2ECE-A
---
### **Background of the Experiment**
##### Pandas is a core Python library designed for high-performance, easy-to-use data structures and data analysis tools. It can handle tabular data with mixed data types, similar to SQL tables or Excel spreadsheets, and supports both ordered and unordered time series data. Pandas can also work with arbitrary matrix data (homogeneous and heterogeneous types) and offer powerful capabilities for managing and analyzing a wide range of observational or statistical datasets.
---
### **Objectives of the Experiment**
##### This experiment aims for students to identify the codes and functions incorporated in the Pandas library and be able to apply and use the different codes and functions in creating a Python program using a Pandas library.
---
### **Instructions**
##### Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin. 

##### For this programming assignment, download the following file and save to your default user folder: http://bit.ly/Cars_file
---

### **Problem 1**
##### Using the .csv file, load the file into a data frame named cars using pandas. Then, display the first five and last five rows of the resulting cars.

---
### **Problem 1 Code**
##### Import the Pandas library and load and display the .csv file into the code

``` js
import pandas as pd
cars = pd.read_csv('cars.csv')
cars
```
##### *Result:*
![Screenshot 2024-09-15 171144](https://github.com/user-attachments/assets/574d1f99-065e-40de-b192-13dc61e5e0d1)
---
#

##### Use the cars.head() function to display the first five cars in the data frame.

``` js
cars.head() 
```
##### *Result:*
![Screenshot 2024-09-15 172358](https://github.com/user-attachments/assets/cae8262d-c274-4541-b7dd-417d91a26570)
---
#

##### Use the cars.tail() function to display the last five cars in the data frame.

``` js
cars.tail()
```
##### *Result:*
![Screenshot 2024-09-15 172518](https://github.com/user-attachments/assets/d004e1e7-d64c-4818-bca0-97f3a0ac4904)


---

### **Problem 2**
##### Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
#####     a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
##### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
##### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
##### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

---
### **Problem 2 Code**
##### Import the Pandas library and load the .csv file into the code.

``` js
import pandas as pd

cars = pd.read_csv('cars.csv') 
```

---
#

#####  Use the car.iloc[:5, ::2] function to display the first five rows with odd-numbered columns of cars.

``` js
cars.iloc[:5, ::2] 
```
##### *Result:*
![Screenshot 2024-09-15 173444](https://github.com/user-attachments/assets/e6f04b2d-4648-45b0-91b7-8ab5618d342b)
---
#

##### Use this function to display the row containing the car model 'Mazda RX4'

``` js
cars.loc[cars['Model'] == 'Mazda RX4']
```
##### *Result:*
![Screenshot 2024-09-15 173623](https://github.com/user-attachments/assets/34eda3bb-d13a-4799-ab95-2d789c7c25d9)
#

#####  Use this function to display the number of 'cyl' the model 'Camaro Z28' has.

``` js
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]
```
##### *Result:*
![Screenshot 2024-09-15 173648](https://github.com/user-attachments/assets/929d3e91-a38c-45ec-a972-e42ed54bfc8d)---
#

#####  Use this function to display how many cyl and what gear type the Models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have.

``` js
cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
         (cars['Model'] == 'Ford Pantera L')|
         (cars['Model'] == 'Honda Civic') ,['Model','cyl','gear']] 
```
##### *Result:*
![Screenshot 2024-09-15 173946](https://github.com/user-attachments/assets/5b173cd0-2b1d-4d65-81f7-696bd3580ed9)
---



### **Conclusion**
##### This experiment allows students to explore the functions of the Pandas library and apply them to solve the given problems. By applying  the understanding of the Pandas library, students will be able to efficiently manipulate data and create Python programs, enhancing their data analysis skills
