import numpy as np
import pandas as pd
import xlsxwriter



###### IMPORT EXCEL AND CONVERT INTO A MATRIX to manipulate
InputTechToEffort = pd.read_excel(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\MatrixData.xlsx",
                                  sheet_name='TechToEffort')
#print(InputTechToEffort)

InputBiasToEffort = pd.read_excel(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\MatrixData.xlsx",
                                  sheet_name='BiasToEffort')
#print(InputBiasToEffort)

##turn into a matrix
T2E_Matrix = np.array(InputTechToEffort.values)
T2E_Matrix = T2E_Matrix.tolist()
First_row = ['Tech & Effort',
               '1. Examining fewer cues.',
               '2. Reducing the difficulty associated with retrieving and storing cue values.',
               '3. Simplifying the weighting principles for cues.',
               '4. Integrating less information.',
               '5. Examining fewer alternatives.']
T2E_Matrix.insert(0, First_row)
#print('T2E_Matrix')
#print(T2E_Matrix)

B2E_Matrix = np.array(InputBiasToEffort.values)
B2E_Matrix = B2E_Matrix.tolist()
First_row_2 = ['Bias & Effort',
               '1. Examining fewer cues.',
               '2. Reducing the difficulty associated with retrieving and storing cue values.',
               '3. Simplifying the weighting principles for cues.',
               '4. Integrating less information.',
               '5. Examining fewer alternatives.']
B2E_Matrix.insert(0, First_row_2)

#print('B2E_Matrix')
#print(B2E_Matrix)

############################ GENERATE Bias to Tech via effort

#create blank Bias x Tech matrix

print("B2T_Matrix")
B2T_Matrix = []
row_array = []

#adding headers
for i in range(1,len(T2E_Matrix)):
    row = T2E_Matrix[i]
    item = row[0]
    #print('printing item')
    #print(item)
    row_array.append(item)
    #print('printing row array')
    #print(row_array)
row_array.insert(0,'Bias to Tech')
B2T_Matrix.append(row_array)

#print(row_array2)

#adding row labels
for j in range (1, len(B2E_Matrix)):
    row_array2 = [0] * (len(T2E_Matrix) - 1)
    row = B2E_Matrix[j]
    item = row[0]
    row_array2.insert(0, item)
    B2T_Matrix.append(row_array2)

#print(B2T_Matrix)

#calculate over degree of effort link

#iterated over rows
for i in range(1,len(B2E_Matrix)): #len(B2E) counts the number of rows in the Bias to Effort matrix, ie the number of biases
    #iteratre over column
    for j in range (1, len(T2E_Matrix)): #len(T2E) counts the number of rows in the Tech to Effort matrix, ie number of tech
        degree_count = 0
        for a in range(1,6):
            if B2E_Matrix[i][a] == 1 and T2E_Matrix[j][a] == 1:
                degree_count = degree_count +1
        B2T_Matrix[i][j] = degree_count

#print(B2T_Matrix)
#print(np.asarray(B2T_Matrix))
df = pd.DataFrame(np.asarray(B2T_Matrix))
writer = pd.ExcelWriter(r"C:\Users\Lenovo\Dropbox\UCL\4th year modules\TKE\MATRIX PROGRAM\B2TMatrix.xlsx")
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
